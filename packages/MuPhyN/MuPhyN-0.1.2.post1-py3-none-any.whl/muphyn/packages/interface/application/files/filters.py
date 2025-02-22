import re
from .dumpndumper import Dumper
from .fileextensions import FileExtensions

fileExtensions = {value.name: value.value for value in list(FileExtensions._member_map_.values())}
fileFilters = [f"{fileType} (*{fileExtension})" for fileType, fileExtension in fileExtensions.items()]

# Initial file filter
allSupportedFileFormatsFilter = f"All supported types ({' '.join([f'*{fileExtension}' for fileExtension in fileExtensions.values()])})"

# Save file filter list
saveFileFilter = ";;".join(fileFilters)
defaultSupportedFileFormat = FileExtensions.YAML
defaultInitialFileFilter = f"{defaultSupportedFileFormat.name} (*{defaultSupportedFileFormat.value})"

# Load file filter list
loadFileFilter = f"{allSupportedFileFormatsFilter};;{saveFileFilter};;All (*)"

# Get extension
def getExtensionFromFilter(filter_: str) -> FileExtensions:
    # Build pattern
    filterPattern = r"(?P<name>\w+) \(\*(?P<extension>\.\w+)\)"

    if match := re.match(filterPattern, filter_):
        # Get name
        name = match.groupdict()["name"]

        # Get extension
        if name in FileExtensions._member_map_:
            return FileExtensions._member_map_[name]
            
    return None