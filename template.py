import os
from pathlib import Path
import logging
logging.basicConfig(level = logging.INFO, format='[%(asctime)s %(message)s:]')
project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configration.py",
    f"src/{project_name}/pipeline/configration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.py",
    "parmas.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # print(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filename)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory : {filedir} for the file : {filedir}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize) : 
        with open(filepath, "w")as f:
            pass 
            logging.info(f"Creating empty file: {filepath}") 

    else:
        logging.info(f"{filename} is alreasy exists") 