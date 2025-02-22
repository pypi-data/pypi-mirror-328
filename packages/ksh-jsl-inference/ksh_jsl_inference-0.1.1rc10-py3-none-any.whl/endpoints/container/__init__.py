"""
Module for serving inference model to Docker Container
"""

from .utils import generate_docker_files, build_docker_image

from endpoints.settings import TARGET_PLATFORM
from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.server import serve
from .setup import setup_container_env


# Default entrypoint for the Docker containers
def _init(command, inference_model: BaseInferenceModel):
    # For Sagemaker, serve and train are the possible commands
    if command == "serve":
        serve(
            platform=TARGET_PLATFORM,
            inference_model=inference_model,
        )
    else:
        raise NotImplementedError("Command not implemented")


__all__ = [
    "build_docker_image",
    "generate_docker_files",
    "setup_container_env",
]
