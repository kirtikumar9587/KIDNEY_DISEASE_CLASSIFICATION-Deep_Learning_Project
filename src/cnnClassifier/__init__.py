# create logging module here and for all other componesnt import from here. this is python logging functionality 

import os
import sys#system
import logging#using this create custom loginf
#firstly it will store ascii timestamp then store log level name-info level then modeule which module you are this file like template then print message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#it will create one log folder inside it create running_logs.log file and inside this it will save all the log
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)#make exist_ok=true

#define loging functionality
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,#above logging string

#get the file and also want to see in terminal
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

#creating logger object and cnnClassifierLogger is name of logger object
logger = logging.getLogger("cnnClassifierLogger")