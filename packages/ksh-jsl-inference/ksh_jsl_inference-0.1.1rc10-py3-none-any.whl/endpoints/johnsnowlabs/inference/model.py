from typing import Dict, List, Union

from abc import ABC, abstractmethod
from endpoints.utils import append_string_or_list_of_string
from .schema import Schema, SchemaCollection

DEFAULT_INPUT_KEYS = ["text", "input_text", "texts", "input_texts"]


class BaseInferenceModel(ABC):
    """Base class for all inference models"""

    def __init__(self, input: Schema, input_params: SchemaCollection, output: Schema):
        """Constructor for BaseInferenceModel

        :param Schema input: The input schema
        :param SchemaCollection input_params: The input parameters schema
        :param Schema output: The output schema
        """
        self._input = input
        assert (
            input._field in DEFAULT_INPUT_KEYS
        ), f"Input schema must contain one of the following keys: {DEFAULT_INPUT_KEYS}"

        self._input_params = input_params
        self._output = output

    def _validate_input(self, input_data: Union[Dict, List[Dict]]) -> Dict:
        inputs = []
        params = []

        def _validate_common_input(input: Dict):
            validated_input = self._input.validate(input)
            validated_input_params = self._input_params.validate(input)

            append_string_or_list_of_string(validated_input, inputs)

            # Append the same params for each input
            for input in inputs:
                params.append(validated_input_params)

        if isinstance(input_data, dict):
            _validate_common_input(input_data)

        if isinstance(input_data, list):
            for item in input_data:
                _validate_common_input(item)
            if not inputs:
                raise ValueError(
                    f"Input data must contain one of the following keys: {DEFAULT_INPUT_KEYS}"
                )

        return {"inputs": inputs, "params": params}

    def predict(self, input_data: Union[Dict, List[Dict]]) -> Dict:
        """
        Validates the schema, perform prediction and returns the output

        :param Union[Dict, List[Dict]] input_data: The input data to be predicted

        :return: The output of the prediction
        """
        validated_data = self._validate_input(input_data)
        predictions = self.concrete_predict(validated_data)
        return {self._output._field: self._output.validate(predictions)}

    @abstractmethod
    def concrete_predict(self, input_data: Dict) -> Dict:
        """
        Factory method for concrete prediction logic. All subclasses should implement this method.

        :param Dict input_data: The input data to be predicted by the model. The input data contains "inputs" and "params" keys. The "inputs" key contains the input data to be predicted and the "params" key contains the input parameters.

        :return: The output of the prediction
        """
        pass

    @abstractmethod
    def get_python_requirements(self) -> List[str]:
        """
        Returns a list of python packages that are required for the model to run.
        """
        pass

    @abstractmethod
    def dispose(self):
        """Dispose of the model and release any resources"""
        pass
