from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation stage"
from mlProject import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f"{STAGE_NAME} started")
        logger.info("Stage: Data Transformation")
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e