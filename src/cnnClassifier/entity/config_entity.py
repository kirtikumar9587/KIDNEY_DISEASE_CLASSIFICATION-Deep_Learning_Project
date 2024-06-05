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

    #here need to import two things