# entiry is return type of any function ,returntype of data detation function
#create out custmo entity using data calss
from dataclasses import dataclass#is a decorator define top of data veriable so it can can access from anywhere this entity
from pathlib import Path

#root-dir from yaml file
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#1.update entity

#create entity here like data_ingestion create another dataclass na dinside that assigned parameter from params.yaml
#frozen=true not want to add any other parameter


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int