from math import log
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(action_name)s]: %(message)s]:')

project_name = 'textSummarizer'

list_files = [
        "github/worflows/.gitkeep", # For CI CD
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constant/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "app.py",
        "main.py",
        "Dockerfile",
        "requirement.txt",
        "setup.py",
        "research/trial.ipynb"
    ]

# Create files automatically
for filepath in list_files:
    filepath = Path(filepath)
    # Create filename inside filedir
    filedir, filename = os.path.split(filepath) 

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

        # If file existed or contain code, skip
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} already exsits")