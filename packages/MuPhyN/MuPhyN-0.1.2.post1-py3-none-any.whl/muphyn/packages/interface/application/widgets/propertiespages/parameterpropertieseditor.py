#-----------------------------------
# Imports
#-----------------------------------

from muphyn.packages.interface.base import PropertyLabel
from ...models.graphicalmodels.boxmodel.boxmodel import BoxModel
from ..datapropertywidgets.datapropertywidgetsfactory import property_widget_factory
from .abstractpropertieseditor import AbstractPropertiesEditor


#-----------------------------------
# Class
#-----------------------------------

class ParameterPropertiesEditor (AbstractPropertiesEditor) :
    """Est l'éditeur qui permet modifier un paramètre."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_model : BoxModel, parameter : str) :

        self._parameter = parameter
        self._box_model = box_model
        self._box_model.param_changed.connect(self.box_param_changed)

        AbstractPropertiesEditor.__init__(self, box_model)

        parameter_to_edit = self.box_model.get_parameter(self._parameter)
        self._semaphore_values = True

        self._widget_value_editor.setValue(parameter_to_edit['value'])

        self._semaphore_values = False
    # -------------
    # Properties
    # -------------

    @property
    def parameter (self) -> str :
        """Permet de récuperer le nom du paramètre qui doit être édité dans la box."""
        return self._parameter

    @property
    def box_model (self) -> BoxModel : 
        """Permet de récuperer le modème de la box dont le paramètre est édité."""
        return self._box_model

    # -------------
    # Methods
    # -------------
    def box_param_changed (self, box, param_name, old_value, new_value) -> None :
        """Est la méthode qui est appelée lorsque la box modifiée par le panel voit un de ses paramètres changer."""
        if not(box == self._model):
            return

        if not(param_name == 'params.' + self._parameter) :
            return

        self._semaphore_values = True

        self._widget_value_editor.setValue(new_value)

        self._semaphore_values = False


    def init_ui (self) -> None :
        # Parameter Name Label
        self._parameter_name_label: PropertyLabel = PropertyLabel(self.parameter)
        
        # Parameter Value
        parameter_to_edit = self.box_model.get_parameter(self.parameter)
        self._widget_value_editor = property_widget_factory(parameter_to_edit)
        self._widget_value_editor.valueChanged.connect(self.on_value_changed)

        # Add Row
        row = self.layout().rowCount()
        self.layout().addWidget(self._parameter_name_label, row, 0)
        self.layout().addWidget(self._widget_value_editor, row, 1)
        # self.layout().addRow(self._parameter_name_label, QLabel("test"))

    def translate_ui (self) -> None:
        pass
        # self._lbl_parameter_name.setText(QCoreApplication.translate(self.objectName(), u"Nom : ", None))
        # self._lbl_parameter_type.setText(QCoreApplication.translate(self.objectName(), u"Type : ", None))
        # self._lbl_parameter_value.setText(QCoreApplication.translate(self.objectName(), u"Valeur : ", None))

    def unload (self) -> None :
        self._box_model.param_changed.disconnect(self.box_param_changed)


    def on_value_changed(self) -> None:
        if self._semaphore_values :
            return

        # Get old & new values
        new_value = self._widget_value_editor.value
        old_value = self.box_model.get_parameter(self.parameter)['value']
        param_name = 'params.' + self.parameter

        # Prepare action holder
        self.actions_generator(old_value, new_value, param_name)
        
        # Apply parameter value change
        self.box_model.action_param_semaphore = True
        self.box_model.set_parameter(self.parameter, new_value)
        self.box_model.action_param_semaphore = False