import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Any other exception that occurs during the reading process.

    Returns:
        ConfigBox: The ConfigBox containing the YAML file's contents.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of paths for the directories to be created.
        verbose (bool, optional): If True, log the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as a JSON file.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data to a file.

    Args:
        data (Any): The data to be saved as binary.
        path (Path): The path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.

    Args:
        path (Path): The path of the file.

    Returns:
        str: The size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    """Decodes an image from a base64 encoded string and saves it to a file.

    Args:
        imgstring (str): The base64 encoded image data.
        fileName (str): The name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image from a file into a base64 string.

    Args:
        croppedImagePath (str): The path to the image file.

    Returns:
        str: The base64 encoded image data.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
