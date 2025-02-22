import os
import shutil
from johnsnowlabs import nlp
from sparknlp.pretrained import PretrainedPipeline
from endpoints.settings import MODEL_LOCATION
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp_jsl.annotator import *
from endpoints.log_utils import logger
from endpoints.utils import ProgressPercentage


def download_healthcare_model(
    model_ref: str,
    language: str = "en",
    output_dir: str = MODEL_LOCATION,
):
    """
    Downloads the specified healthcare model from John Snow Labs and stores it in the specified location.
    :param str model_ref: The model to download
    :param str language: The language of the model. Default: 'en'
    :param str output_dir: The directory where the model will be saved. Default is MODEL_LOCATION.
    """
    try:
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir, ignore_errors=True)

        os.makedirs(output_dir, exist_ok=True)

        spark = nlp.start()
        spark.sparkContext.setLogLevel("ERROR")

        if model_ref:
            pretrained_pipeline = PretrainedPipeline(
                model_ref, language, "clinical/models"
            )
            pretrained_pipeline.model.write().overwrite().save(output_dir)
            return output_dir
        else:
            raise ValueError(
                "No model reference provided. Please specify a valid model."
            )

    except PermissionError as e:
        raise PermissionError(
            f"Permission error: {e}. Please ensure you have read/write access to {output_dir}."
        )
    except Exception as e:
        raise RuntimeError(f"Failed to download and save the healthcare model: {e}")


