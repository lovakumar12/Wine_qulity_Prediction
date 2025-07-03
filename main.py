from mlProject import logger

#logger.info("Logging has been set up successfully.") ## first check

## next check the data ingestion pipeline
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


## next check the data validation pipelinefrom mlProject.config.configuration import ConfigurationManager
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject import logger


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
    


