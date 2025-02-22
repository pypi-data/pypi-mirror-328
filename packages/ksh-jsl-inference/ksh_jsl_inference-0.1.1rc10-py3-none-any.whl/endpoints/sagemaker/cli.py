import click
import json
from typing import Optional

from endpoints.cli import internals
from endpoints.cli.options import common_options


from endpoints import Platform, Recipe


@click.group()
def sagemaker():
    """
    Group of commands related to SageMaker functionality.

    """
    pass


@sagemaker.command()
@common_options
@click.option(
    "--output-dir",
    help="Output directory for the Docker files. If not provided, a default directory will be used.",
)
def generate_docker_files(model: str, **kwargs):
    """
    Generates Docker files for the specified model in a SageMaker-compatible format.
    """

    output_dir = internals._generate_docker_files(
        model=model, platform=Platform.SAGEMAKER, **kwargs
    )


@sagemaker.command()
@common_options
@click.option(
    "--image-name",
    default=None,
    help="Name of the Docker image to build. Defaults to the model name if not provided.",
)
@click.option(
    "--license-path",
    required=False,
    help="Path to the license file required to build the Docker image. By default, uses licenses set in the JSL_HOME.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable Docker cache during build.",
)
@click.option(
    "--image-tag",
    default="latest",
    show_default=True,
    help="Tag for the built Docker image (default: latest).",
)
def build_docker_image(model: str, **kwargs):
    """
    Builds a Docker image for  Sagemaker with the specified model.

    :raises click.ClickException: If the Docker image build fails.
    """
    internals.build_docker_image(model, platform=Platform.SAGEMAKER, **kwargs)


@sagemaker.command()
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
    """Run a local instance of the Sagemaker Inference container."""
    internals.run_local(
        model=model,
        language=language,
        platform=Platform.SAGEMAKER,
        inference_model=inference_model,
        recipe=Recipe(recipe),
        port=port,
    )


