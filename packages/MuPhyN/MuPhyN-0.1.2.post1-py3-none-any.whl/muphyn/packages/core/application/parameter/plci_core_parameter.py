
from typing import Any, Dict, overload


from ..data.plci_core_data import Data
from ..data.plci_core_data_type import DataType, get_data_type

class Parameter:

    @overload
    def __init__(self, name: str, type_: Any, value: Any):
        pass

    @overload
    def __init__(self, name: str, data: Data):
        pass

    def __init__(self, name: str, *args):
        self._name: str = name
        
        if len(args) == 1 and type(args[0]) == Data:
            self._data = args[0]
        elif len(args) == 2:
            self._data = Data(get_data_type(args[0]), args[1])

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def type(self) -> Any:
        return self._data.data_type
    
    @property
    def value(self) -> Any:
        return self._data.value
    
    def __str__(self) -> str:
        return f"Parameter(name = \"{self._name}\", type = {self.type}, value = {self.value})"
    
    @staticmethod
    def fromDict(dict_: Dict) -> "Parameter":

        # Extract parameter attributes from dict
        name = dict_.get("name", "")
        type_ = dict_.get("type", None)
        value = dict_.get("value", None)

        # Get type from value if no type defined
        if type_ is None and value is not None:
            type_ = get_data_type(str(type(value)))

        # Set default value
        if type is not None and value is None:
            value = get_data_type(dict_["type"]).default_value()

        return Parameter(name, type_, value)
    
if __name__ == "__main__":

    # Create parameter form dict
    parameter = Parameter.fromDict({"name": "parameter", "type": "float", "value": "1e-3"})

    # Assertion
    assert parameter.name == "parameter"
    assert parameter.type == DataType.FLOAT
    assert parameter.value == 0.001