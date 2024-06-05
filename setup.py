#-e will install local package automaticaly with the help of setup.py
import setuptools
#firslty reading readme file #This is ont imp but this will help when publishing this project thatt time it needed
#give description above file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#version of our project
__version__ = "0.0.0"

#project description
#here install cnnClassifier as local package in python enviromnment this folder is considered as local package
REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "kirtikumar9587"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "kirtikumar963@gmail.com"

#this code will remain same this will look for constructure file and install as my local package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    #key and value in this.This formatted string essentially constructs the URL for the bug tracker of a project hosted on GitHub
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)