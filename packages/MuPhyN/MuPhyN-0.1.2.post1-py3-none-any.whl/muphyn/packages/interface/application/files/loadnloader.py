import os
from typing import Dict

from .fileextensions import FileExtensions, supportedExtensions

def load(path: str) -> Dict:
    # Get file extension
    fileExtension = os.path.splitext(path)[-1]

    if fileExtension == ".yaml":
        return Loader.loadYaml(path)

    elif fileExtension == ".json":
        return Loader.loadJson(path)
    
    else:
        raise(ValueError(f"Not a supported file format '{fileExtension}':\n\t[{', '.join(supportedExtensions)}]"))
    
class Loader:

    @staticmethod
    def load(dataDict: Dict, path: str, extension: "FileExtensions"):
        if extension == FileExtensions.JSON:
            Loader.loadJson(dataDict, path)
        elif extension == FileExtensions.YAML:
            Loader.loadYaml(dataDict, path)
        else:
            raise(ValueError(f"Not a supported file extension: {extension}"))

    @staticmethod
    def loadJson(path: str) -> Dict:
        # Import json library
        import json

        # Save file
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def loadYaml(path: str) -> Dict:
        # Import yaml library
        import yaml

        # Save file
        with open(path, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