@sagemaker.command()
@common_options
@click.option(
    "--model-name",
    required=False,
    help="The name of the new SageMaker model. This name must be unique within your AWS account.",
)
@click.option(
    "--endpoint-name",
    required=False,
    help="The name of the endpoint. The name must be unique within an AWS Region in your AWS account.",
)
@click.option(
    "--variant-name",
    required=False,
    default="AllTraffic",
    help="The name of the production variant.",
)
@click.option(
    "--initial-instance-count",
    type=int,
    required=False,
    default=1,
    help="The number of instances to launch initially.",
)
@click.option(
    "--instance-type",
    required=False,
    default="ml.m4.xlarge",
    help="The ML compute instance type (e.g., ml.m5.large). Defaults to 'ml.m4.xlarge'.",
)
@click.option(
    "--execution-role-arn",
    required=False,
    help="The Amazon Resource Name (ARN) of the IAM role that SageMaker can assume to perform actions on your behalf. Defaults to the current user role.",
)
@click.option(
    "--enable-network-isolation",
    type=click.BOOL,
    default=False,
    help="If set to True, isolates the model container. No inbound or outbound network calls can be made to or from the model container.",
)
@click.option(
    "--ecr-repo-name",
    required=False,
    default="jsl-inference",
    help="The name of the ECR repository to push the Docker image to. Defaults to 'jsl-inference'.",
)
@click.option(
    "--s3-bucket-name",
    required=False,
    help="The name of the S3 bucket to upload model artifacts to. If not provided, one will be created automatically.",
)
@click.option(
    "--s3-key",
    required=False,
    help="The S3 key (path) where the model artifacts will be stored.",
)
@click.option(
    "--model-artifacts-path",
    required=False,
    help="Path to the model artifacts file (e.g., model.tar.gz) to upload to S3.",
)
@click.option(
    "--image-name",
    required=False,
    default=None,
    help="Name of the Docker image to build. Defaults to the model name if not provided.",
)
@click.option(
    "--image-tag",
    required=False,
    default=None,
    help="Tag for the Docker image (used for both the local image and the ECR image). Defaults to the model name if not provided.",
)
@click.option(
    "--license-path",
    required=False,
    help="Path to the license file required to build the Docker image. By default, uses licenses set in the JSL_HOME.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable Docker cache during build.",
)
@click.option(
    "--environment",
    required=False,
    default=None,
    help="Environment variables to set in the Docker container as a JSON string.",
)
def deploy(
    model: str,
    johnsnowlabs_version: str,
    no_license: bool,
    language: str,
    inference_model: str,
    legacy: bool,
    recipe: str,
    image_name: Optional[str],
    model_name: str,
    endpoint_name: str,
    variant_name: str,
    initial_instance_count: int,
    instance_type: str,
    execution_role_arn: Optional[str],
    enable_network_isolation: bool,
    ecr_repo_name: Optional[str],
    s3_bucket_name: Optional[str],
    s3_key: Optional[str],
    model_artifacts_path: Optional[str],
    license_path: str,
    no_cache: bool,
    environment: Optional[str],
    image_tag: Optional[str],
    **kwargs,
):
    """
    Deploys a SageMaker endpoint with the specified JSL model.
    """
    from endpoints.utils import logger
    from endpoints.sagemaker.client import SageMakerClient
    from endpoints.sagemaker.utils import (
        push_image_to_ecr,
        upload_and_get_model_data_url,
        create_default_s3_bucket,
        format_for_sagemaker,
        get_sagemaker_execution_role,
        ensure_ecr_repo_exists,
        login_to_ecr,
    )
    from endpoints.container.utils import (
        validate_docker_image_name,
        validate_image_tag,
        format_docker_image_name,
        format_image_tag,
    )

    sm_client = SageMakerClient()
    login_to_ecr()
    ensure_ecr_repo_exists(ecr_repo_name)

    endpoint_name = endpoint_name or format_for_sagemaker(model)
    model_name = model_name or format_for_sagemaker(model)

    if not image_name:
        image_name = format_docker_image_name(model)
    elif not validate_docker_image_name(image_name):
        raise ValueError(f"Invalid Docker image name: {image_name}")

    if not image_tag:
        image_tag = format_image_tag(model)
    elif not validate_image_tag(image_tag):
        raise ValueError(f"Invalid Docker image tag: {image_tag}")

    execution_role_arn = execution_role_arn or get_sagemaker_execution_role()
    s3_bucket_name = s3_bucket_name or create_default_s3_bucket()

    @sm_client.handle_aws_exceptions
    def _deploy():
        internals.build_docker_image(
            model,
            johnsnowlabs_version=johnsnowlabs_version,
            language=language,
            platform=Platform.SAGEMAKER,
            no_license=no_license,
            recipe=recipe,
            legacy=legacy,
            inference_model=inference_model,
            no_cache=no_cache,
            license_path=license_path,
            image_name=image_name,
            image_tag=image_tag,
        )

        ecr_image_uri = push_image_to_ecr(
            local_image=f"{image_name}:{image_tag}",
            target_repo=ecr_repo_name,
            image_tag=image_tag,
        )

        model_data_url = upload_and_get_model_data_url(
            model_artifacts_path=model_artifacts_path,
            s3_bucket_name=s3_bucket_name,
            s3_key=s3_key,
            model=model,
            recipe=Recipe(recipe),
            language=language,
        )

        logger.info(f"Model data URL: {model_data_url}")

        primary_container = {
            "Image": ecr_image_uri,
            "ModelDataUrl": model_data_url,
        }
        if environment:
            primary_container["Environment"] = json.loads(environment)

        sm_client.create_model(
            model_name=model_name,
            primary_container=primary_container,
            execution_role_arn=execution_role_arn,
            enable_network_isolation=enable_network_isolation,
        )
        logger.info(f"SageMaker model '{model_name}' created successfully!")

        production_variants = [
            {
                "VariantName": variant_name,
                "ModelName": model_name,
                "InitialInstanceCount": initial_instance_count,
                "InstanceType": instance_type,
            }
        ]
        sm_client.create_endpoint_config(
            endpoint_config_name=endpoint_name,
            production_variants=production_variants,
            enable_network_isolation=enable_network_isolation,
        )
        logger.info(
            f"SageMaker endpoint configuration '{endpoint_name}' created successfully!"
        )

        sm_client.create_endpoint(
            endpoint_name=endpoint_name,
            endpoint_config_name=endpoint_name,
        )
        logger.info(f"SageMaker endpoint '{endpoint_name}' created successfully!")

    return _deploy()


# To Do:
# https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html#realtime-endpoints-delete-model
# https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html#realtime-endpoints-delete-endpoint-config
# https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html#realtime-endpoints-delete-endpoint
