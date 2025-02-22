import click
from endpoints import Recipe


def common_options(f):
    """
    A decorator to add common CLI options for SageMaker commands, including:
    - Model argument (required).
    - John Snow Labs version.
    - Flags to store license and model in the Docker image.
    - Language specification for the model.
    """
    f = click.argument("model")(f)
    f = click.option(
        "--johnsnowlabs-version",
        default="5.5.0",
        help="Version of the John Snow Labs library (default: 5.5.0)",
    )(f)
    f = click.option(
        "--no-license",
        is_flag=True,
        default=False,
        show_default=True,
        help="Store the license in the Docker image (default: True)",
    )(f)
    f = click.option(
        "--language", default="en", help="Language of the model to load (default: 'en')"
    )(f)
    f = click.option(
        "--inference_model",
        required=False,
        default=None,
        help="""
        Inference model to use. Must be a subclass of BaseInference
        :ref:`See Example <custom_inference_model_usage>`. In legacy mode, this option is ignored.`

        """,
    )(f)
    f = click.option(
        "--legacy",
        is_flag=True,
        default=False,
        help="Use legacy version to build the Docker image (default: False)",
    )(f)

    f = click.option(
        "--recipe",
        required=False,
        type=click.Choice([recipe.value for recipe in Recipe], case_sensitive=False),
        default=Recipe.HEALTHCARE_NLP.value,
        help="Recipe to use. Valid values: "
        + ", ".join([recipe.value for recipe in Recipe]),
    )(f)

    return f
