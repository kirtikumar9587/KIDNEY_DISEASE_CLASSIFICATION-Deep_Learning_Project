#first import the log here
from src.cnnClassifier import logger

logger.info("Welcome to our custom log") #see that log folder has been created

#same msg get by running this file is saved in running_log which we can see by terminal also
#after production this applicaion we can't any terminal to see log what is happening in our code by download file and you can easily look into it and fix it.
#so why create log file inside src instead of creating lof folder out in main
#so write inside cnnclassifier so need to go inside this folder again and again