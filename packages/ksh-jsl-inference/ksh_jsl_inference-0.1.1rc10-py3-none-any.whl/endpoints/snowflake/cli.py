import subprocess

import click

from endpoints.cli import internals
from endpoints.cli.options import common_options
from endpoints.log_utils import logger
from endpoints.settings import DEFAULT_IMAGE_REPOSITORY_NAME
from endpoints.snowflake import components
from endpoints import Platform, Recipe


def connection_options(f):
    """
    A decorator to use connection-name configuration options overriding default
    Snowflake connection specififed on config.toml
    """
    f = click.option(
        "--connection-name",
        help="Snowflake connection-name to use. This overrides default configuration of config.toml file",
    )(f)
    return f


@click.group()
def snowflake():
    """
    Group of commands related to Snowflake functionality.
    """
    pass


@snowflake.command()
@common_options
@click.option(
    "--output-dir",
    help="Output directory for the Docker files. If not provided, a default directory will be used.",
)
def generate_docker_files(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Snowflake.
    """

    output_dir = internals._generate_docker_files(
        model=model,
        platform=Platform.SNOWFLAKE,
        **kwargs,
    )


@snowflake.command()
@common_options
@click.option(
    "--image-name",
    default=None,
    help="Name of the Docker image to build. Defaults to the model name if not provided.",
)
@click.option(
    "--license-path",
    required=False,
    help="Path to the license file required to build the Docker image.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable Docker cache during build.",
)
def build_docker_image(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Snowflake.
    """
    internals.build_docker_image(model, platform=Platform.SNOWFLAKE, **kwargs)


@snowflake.command()
@click.option("--model", required=False, help="The model to run locally.")
@click.option(
    "--language",
    required=False,
    default="en",
    help="Language of the model to load (default: 'en')",
)
@click.option(
    "--inference_model",
    required=False,
    help="Inference model to use. Must be a subclass of BaseInference",
)
@click.option(
    "--recipe",
    required=False,
    type=click.Choice([recipe.value for recipe in Recipe], case_sensitive=False),
    default=Recipe.HEALTHCARE_NLP.value,
    help="Recipe to use. Valid values: "
    + ", ".join([recipe.value for recipe in Recipe]),
)
@click.option("--port", required=False, default=8080)
def run_local(model: str, language: str, inference_model: str, recipe: str, port: int):
    """Run a local instance of the Snowflake Inference container"""
    internals.run_local(
        model=model,
        language=language,
        inference_model=inference_model,
        platform=Platform.SNOWFLAKE,
        recipe=Recipe(recipe),
        port=port,
    )


@snowflake.command()
@common_options
@click.option(
    "--image-repo-path",
    help="Path of snowflake repository where docker image is to be pushed",
)
@click.option(
    "--license-path",
    required=False,
    help="Path to the license file required to build the Docker image.",
)
@click.option(
    "--service-name",
    default="prediction_service",
    help="Service name (default: 'prediction_service')",
)
@click.option(
    "--compute-pool-name",
    required=True,
    help="Compute Pool name",
)
@connection_options
def deploy(
    model,
    image_repo_path=None,
    compute_pool_name=None,
    service_name=None,
    connection_name=None,
    **kwargs,
):
    image_name_with_tag = f"{model}:latest"
    # Check if docker image exists
    # If exists, skip creating docker image.
    try:
        process_result = subprocess.call(
            ["docker", "image", "inspect", image_name_with_tag],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        if process_result != 0:
            logger.info(
                f"Couldn't find docker image - {image_name_with_tag}. Creating it.."
            )
            internals.build_docker_image(
                model=model, platform=Platform.SNOWFLAKE, **kwargs
            )

        db = schema = None
        # image_repo_path = kwargs.get("image_repo_path", None)
        if not image_repo_path:
            image_repo_path = DEFAULT_IMAGE_REPOSITORY_NAME

        image_repo_path_splits = image_repo_path.split("/")
        # Last part of image_repo_path should be repository name
        image_repo_name = image_repo_path_splits[-1]
        # Extract db and schema from the image_repo_path if possible
        if len(image_repo_path_splits) >= 3:
            db = image_repo_path_splits[-3]
            schema = image_repo_path_splits[-2]

        # Create image repository.
        # This checks if repo already exists and creates one if doesn't exist
        snowflake_repo_path = components.create_image_repository_if_not_exists(
            repo_name=image_repo_name, db=db, schema=schema
        )
        snowflake_repo_url = f"{snowflake_repo_path}/{image_name_with_tag}"

        components.push_docker_image(image_name_with_tag, snowflake_repo_url)

        components.deploy(
            service_name=service_name or "prediction_service",
            compute_pool_name=compute_pool_name or f"COMPUTE_POOL_{model}",
            warehouse_name=f"{model}_WAREHOUSE",
            image_path=snowflake_repo_url,
            udf_name="prediction_udf",
            connection_name=connection_name,
        )

        logger.info(
            """\nPlease check the service status using snowflake command service-status.
                    To use the prediction function, a sample query below: 
                    SELECT prediction_udf('John Doe's left arm was prepped and draped')
                    """
        )
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


@snowflake.command()
@click.option(
    "--service-name",
    default="prediction_service",
    help="Service name (default: 'prediction_service')",
)
@connection_options
def service_status(service_name, connection_name):
    components.get_service_status(
        service_name=service_name,
        connection_name=connection_name,
    )


@snowflake.command()
@click.option(
    "--service-name",
    default="prediction_service",
    help="Service name (default: 'prediction_service')",
)
@click.option(
    "--drop_compute_pool",
    is_flag=True,
    default=False,
    help="Flag to drop compute pool. By default, compute pool is suspended",
)
@connection_options
def stop_services(
    service_name,
    drop_compute_pool,
    connection_name,
):
    components.stop_all(
        service_name=service_name,
        drop_compute_pool=drop_compute_pool,
        connection_name=connection_name,
    )
