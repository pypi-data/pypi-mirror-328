from typing import Dict, List, Type, Any


MODEL_LOCATION = "/opt/ml/model"
DEFAULT_INPUT_KEYS = ["text", "input_text", "texts", "input_texts"]


class SchemaValidationError(Exception):
    """Exception for schema validation errors"""

    pass


class Schema:
    """Schema class for defining the schema of the input and output data"""

    def __init__(
        self,
        field: str,
        typing: Type,
        default: Any = None,
        required: bool = False,
        dtypes: List[str] = [],
    ):
        """
        Constructor for Schema

        :param str field: The field name
        :param Type typing: The type of the field
        :param Any default: The default value of the field
        :param bool required: Whether the field is required
        :param List[str] dtypes: A list of valid values for the field
        """
        self._field = field
        self._required = required
        self._typing = typing
        self._dtypes = dtypes
        self._default = default

    def validate(self, data: Dict):
        """
        Validates the schema of the data

        :param Dict data: The data to be validated

        :raises SchemaValidationError: If the schema is invalid
        """
        if self._required and self._field not in data:
            raise SchemaValidationError(f"Key {self._field} is missing in the data")
        value = data.get(self._field, self._default)
        if self._dtypes:
            if value not in self._dtypes:
                raise SchemaValidationError(
                    f"Key {self._field} must be of type {self._dtypes}"
                )
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, self._typing):
                    raise SchemaValidationError(
                        f"Key {self._field} must be of type {self._typing}"
                    )
        elif not isinstance(value, self._typing):
            raise SchemaValidationError(f"Key {value} must be of type {self._typing}")
        return value


class SchemaCollection:
    """A collection of schemas for validating multiple fields"""

    def __init__(self, schemas: List[Schema]):
        """
        Constructor for SchemaCollection

        :param List[Schema] schemas: A list of schemas
        """
        self._schemas = schemas

    def validate(self, data: Dict):
        """
        Validates the schema of the data

        :param Dict data: The data to be validated
        """
        return {schema._field: schema.validate(data) for schema in self._schemas}
