from typing import Dict, List

from endpoints.johnsnowlabs.encoder import AnnotationEncoder
from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.johnsnowlabs.inference.schema import Schema, SchemaCollection
from endpoints.log_utils import logger
import json

from pyspark.sql.dataframe import DataFrame


class MedicalNlpInferenceModel(BaseInferenceModel):
    """Base class for all Medical NLP models"""

    def __init__(self):
        """
        Constructor for MedicalNlpInferenceModel
        """
        super().__init__(
            input=Schema(field="text", typing=str, required=True),
            input_params=SchemaCollection([]),
            output=Schema(field="predictions", typing=Dict),
        )
        self._spark = None
        self._light_pipeline = None

    def get_python_requirements(self) -> List[str]:
        return ["johnsnowlabs>=5.4.0"]

    @property
    def spark(self):
        if not self._spark:
            from endpoints.johnsnowlabs.model_loader import spark, light_pipeline

            self._spark = spark
            self._light_pipeline = light_pipeline
        return self._spark

    @property
    def light_pipeline(self):
        if not self._light_pipeline:
            from endpoints.johnsnowlabs.model_loader import spark, light_pipeline

            self._spark = spark
            self._light_pipeline = light_pipeline
        return self._light_pipeline

    def _prepare_data(self, texts: List[str]) -> DataFrame:
        logger.debug("Preparing the Spark DataFrame")
        indexed_text = [(i, t) for i, t in enumerate(texts)]
        df = self.spark.createDataFrame(indexed_text, ["index", "text"])
        return df.repartition(1000)

    def process_light_pipeline_results(
        self, inputs: List[str], results: List, params: Dict
    ):
        """
        Processes the results from the Light Pipeline. Subclasses can override this method to customize the output.

        :param List[str] inputs: The input texts
        :param List results: The results from the Light Pipeline
        :param Dict params: Additional input params
        """
        data = json.dumps(results, cls=AnnotationEncoder)
        return json.loads(data)

    def process_pretrained_pipeline_results(
        self, inputs: List[str], results: DataFrame, params: Dict
    ):
        """
        Processes the results from the Pretrained Pipeline. Subclasses can override this method to customize the output.

        :param List[str] inputs: The input texts
        :param DataFrame results: The results from the Pretrained Pipeline
        :param Dict params: Additional input params
        """
        json_result = results.toJSON().collect()
        return list(map(json.loads, json_result))

    def _get_predictions_from_light_pipeline(self, texts: List[str], params: Dict):
        logger.debug(f"Processing {len(texts)} texts with Light Pipeline")
        results = self.light_pipeline.fullAnnotate(texts)
        return self.process_light_pipeline_results(texts, results, params)

    def _get_predictions_from_pretrained_pipeline(self, texts: List[str], params: Dict):
        logger.debug(f"Processing {len(texts)} texts with Pretrained Pipeline")
        input_df = self._prepare_data(texts)
        predictions_df = self.light_pipeline.transform(input_df).cache()
        sorted_df = predictions_df.orderBy("index")
        logger.debug("Transformation complete, extracting results")
        return self.process_pretrained_pipeline_results(texts, sorted_df, params)

    def concrete_predict(self, input_data: Dict) -> Dict:
        """
        Perform the model prediction either using the pretrained pipeline or the light pipeline.

        :param Dict input_data: The input data to be predicted by the model
        :return: The output of the prediction
        """

        inputs = input_data["inputs"]
        params = input_data["params"]

        if isinstance(inputs, list) and len(inputs) >= 20:
            predictions = self._get_predictions_from_pretrained_pipeline(inputs, params)
        else:
            predictions = self._get_predictions_from_light_pipeline(inputs, params)

        return {self._output._field: predictions}

    def dispose(self):
        """
        Dispose the model resources. Close the spark session.
        """
        self.spark.sparkContext.stop()