vdb_ner_models = {
    "icd10cm": {
        "ner_clinical": ["PROBLEM"],
        "ner_jsl": [
            "CEREBROVASCULAR_DISEASE",
            "COMMUNICABLE_DISEASE",
            "DIABETES",
            "DISEASE_SYNDROME_DISORDER",
            "EKG_FINDINGS",
            "HEART_DISEASE",
            "HYPERLIPIDEMIA",
            "HYPERTENSION",
            "IMAGINGFINDINGS",
            "INJURY_OR_POISONING",
            "KIDNEY_DISEASE",
            "OBESITY",
            "ONCOLOGICAL",
            "OVERWEIGHT",
            "PREGNANCY",
            "PSYCHOLOGICAL_CONDITION",
            "SYMPTOM",
            "VS_FINDING",
        ],
    },
    "mesh": {"ner_clinical": []},
    "atc": {"ner_posology": ["DRUG"]},
    "cpt": {
        "ner_jsl": ["PROCEDURE"],
        "ner_measurements_clinical": ["MEASUREMENTS"],
    },
    "hcc": {
        "ner_clinical": ["PROBLEM"],
        "ner_jsl": [
            "CEREBROVASCULAR_DISEASE",
            "COMMUNICABLE_DISEASE",
            "DIABETES",
            "DISEASE_SYNDROME_DISORDER",
            "EKG_FINDINGS",
            "HEART_DISEASE",
            "HYPERLIPIDEMIA",
            "HYPERTENSION",
            "IMAGINGFINDINGS",
            "INJURY_OR_POISONING",
            "KIDNEY_DISEASE",
            "OBESITY",
            "ONCOLOGICAL",
            "OVERWEIGHT",
            "PREGNANCY",
            "PSYCHOLOGICAL_CONDITION",
            "SYMPTOM",
            "VS_FINDING",
        ],
    },
    "ndc": {"ner_posology_greedy": ["DRUG"]},
    "ncit": {
        "ner_oncology": [
            "ADENOPATHY",
            "BIOMARKER",
            "BIOMARKER_RESULT",
            "CANCER_DX",
            "CANCER_SCORE",
            "CANCER_SURGERY",
            "CHEMOTHERAPY",
            "CYCLE_COUNT",
            "CYCLE_DAY",
            "CYCLE_NUMBER",
            "DIRECTION",
            "DURATION",
            "FREQUENCY",
            "GRADE",
            "HISTOLOGICAL_TYPE",
            "HORMONAL_THERAPY",
            "IMAGING_TEST",
            "IMMUNOTHERAPY",
            "INVASION",
            "LINE_OF_THERAPY",
            "METASTASIS",
            "ONCOGENE",
            "PATHOLOGY_RESULT",
            "PATHOLOGY_TEST",
            "PERFORMANCE_STATUS",
            "RADIATION_DOSE",
            "RADIOTHERAPY",
            "RESPONSE_TO_TREATMENT",
            "ROUTE",
            "SITE_BONE",
            "SITE_BRAIN",
            "SITE_BREAST",
            "SITE_LIVER",
            "SITE_LUNG",
            "SITE_LYMPH_NODE",
            "SITE_OTHER_BODY_PART",
            "STAGING",
            "TARGETED_THERAPY",
            "TUMOR_FINDING",
            "UNSPECIFIC_THERAPY",
        ]
    },
    "hcpcs": {"ner_jsl": ["PROCEDURE"], "ner_clinical": ["TREATMENT"]},
    "hgnc": {"ner_human_phenotype_gene_clinical": ["GENE"]},
    "meddra_llt": {
        "ner_jsl": [
            "PROCEDURE",
            "KIDNEY_DISEASE",
            "CEREBROVASCULAR_DISEASE",
            "HEART_DISEASE",
            "DISEASE_SYNDROME_DISORDER",
            "IMAGINGFINDINGS",
            "SYMPTOM",
            "VS_FINDING",
            "EKG_FINDINGS",
            "COMMUNICABLE_DISEASE",
            "SUBSTANCE",
            "INTERNAL_ORGAN_OR_COMPONENT",
            "EXTERNAL_BODY_PART_OR_REGION",
            "MODIFIER",
            "TRIGLYCERIDES",
            "ALCOHOL",
            "SMOKING",
            "PREGNANCY",
            "HYPERTENSION",
            "OBESITY",
            "INJURY_OR_POISONING",
            "TEST",
            "HYPERLIPIDEMIA",
            "BMI",
            "ONCOLOGICAL",
            "PSYCHOLOGICAL_CONDITION",
            "LDL",
            "DIABETES",
        ],
        "ner_clinical_large": ["PROBLEM"],
    },
    "meddra_pt": {
        "ner_jsl": [
            "PROCEDURE",
            "KIDNEY_DISEASE",
            "CEREBROVASCULAR_DISEASE",
            "HEART_DISEASE",
            "DISEASE_SYNDROME_DISORDER",
            "IMAGINGFINDINGS",
            "SYMPTOM",
            "VS_FINDING",
            "EKG_FINDINGS",
            "COMMUNICABLE_DISEASE",
            "SUBSTANCE",
            "INTERNAL_ORGAN_OR_COMPONENT",
            "EXTERNAL_BODY_PART_OR_REGION",
            "MODIFIER",
            "TRIGLYCERIDES",
            "ALCOHOL",
            "SMOKING",
            "PREGNANCY",
            "HYPERTENSION",
            "OBESITY",
            "INJURY_OR_POISONING",
            "TEST",
            "HYPERLIPIDEMIA",
            "BMI",
            "ONCOLOGICAL",
            "PSYCHOLOGICAL_CONDITION",
            "LDL",
            "DIABETES",
        ],
        "ner_clinical_large": ["PROBLEM"],
    },
    "rxnorm": {"ner_posology_greedy": ["DRUG"], "ner_jsl_greedy": ["DRUG"]},
    "icd10pcs": {"ner_clinical": ["TREATMENT"], "ner_jsl": ["PROCEDURE"]},
    "icdo": {
        "ner_oncology": [
            "CANCER_DX",
            "HISTOLOGICAL_TYPE",
            "METASTASIS",
            "TUMOR_FINDING",
        ],
        "ner_jsl": ["ONCOLOGICAL"],
    },
    "loinc": {"ner_jsl": ["TEST"], "ner_clinical": ["TEST"]},
    "snomed": {
        "ner_jsl": [
            "PROCEDURE",
            "KIDNEY_DISEASE",
            "CEREBROVASCULAR_DISEASE",
            "HEART_DISEASE",
            "DISEASE_SYNDROME_DISORDER",
            "IMAGINGFINDINGS",
            "SYMPTOM",
            "VS_FINDING",
            "EKG_FINDINGS",
            "COMMUNICABLE_DISEASE",
            "SUBSTANCE",
            "DRUG_INGREDIENT",
            "INTERNAL_ORGAN_OR_COMPONENT",
            "EXTERNAL_BODY_PART_OR_REGION",
            "MODIFIER",
            "TRIGLYCERIDES",
            "ALCOHOL",
            "SMOKING",
            "PREGNANCY",
            "HYPERTENSION",
            "OBESITY",
            "INJURY_OR_POISONING",
            "TEST",
            "HYPERLIPIDEMIA",
            "BMI",
            "ONCOLOGICAL",
            "PSYCHOLOGICAL_CONDITION",
            "LDL",
            "DIABETES",
            "HDL",
        ],
        "ner_snomed_term": ["SNOMED_TERM"],
        "ner_posology": ["DRUG"],
        "ner_clinical": ["PROBLEM", "TREATMENT"],
    },
}


