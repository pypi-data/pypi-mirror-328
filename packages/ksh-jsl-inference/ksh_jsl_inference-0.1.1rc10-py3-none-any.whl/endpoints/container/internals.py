from typing import Union, Optional
from uuid import uuid4

from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints import Platform, Recipe
from endpoints.settings import DEFAULT_JOHNSNOWLABS_VERSION
import dataclasses


@dataclasses.dataclass
class CommonParams:
    model: str
    johnsnowlabs_version: str = DEFAULT_JOHNSNOWLABS_VERSION
    no_license: bool = False
    store_model: bool = False
    language: str = "en"
    inference_model: Optional[Union[str, BaseInferenceModel]] = None
    legacy: bool = False
    platform: Platform = Platform.SAGEMAKER
    recipe: Recipe = Recipe.HEALTHCARE_NLP


@dataclasses.dataclass(init=False)
class GenerateDockerFilesRequest(CommonParams):
    output_dir: str = f"/tmp/{uuid4()}"

    def __init__(self, **kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)


@dataclasses.dataclass
class BuildDockerImageRequest(CommonParams):
    image_name: Optional[str] = None
    no_cache: bool = False
    license_path: Optional[str] = None
    image_tag: str = "latest"

