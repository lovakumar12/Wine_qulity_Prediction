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
    


### next check the data transformation pipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline  
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


### next check the model trainer pipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
STAGE_NAME = "Model Trainer stage"
try:    
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")  
    
except Exception as e:
    logger.exception(e)
    raise e


#### next check the model evaluation pipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e