def _get_ner_stages(concept):
    """
    Builds a pipeline of stages for Named Entity Recognition (NER) based on the given concept.

    Args:
        concept (str): The medical coding system or concept (e.g., "icd10cm", "mesh").

    Returns:
        list: A list of Spark NLP pipeline stages for NER.
    """
    # Get the NER models and whitelists for the specified concept
    ner_models = vdb_ner_models[concept]

    # Initialize lists to store pipeline stages and chunk column names
    merger_inputs = []  # Stores names of columns containing NER chunks to be merged
    ner_pipe = []  # Stores the individual stages of the NER pipeline

    # Iterate through the selected NER models and their whitelists
    for ner_model, whitelist in ner_models.items():
        logger.info("Model Name :", ner_model, "---", "White List:", whitelist)

        try:
            # Load a pre-trained MedicalNerModel
            tmp_model = (
                MedicalNerModel.pretrained(ner_model, "en", "clinical/models")
                .setInputCols(["sentence", "token", "word_embeddings"])
                .setOutputCol(ner_model)
                .setLabelCasing("upper")
            )
            ner_pipe.append(tmp_model)  # Add the NER model to the pipeline

            # Add NerConverterInternal to convert NER annotations into chunks
            if len(whitelist) == 0:
                # If no whitelist, use all entities
                ner_pipe.append(
                    NerConverterInternal()
                    .setInputCols(["sentence", "token", ner_model])
                    .setOutputCol(f"{ner_model}_chunk")
                )
            else:
                # If whitelist is provided, filter entities
                ner_pipe.append(
                    NerConverterInternal()
                    .setInputCols(["sentence", "token", ner_model])
                    .setOutputCol(f"{ner_model}_chunk")
                    .setWhiteList(whitelist)
                )

            # Add the chunk column name to the list for merging
            merger_inputs.append(f"{ner_model}_chunk")

        except Exception as e:
            logger.error(e)

    # Create a ChunkMergeApproach to combine chunks from different NER models
    chunk_merger = (
        ChunkMergeApproach()
        .setInputCols(merger_inputs)
        .setOutputCol("ner_chunk")
        .setMergeOverlapping(True)
    )
    ner_pipe.append(chunk_merger)  # Add the chunk merger to the pipeline

    # Return the assembled NER pipeline stages
    return ner_pipe


