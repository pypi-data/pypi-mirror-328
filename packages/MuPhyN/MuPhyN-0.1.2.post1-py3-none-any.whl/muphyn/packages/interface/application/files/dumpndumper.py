from typing import Dict

from .fileextensions import FileExtensions, supportedExtensions

def dump(dataDict: Dict, path: str, fileExtension: str):

    if fileExtension == ".yaml":
        Dumper.dumpYaml(dataDict, path)

    elif fileExtension == ".json":
        Dumper.dumpJson(dataDict, path)

    else:
        raise(ValueError(f"Not a supported file format '{fileExtension}':\n\t[{', '.join(supportedExtensions)}]"))
    
class Dumper:

    @staticmethod
    def dump(dataDict: Dict, path: str, extension: "FileExtensions"):
        if extension == FileExtensions.JSON:
            Dumper.dumpJson(dataDict, path)
        elif extension == FileExtensions.YAML:
            Dumper.dumpYaml(dataDict, path)
        else:
            raise(ValueError(f"Not a supported file extension: {extension}"))

    @staticmethod
    def dumpJson(dataDict: Dict, path: str):
        # Import json library
        import json

        # Save file
        with open(path, 'w') as file:
            json.dump(dataDict, file)

    @staticmethod
    def dumpYaml(dataDict: Dict, path: str):
        # Import yaml library
        import yaml

        # Save file
        with open(path, 'w') as file:
            yaml.dump(dataDict, file)
