import os
import logging
import subprocess
from snowflake import connector
import json
from snowflake.core import Root
from endpoints.log_utils import logger


logging.getLogger("snowflake.connector.cursor").setLevel(logging.WARNING)
logging.getLogger("snowflake.connector.connection").setLevel(logging.WARNING)
logging.getLogger("snowflake.core").setLevel(logging.WARNING)


def __get_token():
    # https://github.com/snowflakedb/snowflake-cli/blob/main/src/snowflake/cli/_plugins/spcs/image_registry/manager.py#L35

    with connector.connect() as connection:
        result = connection.execute_string(
            "alter session set PYTHON_CONNECTOR_QUERY_RESULT_FORMAT = 'json'"
        )
        # disable session deletion
        connection._all_async_queries_finished = lambda: False

        token_data = connection._rest._token_request("ISSUE")
        return {
            "token": token_data["data"]["sessionToken"],
            "expires_in": token_data["data"]["validityInSecondsST"],
        }


def login_to_image_registry():
    try:
        subprocess.call(["snow", "spcs", "image-registry", "login"])
    except FileNotFoundError:
        logger.debug("snowcli not installed")
        token_info = __get_token()

        commands = [
            "docker",
            "login",
            "-u",
            "0sessiontoken",
            "--password-stdin",
            os.environ["DOCKER_REGISTRY"],
        ]

        result = subprocess.check_output(
            commands, input=json.dumps(token_info), text=True, stderr=subprocess.PIPE
        )
        logger.info(result)


def push_docker_image(image_name, repository_url):
    logger.info(f"Pushing image {image_name} to {repository_url}")
    subprocess.call(["docker", "tag", image_name, repository_url])

    login_to_image_registry()
    subprocess.call(["docker", "image", "push", repository_url])


def deploy(
    service_name,
    compute_pool_name,
    warehouse_name,
    image_path,
    udf_name,
    connection_name=None,
):
    try:
        # Override default connection
        set_snowflake_env(connection_name=connection_name)

        create_warehouse(warehouse_name)

        create_compute_pool(
            compute_pool_name
        )  # Uses default value 1 for min_nodes and max_nodes

        create_service(service_name, compute_pool_name, image_path)

        create_udf(udf_name, service_name)
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        stop_all(service_name, udf_name, compute_pool_name)


def set_snowflake_env(connection_name):
    if connection_name:
        os.environ["SNOWFLAKE_DEFAULT_CONNECTION_NAME"] = connection_name


def create_warehouse(
    warehouse_name, warehouse_size="XSMALL", warehouse_type="STANDARD"
):
    with connector.connect() as conn:
        logger.info(f"Creating warehouse {warehouse_name} if doesn't exist..")
        with conn.cursor() as curr:
            curr.execute(
                f"CREATE WAREHOUSE IF NOT EXISTS {warehouse_name} WAREHOUSE_SIZE = '{warehouse_size}' WAREHOUSE_TYPE = '{warehouse_type}'"
            )


def create_compute_pool(compute_pool_name, min_nodes=1, max_nodes=1):
    with connector.connect() as conn:
        logger.info("Creating compute pool if doesn't exist..")

        conn.cursor().execute(
            f"CREATE COMPUTE POOL IF NOT EXISTS {compute_pool_name} INSTANCE_FAMILY = CPU_X64_M MIN_NODES={min_nodes} MAX_NODES={max_nodes} AUTO_RESUME = true;"
        )


def create_service(service_name, compute_pool_name, image_path):
    warehouse = connector.connection.SnowflakeConnection().warehouse
    command = f"""
        CREATE SERVICE IF NOT EXISTS {service_name}
        IN COMPUTE POOL {compute_pool_name}
        QUERY_WAREHOUSE={warehouse}
        MIN_INSTANCES=1
        MAX_INSTANCES=1
        FROM SPECIFICATION $$
            spec:
              containers:
                - name: jsl-container
                  image: {image_path}
                  args:
                    - serve
                  env:
                    SERVER_PORT: 8080
                    LOG_LEVEL: DEBUG
                  readinessProbe:
                    port: 8080
                    path: /ping
              endpoints:
                - name: predictionendpoint
                  port: 8080
                  public: true
            $$
        ;
        """
    with connector.connect() as conn:
        logger.info("Executing service creation if doesn't exist..")
        conn.cursor().execute(command)


