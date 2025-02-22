import os
import re
import base64
import subprocess
from typing import Optional
from endpoints.log_utils import logger
from endpoints.utils import ProgressPercentage
from endpoints import Recipe


def get_aws_client(service_name: str):
    """
    Utility function to initialize and return an AWS service client.

    :param service_name: Name of the AWS service (e.g., 's3', 'ecr').
    :return: Boto3 client for the specified service.
    """
    import boto3

    return boto3.client(service_name)


def upload_model_to_s3(file_path: str, bucket_name: str, s3_key: str):
    """
    Uploads a model file to an S3 bucket.

    :param file_path: Path to the model file to upload.
    :param bucket_name: Name of the S3 bucket.
    :param s3_key: S3 key (path) where the file will be stored.
    """
    s3_client = get_aws_client("s3")
    try:
        file_size = os.path.getsize(file_path)
        progress_tracker = ProgressPercentage(file_size)

        with open(file_path, "rb") as f:
            s3_client.upload_fileobj(
                f,
                bucket_name,
                s3_key,
                Callback=progress_tracker.upload_callback,
            )

        logger.info(f"Model file {file_path} uploaded to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logger.error(f"Failed to upload model to S3: {str(e)}")
        raise


def push_image_to_ecr(local_image: str, target_repo: str, image_tag: str) -> str:
    """
    Pushes a Docker image to an ECR repository.

    :param local_image: Name of the local Docker image to push.
    :param target_repo: Name of the ECR repository.
    :param image_tag: Tag for the Docker image.
    :return: The full ECR image URI.
    """
    if not local_image or not target_repo or not image_tag:
        raise ValueError(
            "local_image, target_repo, and image_tag must be non-empty strings"
        )

    ecr_client = get_aws_client("ecr")

    try:
        auth_response = ecr_client.get_authorization_token()
        endpoint = auth_response["authorizationData"][0]["proxyEndpoint"]
        ecr_image_uri = f"{endpoint.replace('https://', '')}/{target_repo}:{image_tag}"
        subprocess.run(["docker", "tag", local_image, ecr_image_uri], check=True)

        logger.info(f"Pushing Docker image to ECR: {ecr_image_uri}")
        subprocess.run(["docker", "push", ecr_image_uri], check=True)
        logger.info(f"Successfully pushed Docker image to ECR: {ecr_image_uri}")

        return ecr_image_uri

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to push Docker image to ECR: {str(e)}")
        logger.error(f"Command error output: {e.stderr}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while pushing Docker image: {str(e)}")
        raise


def format_for_sagemaker(name: str) -> str:
    """
    Formats a string to comply with SageMaker's naming conventions.
    - Replaces invalid characters (anything other than alphanumeric or hyphens) with hyphens.
    - Ensures the name starts and ends with an alphanumeric character.
    - Truncates the name if it exceeds the maximum length (63 characters).
    """

    formatted_name = re.sub(r"[^a-zA-Z0-9-]+", "-", name)

    formatted_name = formatted_name.strip("-")

    return formatted_name[:63]


def create_default_s3_bucket() -> str:
    """
    Creates a default S3 bucket for storing model artifacts if not provided.
    The bucket name format is `jsl-inference-<account_id>-<region>`.

    :return: Name of the created or existing bucket.
    """
    s3_client = get_aws_client("s3")
    sts_client = get_aws_client("sts")

    account_id = sts_client.get_caller_identity()["Account"]
    region = s3_client.meta.region_name
    bucket_name = f"jsl-inference-{account_id}-{region}"

    try:
        s3_client.head_bucket(Bucket=bucket_name)
        logger.info(f"S3 bucket '{bucket_name}' already exists.")
    except s3_client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            try:
                if region == "us-east-1":
                    s3_client.create_bucket(Bucket=bucket_name)
                else:
                    s3_client.create_bucket(
                        Bucket=bucket_name,
                        CreateBucketConfiguration={"LocationConstraint": region},
                    )
                logger.info(f"Created S3 bucket: {bucket_name}")
            except Exception as e:
                logger.error(f"Error creating S3 bucket: {str(e)}")
                raise
        else:
            logger.error(f"Error checking S3 bucket: {str(e)}")
            raise

    return bucket_name


def get_sagemaker_execution_role() -> str:
    """
    Retrieves the execution role ARN from the current session.

    :return: The execution role ARN.
    :raises ValueError: If there's an error retrieving or parsing the role.
    """
    try:
        sts_client = get_aws_client("sts")
        identity_info = sts_client.get_caller_identity()
        sts_arn = identity_info["Arn"]
        role_name = sts_arn.split("/")[1]
        iam_client = get_aws_client("iam")
        role_response = iam_client.get_role(RoleName=role_name)
        return role_response["Role"]["Arn"]
    except Exception as e:
        raise ValueError(f"Error retrieving execution role: {e}")


def ensure_ecr_repo_exists(ecr_repo_name: str) -> None:
    """
    Ensures the ECR repository exists. If it doesn't exist, creates it.

    :param ecr_repo_name: Name of the ECR repository.
    """
    ecr_client = get_aws_client("ecr")
    try:
        ecr_client.create_repository(repositoryName=ecr_repo_name)
        logger.info(f"Repository '{ecr_repo_name}' created successfully.")
    except ecr_client.exceptions.RepositoryAlreadyExistsException:
        logger.info(f"Repository '{ecr_repo_name}' already exists. Proceeding...")
    except Exception as e:
        logger.error(f"Failed to create ECR repository: {str(e)}")
        raise


def create_model_tarball(
    model_dir: str, tarball_name: str = None, output_path: str = None
) -> str:
    """
    Creates a .tar.gz file from the contents of the model directory.

    If tarball_name is not provided, the base name of model_dir with '.tar.gz' is used.
    If output_path is a directory, tarball_name is appended to it.
    If output_path is None, the temporary directory is used.

    The tarball will include only the contents of model_dir, not the directory itself.

    Returns the full path to the created tarball.
    """
    import tempfile

    if tarball_name is None:
        tarball_name = f"{os.path.basename(model_dir)}.tar.gz"

    if output_path is None:
        base_tarballs_dir = os.path.join(
            tempfile.gettempdir(), "jsl_inference", "tarballs"
        )
        os.makedirs(base_tarballs_dir, exist_ok=True)
        full_tar_path = os.path.join(base_tarballs_dir, tarball_name)
    else:
        full_tar_path = os.path.join(output_path, tarball_name)

    cmd = f"tar -czf {full_tar_path} -C {model_dir} ."
    logger.info(f"Executing command: {cmd}")

    try:
        exit_code = os.system(cmd)
        if exit_code != 0:
            logger.error("Tar command failed with exit code: %s", exit_code)
            raise Exception("Tar command failed.")
    except Exception as e:
        logger.error(
            "An exception occurred during tarball creation: %s", e, exc_info=True
        )
        raise

    logger.info(f"Tarball created successfully at: {full_tar_path}")
    return full_tar_path


def upload_and_get_model_data_url(
    model_artifacts_path: Optional[str],
    s3_bucket_name: str,
    s3_key: Optional[str],
    model: str,
    recipe: Recipe.HEALTHCARE_NLP,
    language: str = "en",
) -> str:
    """
    Returns the model data URL based on the provided parameters.
    """
    from endpoints.model import download_model

    if model_artifacts_path and s3_key:
        upload_model_to_s3(model_artifacts_path, s3_bucket_name, s3_key)
        return f"s3://{s3_bucket_name}/{s3_key}"
    elif model_artifacts_path:
        upload_model_to_s3(model_artifacts_path, s3_bucket_name, f"{model}.tar.gz")
        return f"s3://{s3_bucket_name}/{model}.tar.gz"
    elif s3_bucket_name and s3_key:
        return f"s3://{s3_bucket_name}/{s3_key}"
    else:

        model_path = download_model(model=model, language=language, recipe=recipe)
        model_tar_file_path = create_model_tarball(model_path, f"{model}.tar.gz")
        upload_model_to_s3(model_tar_file_path, s3_bucket_name, f"{model}.tar.gz")
        return f"s3://{s3_bucket_name}/{model}.tar.gz"


def login_to_ecr() -> None:
    """
    Logs in to AWS ECR using the default AWS credentials.

    This method retrieves the ECR authorization token, decodes it to obtain
    the username and password, and then logs in to the registry using the Docker CLI.
    """

    ecr_client = get_aws_client("ecr")
    auth_response = ecr_client.get_authorization_token()
    auth_data = auth_response["authorizationData"][0]
    auth_token = auth_data["authorizationToken"]
    registry_endpoint = auth_data["proxyEndpoint"]

    username, password = base64.b64decode(auth_token).decode().split(":")

    cmd = [
        "docker",
        "login",
        "--username",
        username,
        "--password",
        password,
        registry_endpoint,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        error_msg = f"Docker login failed: {result.stderr}"
        logger.error(error_msg)
        raise Exception(error_msg)

    logger.info(
        f"Logged in to ECR registry '{registry_endpoint}'. Login response: {result.stdout}"
    )
