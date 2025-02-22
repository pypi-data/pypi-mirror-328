import endpoints
from endpoints import container
from .utils import *


def generate_docker_files(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Sagemaker.
    """

    return container.generate_docker_files(
        model,
        platform=endpoints.Platform.SAGEMAKER,
        store_model=False,
        **kwargs,
    )