def get_service_status(service_name, connection_name):
    try:
        set_snowflake_env(connection_name=connection_name)
        with connector.connect() as conn:
            schema = connector.connection.SnowflakeConnection().schema
            logger.info(f"Using schema: {schema}")
            logger.info(f"Checking status of service: {service_name}..")
            with conn.cursor() as cur:
                cur.execute(f"SELECT SYSTEM$GET_SERVICE_STATUS('{service_name}');")
                result = cur.fetchone()
                logger.info(f"{result}")
                return result
    except Exception as e:
        logger.info(f"An error occurred: {e}")


def create_udf(udf_name, service_name):
    command = f"""
        CREATE OR REPLACE FUNCTION {udf_name} (TEXT VARCHAR)
        RETURNS varchar
        SERVICE={service_name}
        ENDPOINT=predictionendpoint
        AS '/invoke';
        """
    with connector.connect() as conn:
        logger.info("Creating function..")
        conn.cursor().execute(command)


def stop_all(service_name, drop_compute_pool: bool = False, connection_name=None):

    set_snowflake_env(connection_name=connection_name)
    with connector.connect() as conn:
        logger.info("Removing services and functions..")
        associated_compute_pool = get_compute_pool(service_name)
        conn.cursor().execute(f"DROP SERVICE IF EXISTS {service_name};")
        conn.cursor().execute(f"DROP FUNCTION IF EXISTS prediction_udf(varchar);")

        if associated_compute_pool:
            if drop_compute_pool:
                logger.info("Removing compute pool..")
                conn.cursor().execute(
                    f"DROP COMPUTE POOL IF EXISTS {associated_compute_pool};"
                )
            else:
                logger.info("Suspending compute pool..")
                conn.cursor().execute(
                    f"ALTER COMPUTE POOL IF EXISTS {associated_compute_pool} SUSPEND;"
                )
        else:
            logger.info("Service or Compute pool doesn't exist")


def get_compute_pool(service_name):
    try:
        connection = connector.connect()
        db = connection.database
        schema = connection.schema
        root = Root(connection)

        my_service = root.databases[db].schemas[schema].services[service_name].fetch()

        return my_service.compute_pool if my_service else None
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
    finally:
        connection.close()


def get_image_repository(repo_name, db, schema, snowflake_root: Root):
    my_repo = None
    try:
        my_repo_res = (
            snowflake_root.databases[db].schemas[schema].image_repositories[repo_name]
        )
        my_repo = my_repo_res.fetch()
    except Exception as e:
        logger.error(f"Repository {repo_name} not found.")
    return my_repo


def create_image_repository(repo_name, db, schema, snowflake_root: Root):
    from snowflake.core.image_repository import ImageRepository

    repo = snowflake_root.databases[db].schemas[schema].image_repositories
    repo.create(ImageRepository(repo_name))


def create_image_repository_if_not_exists(repo_name, db=None, schema=None):

    try:
        with connector.connect() as connection:
            db = connection.database if not db else db
            schema = connection.schema if not schema else schema
            root = Root(connection)

            logger.info(f"Checking if repository {repo_name} exists..")
            my_repo = get_image_repository(repo_name, db, schema, root)

            if my_repo:
                logger.info(f"Repository already exists..")
            else:
                logger.info(f"Creating repository {repo_name}..")
                create_image_repository(
                    repo_name=repo_name, db=db, schema=schema, snowflake_root=root
                )
                print("databases ", root.databases[db])

                my_repo = get_image_repository(repo_name, db, schema, root)

            return my_repo.repository_url if my_repo else None
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        raise e
