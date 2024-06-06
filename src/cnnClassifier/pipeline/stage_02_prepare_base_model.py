from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare base model"

# it is just step of ruing one function
#initialize cinfigmanger from that call prepare base model
#initialize preparebase mdel and by this call get base model and update base mdeol
#model has been dwnloaded and also save inside the artifacts
#so have 2 model vgg16 model and updated base model 

class PrepareBaseModelTrainingPipeline:
    def __Init__(self):
        pass

    def main(self): #this we will run in terminal
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

#so initialize class and call this main method
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise 