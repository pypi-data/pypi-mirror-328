import json
from endpoints.log_utils import logger
from endpoints.sagemaker.utils import get_aws_client
from typing import Optional, Dict, List


class SageMakerClient:
    def __init__(self):
        """
        Initialize the SageMaker client.
        """
        self.client = get_aws_client("sagemaker")

    def handle_aws_exceptions(self, func):
        """
        Decorator to handle common AWS-related exceptions.
        """

        def wrapper(*args, **kwargs):
            from botocore.exceptions import (
                NoCredentialsError,
                PartialCredentialsError,
                ClientError,
            )

            try:
                return func(*args, **kwargs)
            except NoCredentialsError:
                logger.error(
                    "Credentials not found. Please configure your AWS credentials."
                )
                raise Exception("AWS credentials error.")
            except PartialCredentialsError:
                logger.error(
                    "Incomplete credentials provided. Please check your AWS credentials."
                )
                raise Exception("AWS credentials error.")
            except ClientError as e:
                logger.error(f"AWS Client Error: {e.response['Error']['Message']}")
                raise Exception("AWS client error.")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON format for one of the parameters: {str(e)}")
                raise Exception("JSON parsing error.")
            except Exception as e:
                logger.error(f"An error occurred: {str(e)}")
                raise Exception("An unexpected error occurred.")

        return wrapper

    def create_model(
        self,
        model_name: str,
        primary_container: Dict,
        execution_role_arn: str,
        containers: Optional[List[Dict]] = None,
        inference_execution_config: Optional[Dict] = None,
        tags: Optional[List[Dict]] = None,
        vpc_config: Optional[Dict] = None,
        enable_network_isolation: bool = False,
    ):
        """
        Creates a SageMaker model.
        """
        request_params = {
            "ModelName": model_name,
            "PrimaryContainer": primary_container,
            "ExecutionRoleArn": execution_role_arn,
            "EnableNetworkIsolation": enable_network_isolation,
        }

        if containers:
            request_params["Containers"] = containers
        if inference_execution_config:
            request_params["InferenceExecutionConfig"] = inference_execution_config
        if tags:
            request_params["Tags"] = tags
        if vpc_config:
            request_params["VpcConfig"] = vpc_config

        return self.client.create_model(**request_params)

    def create_endpoint_config(
        self,
        endpoint_config_name: str,
        production_variants: List[Dict],
        enable_network_isolation: bool = False,
        data_capture_config: Optional[Dict] = None,
        tags: Optional[List[Dict]] = None,
        kms_key_id: Optional[str] = None,
        async_inference_config: Optional[Dict] = None,
        explainer_config: Optional[Dict] = None,
        shadow_production_variants: Optional[List[Dict]] = None,
        execution_role_arn: Optional[str] = None,
        vpc_config: Optional[Dict] = None,
    ):
        """
        Creates an endpoint configuration in SageMaker.
        """
        request_params = {
            "EndpointConfigName": endpoint_config_name,
            "ProductionVariants": production_variants,
            "EnableNetworkIsolation": enable_network_isolation,
        }

        if data_capture_config:
            request_params["DataCaptureConfig"] = data_capture_config
        if tags:
            request_params["Tags"] = tags
        if kms_key_id:
            request_params["KmsKeyId"] = kms_key_id
        if async_inference_config:
            request_params["AsyncInferenceConfig"] = async_inference_config
        if explainer_config:
            request_params["ExplainerConfig"] = explainer_config
        if shadow_production_variants:
            request_params["ShadowProductionVariants"] = shadow_production_variants
        if execution_role_arn:
            request_params["ExecutionRoleArn"] = execution_role_arn
        if vpc_config:
            request_params["VpcConfig"] = vpc_config

        return self.client.create_endpoint_config(**request_params)

    def create_endpoint(
        self,
        endpoint_name: str,
        endpoint_config_name: str,
        deployment_config: Optional[Dict] = None,
        tags: Optional[List[Dict]] = None,
    ):
        """
        Creates a SageMaker endpoint.
        """
        request_params = {
            "EndpointName": endpoint_name,
            "EndpointConfigName": endpoint_config_name,
        }

        if deployment_config:
            request_params["DeploymentConfig"] = deployment_config
        if tags:
            request_params["Tags"] = tags

        return self.client.create_endpoint(**request_params)
