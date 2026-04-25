import os
from pathlib import Path    # Define the path 
import logging              # Track or monitering the application 

logging.basicConfig(level = logging.INFO, format='[%(asctime)s %(message)s:]') # what show in logs

project_name = "cnnClassifier" 

# create many files
list_of_files = [
    ".github/workflows/.gitkeep",                   # .gitkeep : when make  CI/CD ==> we make automation workflow ==> this script write on this file 
    f"src/{project_name}/__init__.py",              # __init__.py : make package 
    f"src/{project_name}/components/__init__.py",   # component : there have data Injection 
    f"src/{project_name}/utils/__init__.py",        # utils : in folder we have our parameter like : learning rate 
    f"src/{project_name}/config/__init__.py",       # config : in folder we have our confugration which file import 
    f"src/{project_name}/config/configuration.py",   # configration.py : this monitor all the parameter
    f"src/{project_name}/pipeline/configuration.py", # 
    f"src/{project_name}/entity/__init__.py",       # entity folder
    f"src/{project_name}/constants/__init__.py",    # constance folder 
    "config/config.yaml",                           # config.yaml ==> wrtite script
    "dvc.py",                                       # DVC 
    "parmas.py",                                    # write parameter like learning rate
    "requirements.txt",                             #
    "setup.py",                                     #
    "research/trails.ipynb",                        #
    "templates/index.html"                          # for frontend
]

# this loop help to create project structure 
for filepath in list_of_files:                      
    filepath = Path(filepath)
    # print(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filename)
    if filedir != "":                               # file path gives value zero 
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory : {filedir} for the file : {filedir}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize) :    # 
        with open(filepath, "w")as f:
            pass 
            logging.info(f"Creating empty file: {filepath}") 

    else:
        logging.info(f"{filename} is alreasy exists") 