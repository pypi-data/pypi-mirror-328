
#
from muphyn.packages.core.application import DataType
from muphyn.packages.core.base import LogManager

from ..propertiespages.abstractpropertieseditor import AbstractPropertiesEditor
from .basictypes.unknownpropertywidget import UnknownTypePropertyWidget
from .choices.choicepropertywidget import ChoicePropertyWidget
from .pathtypes.anyfilepropertywidget import AnyFilePropertyWidget
from .pathtypes.directorypropertywidget import DirectoryPropertyWidget
from .pathtypes.existingfilepropertywidget import ExistingFilePropertyWidget
from .pathtypes.existingfilespropertywidget import ExistingFilesPropertyWidget

from .basictypes.booleanpropertywidget import BooleanPropertyLineEdit
from .basictypes.integerpropertylineedit import IntegerPropertyLineEdit
from .basictypes.floatpropertylineedit import FloatPropertyLineEdit
from .basictypes.ndarraypropertywidgets import NdArrayPropertyLineEdit
from .basictypes.stringpropertylineedit import StringPropertyLineEdit

def property_widget_factory(parameter_to_edit: dict) -> AbstractPropertiesEditor:
    # Get parameter type name
    param_type_name = parameter_to_edit["type"].__str__().lower()


    if param_type_name == str(DataType.BOOLEAN):
        return BooleanPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.FLOAT):
        return FloatPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.INT):
        return IntegerPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.STRING):
        return  StringPropertyLineEdit(parameter_to_edit)

    # elif param_type_name == str(DataType.Vector):
    #     return  StringPropertyLineEdit(parameter_to_edit)

    # elif param_type_name == str(DataType.Matrix):
    #     return  StringPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.NDARRAY):
        return NdArrayPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.ANYFILE):
        return AnyFilePropertyWidget()

    elif param_type_name == str(DataType.DIRECTORY):
        return DirectoryPropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILE):
        return ExistingFilePropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILES):
        return ExistingFilesPropertyWidget()

    elif param_type_name == str(DataType.CHOICE):
        return ChoicePropertyWidget(parameter_to_edit)
    else:
        LogManager().error(f"Unsupported parameter type for : {param_type_name}")
        return UnknownTypePropertyWidget(param_type_name.__str__())