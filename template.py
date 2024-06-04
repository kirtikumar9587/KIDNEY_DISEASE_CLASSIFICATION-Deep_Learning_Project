#This is Python code to create the file and folder structure in directory
import os
from pathlib import Path
import logging

#logging string
#need to create a logging string here -why -whenever execute template file so what activity this file this creating a folder and all other.instead of printing them you can log them
#so instead of print statement use logging
#basicConfig-function need to use #here level-here only log the info related to log that info related to log that want to print inside terminal
#format-extract the current time with that give logging msg
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

#create some list of files and folder #firstly create .github holder and all other inside it.
#make .gitkeep because whenever commenting code in github if folder is empty it cannot be consider it not upload in gihub .it should have inside it so keep .gitkeep
#so whenever creating cicd pipeline remove this file and create cicd component
#then creating one folder src
#like in keras official library folder has component so can create or remove folder there
#this down all are components need in project # inresearch -creating all jupyter notebook experiment
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",#creating all jupyter notebook experiment
    "templates/index.html"

]#create another component then only add above like add test.py

#from above folder providing one by one #then pass complete path #
for filepath in list_of_files:
    filepath = Path(filepath) #Path -if run in any os it will run inall sometimes it not run in all os
    filedir, filename = os.path.split(filepath)#seperate the file .py and the folder

#getting folder so create a folder
    if filedir !="":#folder is present then not create if present then create
        os.makedirs(filedir, exist_ok=True)
        #calling the logging string
        logging.info(f"Creating directory; {filedir} for the file: {filename}")#creating a directory for the file

#now also create file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:#it will crate file and write inside it
            pass
            logging.info(f"Creating empty file: {filepath}")# then display creating file


    else:
        logging.info(f"{filename} is already exists")

