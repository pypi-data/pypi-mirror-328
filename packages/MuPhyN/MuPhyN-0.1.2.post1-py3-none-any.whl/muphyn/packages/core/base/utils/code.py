import importlib
import os
import sys

from importlib._bootstrap import ModuleSpec
from types import ModuleType

def loadCode(libraryName: str, pythonFilePath: os.PathLike) -> ModuleType:
    
    # Test if file exists
    if not os.path.exists(pythonFilePath):
        raise(FileNotFoundError(f"Python file doesn't exists: {pythonFilePath}"))
    
    # Build absolute path
    if not os.path.isabs(pythonFilePath):
        pythonFilePath = os.path.abspath(pythonFilePath)
    
    # Add file path to sys
    sys.path.insert(0, os.path.dirname(pythonFilePath))

    # Importations des méthodes du fichier python.
    spec: ModuleSpec = importlib.util.spec_from_file_location(libraryName, pythonFilePath)
    foo: ModuleType = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    # Remove path from sys
    sys.path.pop(0)

    return foo
