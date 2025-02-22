#-----------------------------------
# Import
#-----------------------------------
import numpy as np
from copy import deepcopy
from typing import Any, Union

from muphyn.packages.core.base import Enum
    
#-----------------------------------
# Class
#-----------------------------------

class AbstractType:

    def defaultValue(self):
        raise(NotImplementedError(f"{self.__class__.__name__}.defaultValue() not implemented yet!"))
    
    def isTypeOf(self, typeName: str):
        if not hasattr(self, "Names"):
            raise(ValueError(f"{self.__class__.__name__}.Names not defined!"))
        return typeName.lower() in self.Names
    
class Undefined(AbstractType):

    def defaultValue(self):
        return None

    def isTypeOf(self, typeName: str):
        return False

class String(AbstractType):
    Names = ["string", "str"]
    def defaultValue(self):
        return str()
    
    def convertValue(self, value: str):
        if value is None:
            return self.defaultValue()
        return str(value)
    
class Integer(AbstractType):
    Names = ["int", "integer"]
    def defaultValue(self):
        return int()
    
    def convertValue(self, value: str):
        if value is None:
            return self.defaultValue()
        return int(float(value))
    
class Float(AbstractType):
    Names = ["float"]
    def defaultValue(self):
        return float()
    
    def convertValue(self, value: str):
        if value is None:
            return self.defaultValue()
        return float(value)
    
class Boolean(AbstractType):
    Names = ["bool", "boolean"]
    def defaultValue(self):
        return bool()
    
    def convertValue(self, value: str):
        if value is None:
            return self.defaultValue()
        return bool(value)
    
class Object(AbstractType):
    Names = ["object"]
    def defaultValue(self):
        return None
    
class AnyFile(AbstractType):
    Names = ["any file", "anyfile"]
    def defaultValue(self):
        return str()
    
class ExistingFile(AbstractType):
    Names = ["existing file", "existingfile"]
    def defaultValue(self):
        return str()
    
class ExistingFiles(AbstractType):
    Names = ["existing files", "existingfiles"]
    def defaultValue(self):
        return str()
    
class Directory(AbstractType):
    Names = ["directory"]
    def defaultValue(self):
        return str()
    
class Choice(AbstractType):
    Names = ["choice", "choices"]
    def defaultValue(self):
        return []
    
class DataType(Enum) : 
    """Est l'enum qui décrit les types acceptés dans les signaux."""


    UNDIFINED = Undefined(),
    """Est le type qui définis un objet indéfinis."""

    STRING = String(),
    """Est le type qui définis un string."""

    INT = Integer(),
    """Est le type qui définis un entier."""

    FLOAT = Float(),
    """Est le type qui définis un nombre à virgule flottante."""

    BOOLEAN = Boolean(),
    """Est le type qui définis un boolean."""
    
    OBJECT = Object(),
    """Est le type qui définis un objet."""

    NDARRAY = np.array([0]),
    """Est le type qui définit un array numpy."""

    ANYFILE = AnyFile()
    """Est le type qui définis un chemin vers un fichier existant ou non."""

    DIRECTORY = Directory()
    """Est le type qui définis un chemin vers un dossier existant."""

    EXISTINGFILE = ExistingFile()
    """Est le type qui définis un chemin vers un fichier existant."""

    EXISTINGFILES = ExistingFile()
    """Est le type qui définis une liste de chemins pointant chacun vers un fichier existant."""

    CHOICE = 9

    def __deepcopy__(self, memo):
        return DataType.items()[self][0].__class__()


    def __str__ (self) :
        """Permet de retourner le data type sous la forme d'un nom."""
        return self.name.lower()

    def default_value (self: "DataType") -> Any :
        """Permet de récuperer la valeur par défaut des données suivant le type."""
        if self in DataType.keys():
            return self.value[0].defaultValue()        
        else:
            return None


#-----------------------------------
# Functions
#-----------------------------------

def get_data_type (value: Union[str, int, DataType]) -> DataType :
    """Permet de retourner un data type suivant la valeur passé en paramètre."""

    # Return DataType from type name
    if isinstance(value, str):        
        for type_ in DataType:
            if type_.value[0].isTypeOf(value):
                return type_

    # Return DataType from index
    elif isinstance(value, int): 
        return DataType[value]

    # Return value if already a datatype
    elif isinstance(value, DataType):
        return value
    
    return DataType.UNDIFINED

if __name__ == "__main__":
    # Init value
    typeName = "int"

    # Get data type from type name
    dataType = get_data_type(typeName)

    # Deep copy data type
    deepcopy(dataType)