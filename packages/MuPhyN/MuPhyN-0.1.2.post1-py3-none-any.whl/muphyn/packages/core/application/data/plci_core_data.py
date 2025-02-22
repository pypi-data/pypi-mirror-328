#-----------------------------------
# Imports
#-----------------------------------
from typing import Any

from .plci_core_data_type import DataType

#-----------------------------------
# Class
#-----------------------------------

class Data : 
    """Est l'objet contenant les données transité par les signaux."""

    # -------------
    # Constructors
    # -------------
    def __init__ (self, dataType : DataType, value : Any = None) :

        # Init object attributes
        self._dataType = None
        self._value = None
        
        # Set Data Type
        self.setDataType(dataType)
        
        # Set value
        self.setValue(value)

    # -------------
    # Properties
    # -------------

    @property
    def data_type (self) -> DataType : 
        """Permet de récuperer le type de la donnée."""
        return self._dataType
    
    @data_type.setter
    def data_type(self, newDataType: DataType):
        self.setDataType(newDataType)

    @property
    def value (self) -> Any :
        """Permet de récuperer la valeur actuelle."""
        return self._value
    
    @value.setter
    def value(self, newValue: Any):
        self.setValue(newValue)
    
    def setDataType(self, newDataType: DataType):
        if self._dataType != newDataType:
            # Assert data type
            if not isinstance(newDataType, DataType):
                raise(TypeError(f"dataType has unsupported type: {type(newDataType)} instead of DataType")) 
            
            self._dataType = newDataType

    def setValue(self, newValue: Any):
        # Handle no value has been passed
        newValue = self._dataType.default_value() if newValue is None else newValue

        if self._value != newValue:
            # Convert value if type supports it
            if hasattr(self._dataType.value[0], "convertValue"):
                newValue = self._dataType.value[0].convertValue(newValue)

            self._value = newValue

    def __str__ (self) -> str :
        """Permet de récuperer la données sous la forme d'un string."""
        return f"Data [type: {self._dataType} | value: {self._value}]"

if __name__ == "__main__":

    # Init Data object
    data = Data(DataType.FLOAT, 0.001)

    # Assertion
    assert data.data_type == DataType.FLOAT
    assert data.value == 0.001