from endpoints import container
import endpoints
from .components import *


def generate_docker_files(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Snowflake.
    """

    return container.generate_docker_files(
        model=model,
        platform=endpoints.Platform.SNOWFLAKE,
        store_model=True,
        **kwargs,
    )
