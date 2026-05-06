import os
from pathlib import Path        # Used for handling file paths in an OS-independent way
import logging                  # Used for tracking and monitoring execution

# -----------------------------------------
# Configure logging
# -----------------------------------------
# This will print logs with timestamp and message
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %(message)s]'
)

# -----------------------------------------
# Project name (used inside src folder)
# -----------------------------------------
project_name = "cnnClassifier"

# -----------------------------------------
# Define project structure (files & folders)
# -----------------------------------------
list_of_files = [

    # CI/CD folder for GitHub Actions
    ".github/workflows/.gitkeep",  
    # .gitkeep ensures Git tracks empty folders

    # -------------------------------
    # Source code structure
    # -------------------------------
    f"src/{project_name}/__init__.py",  
    # Makes cnnClassifier a Python package

    f"src/{project_name}/components/__init__.py",  
    # Contains pipeline components (data ingestion, model training, etc.)

    f"src/{project_name}/utils/__init__.py",  
    # Utility/helper functions (logging, common methods)

    f"src/{project_name}/config/__init__.py",  
    # Config module (reads YAML and manages configuration)

    f"src/{project_name}/config/configuration.py",  
    # Main configuration manager (loads YAML, creates config objects)

    f"src/{project_name}/pipeline/configuration.py",  
    # (Better rename later) Currently unclear purpose — should ideally be pipeline stage files

    f"src/{project_name}/entity/__init__.py",  
    # Stores data classes (structured configs)

    f"src/{project_name}/constants/__init__.py",  
    # Stores constant values (paths, filenames, etc.)

    # -------------------------------
    # External config & scripts
    # -------------------------------
    "config/config.yaml",  
    # External configuration (paths, URLs, settings)

    "dvc.yaml",  
    # Script related to Data Version Control (DVC usage)

    "params.yaml",  
    # Stores hyperparameters (better practice: move to YAML instead)

    "requirements.txt",  
    # Python dependencies

    "setup.py",  
    # Used for packaging the project

    # -------------------------------
    # Research & frontend
    # -------------------------------
    "research/trials.ipynb",  
    # Jupyter notebook for experiments

    "templates/index.html"  
    # Frontend template (for web app using Flask/FastAPI)
]

# -----------------------------------------
# Create directories and files
# -----------------------------------------
for filepath in list_of_files:
    filepath = Path(filepath)

    # Split into directory and filename
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # -----------------------------------------
    # FIXED CONDITION (IMPORTANT)
    # -----------------------------------------
    # Create file if:
    # 1. File does not exist OR
    # 2. File exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create empty file
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")