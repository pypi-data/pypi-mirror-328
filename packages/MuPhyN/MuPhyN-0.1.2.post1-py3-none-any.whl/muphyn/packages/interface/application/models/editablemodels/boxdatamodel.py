from datetime import date

from muphyn.packages.core.application import AbstractBoxData
from .abstracteditablemodel import AbstractEditableModel

class BoxDataModel(AbstractEditableModel):

    def __init__(self, boxData: AbstractBoxData):
        super().__init__(boxData.box_name, boxData.path, boxData.creator, date.today(), boxData.version)

        self._boxData: AbstractBoxData = boxData

    @property
    def boxData(self) -> AbstractBoxData:
        return self._boxData
    
    
    @property
    def editor_type (self) -> str :
        """Permet de récuperer le type d'éditeur à utiliser."""
        return 'box-data-editor'
