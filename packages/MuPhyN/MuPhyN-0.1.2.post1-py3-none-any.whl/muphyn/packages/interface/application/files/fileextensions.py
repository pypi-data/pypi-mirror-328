from enum import Enum

class FileExtensions(Enum):
    JSON = ".json"
    YAML = ".yaml"

supportedExtensions = [value.value for value in list(FileExtensions._member_map_.values())]