def get_ner_model(concept, spark):
    """
    Creates and returns a Spark NLP pipeline model for Named Entity Recognition (NER).

    Args:
        concept (str): The medical coding system or concept (e.g., "icd10cm", "mesh").

    Returns:
        PipelineModel: A fitted Spark NLP pipeline model for NER.
    """

    # 1. Document Assembler: Converts raw text into Spark NLP Documents
    documentAssembler = DocumentAssembler().setInputCol("text").setOutputCol("document")

    # 2. Sentence Detector: Splits documents into sentences
    sentenceDetector = (
        SentenceDetectorDLModel.pretrained(
            "sentence_detector_dl_healthcare", "en", "clinical/models"
        )
        .setInputCols(["document"])
        .setOutputCol("sentence")
    )

    # 3. Tokenizer: Splits sentences into individual tokens (words)
    tokenizer = Tokenizer().setInputCols("sentence").setOutputCol("token")

    # 4. Word Embeddings: Generates word embeddings for each token
    word_embeddings = (
        WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
        .setInputCols("sentence", "token")
        .setOutputCol("word_embeddings")
    )

    # 5. Get NER Stages: Dynamically builds NER stages based on the concept
    ner_stages = _get_ner_stages(concept)

    # 6. Create Pipeline: Combines all stages into a single pipeline
    pipeline = Pipeline(
        stages=[
            documentAssembler,
            sentenceDetector,
            tokenizer,
            word_embeddings,
            *ner_stages,
        ]
    )

    # 7. Fit Pipeline: Fits the pipeline to an empty DataFrame to initialize it
    empty_df = spark.createDataFrame([[""]]).toDF("text")  # Empty DataFrame for fitting
    logger.info("NER pipeline is ready...")
    model = pipeline.fit(empty_df)

    # 8. Return Model: Returns the fitted NER pipeline model
    return model


def download_vector_db(concept, output_dir=MODEL_LOCATION, region_name="us-west-2"):
    import boto3
    from botocore.client import Config

    BUCKET_NAME = "dev.johnsnowlabs.com"
    SOURCE_FILE = f"healthcare_team/resolvers_by_vectordb/{concept}_chroma_db/{concept}_chroma_db.zip"
    target_file = os.path.join(output_dir, f"{concept}_chroma_db.zip")
    extract_path = os.path.join(output_dir, "vector_db")

    os.makedirs(output_dir, exist_ok=True)
    s3 = boto3.client(
        "s3",
        region_name=region_name,
        config=Config(connect_timeout=60, read_timeout=70),
    )
    response = s3.head_object(Bucket=BUCKET_NAME, Key=SOURCE_FILE)
    total_size = response["ContentLength"]

    progress_tracker = ProgressPercentage(total_size)

    s3.download_file(
        BUCKET_NAME,
        SOURCE_FILE,
        target_file,
        Callback=progress_tracker.download_callback,
    )

    logger.info("\nDownload complete.")

    shutil.unpack_archive(target_file, extract_path)
    os.remove(target_file)


def download_chromadb_resolver_model(concept, output_dir=MODEL_LOCATION):
    """Downloads the NER model, embeddings, and VectorDB for the specified concept."""

    if concept not in vdb_ner_models:
        raise ValueError(
            f"Unsupported concept: '{concept}'. "
            f"Supported concepts are: {', '.join(sorted(vdb_ner_models.keys()))}"
        )

    try:
        shutil.rmtree(output_dir, ignore_errors=True)
        os.makedirs("/opt/ml/model", exist_ok=True)
    except PermissionError:
        raise PermissionError(
            "Please make sure you have read/write permissions to /opt/ml/"
        )
    # VectorDB
    download_vector_db(concept, output_dir)

    spark = nlp.start()
    spark.sparkContext.setLogLevel("ERROR")

    from sentence_transformers import SentenceTransformer

    # Download the model for the specified concept
    ner_model_path = os.path.join(output_dir, "ner_model")
    embeddings_path = os.path.join(output_dir, "embeddings")

    # NER model
    ner_model = get_ner_model(concept, spark)
    ner_model.write().overwrite().save(ner_model_path)

    # Embeddings model
    embeddings = SentenceTransformer("BAAI/bge-base-en-v1.5")
    embeddings.save_pretrained(embeddings_path)

    return output_dir
