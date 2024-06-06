from cnnClassifier.constants import * #* means all
from cnnClassifier.utils.common import read_yaml , create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig)


CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")


#inside file created constructer 2 path initialize here in this class variable
#inside this reading 2 files by read_yaml fun and store inn 2 var config and params
#create directories self.artifacts_roots it will return as key value pair

# Import constants
class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

#above is configuration class inside it prepare data_ingestion related configuration
#define above in class as entiry its returntype as DataIngestionConfig liek node calss in LL 
#this returnonly value mention in DataIngestionConfig

#2.update config
#1.extracting data ingestion related configuration #2. and then storing one by one
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        #what ever define in configuration mention it here

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config