#-----------------------------------
# Imports
#-----------------------------------

# general Imports
from typing import Iterable, Any

# PyQt6 Imports
from PyQt6 import QtGui
from PyQt6.QtCore import QPointF, QRectF
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import Path

from ...utils.constants import MuphynPens
from ..graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from .linktype import LinkType

#-----------------------------------
# Class
#-----------------------------------
class AbstractLinkModel (AbstractGraphicalElement) :
    """Est la classe abstraites aux classes représentant des liens entre les noeuds."""

    # -------------
    # Constants
    # -------------
    LinkToBoxMargin = 20
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, startPoint: QPointF, endPoint: QPointF, linkType : LinkType, text : str = '') :
        # Link parameters
        self._linkType: LinkType = linkType
        self._linkValue: float = 0.5

        # Text
        self._text: str = text

        # Start/End Position
        self._startPoint: QPointF = startPoint
        self._oldStartPoint: QPointF = startPoint
        self._endPoint: QPointF = endPoint
        self._oldEndPoint: QPointF = endPoint

        # Points
        points = AbstractLinkModel.calc_path_points(startPoint, endPoint)

        # Calculate origin
        bounding_rect = AbstractLinkModel.calc_bounding_rect(points)

        # Calculate all points from origin
        points = [point - bounding_rect.topLeft() for point in points]

        # Calculate steps
        steps = self.buildPath(points)
        if steps is None:
            return
        
        # Set Position
        AbstractGraphicalElement.__init__(self, 'link', bounding_rect.topLeft(), 0, text, None)

        # Append path
        self._path = Path(steps, parent=self)
        self._path.pen = MuphynPens.SelectedLinkPen if self.isSelected() else MuphynPens.UnSelectedLinkPen


    # -------------
    # Properties
    # -------------
    @AbstractGraphicalElement.rot.setter
    def rot (self, rot_ : float) -> None :
        ...

    @property
    def color(self) -> QColor:
        return self._path.border_color

    @property
    def link_type (self) -> LinkType :
        """Permet de récuperer le type de lien entre les deux noeuds."""
        return self._linkType

    @link_type.setter
    def link_type (self, link_type_ : LinkType) -> None :
        """Permet de modifier le type de lien entre les deux noeuds."""

        if self._linkType == link_type_ :
            return

        old_value = self._linkType

        self._linkType = link_type_

        if self._linkValue > 1.0 or self._linkValue < 0.0 :
            self._linkValue = 0.5

        if self.action_param_semaphore :
            return

        self.param_changed.emit(self, 'link_type', old_value, self._linkType)

    @property
    def link_value (self) -> float :
        """
        Permet de récuperer la valeur du lien :
        - en cas de lien courbe : la courbure du lien.
        - en cas de lien carré : le pourcentage avant que le lien ne se brise.
        """
        return self._linkValue

    @link_value.setter
    def link_value (self, link_value_ : float) -> None :
        """Permet de modifier la valeur du lien."""

        if self._linkValue == link_value_ :
            return

        old_value = self._linkValue

        self._linkValue = link_value_

        if self._linkValue > 1.0 or self._linkValue < 0.0 :
            self._linkValue = 0.5

        if self.action_param_semaphore :
            return

        self.param_changed.emit(self, 'link_value', old_value, self._linkValue)

    @property
    def startPoint(self) -> QPointF:
        return self._startPoint
    
    @startPoint.setter
    def startPoint(self, newStartPoint: QPointF):
        if self._startPoint != newStartPoint:
            self._startPoint = newStartPoint

            self.updateLink()

    @property
    def endPoint(self) -> QPointF:
        return self._endPoint
    
    @endPoint.setter
    def endPoint(self, newEndPoint: QPointF):
        if self._endPoint != newEndPoint:
            self._endPoint = newEndPoint

            self.updateLink()

    # -------------
    # Methods
    # -------------
    def boundingRect(self) -> QRectF:
        return self._path.boundingRect()
    
    def buildPath(self, points: Iterable[QPointF]):
        if self._linkType == LinkType.SQUARE:
            return AbstractLinkModel.build_straight_path(points)
        elif self._linkType == LinkType.CURVED:
            return AbstractLinkModel.build_curved_path(points)
        else:
            LogManager().Error(f"AbstractLinkModel.__init__() : Wrong link type {type(self._linkType)}")
            return None

    def setRotation(self, rot_ : float) -> None :
        ...
 
    def updateLink (self) -> None :
        """Est la méthode appelée lorsque la position ou la taille du node 2 est modifiée."""
        if self.scene() is None :
            return
        
        # Points
        points = AbstractLinkModel.calc_path_points(self._startPoint, self._endPoint)

        # Calculate origin
        bounding_rect = AbstractLinkModel.calc_bounding_rect(points)

        # Calculate all points from origin
        points = [point - bounding_rect.topLeft() for point in points]
        
        # Calculate steps
        steps = self.buildPath(points)
        self._path.steps = steps

        # Update Link Position
        self.setPos(bounding_rect.topLeft())

        # Calc update bounding rect
        min_x = min(self._startPoint.x(), self._oldStartPoint.x(), self._endPoint.x(), self._oldEndPoint.x()) - AbstractLinkModel.LinkToBoxMargin
        min_y = min(self._startPoint.y(), self._oldStartPoint.y(), self._endPoint.y(), self._oldEndPoint.y()) - AbstractLinkModel.LinkToBoxMargin
        max_x = max(self._startPoint.x(), self._oldStartPoint.x(), self._endPoint.x(), self._oldEndPoint.x()) + AbstractLinkModel.LinkToBoxMargin
        max_y = max(self._startPoint.y(), self._oldStartPoint.y(), self._endPoint.y(), self._oldEndPoint.y()) + AbstractLinkModel.LinkToBoxMargin
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)

        # Update Scene 
        self.scene().update(min_x, min_y, width, height)

        self._oldStartPoint = self._startPoint
        self._oldEndPoint = self._endPoint

    def itemChange (self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any:
        if change == QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged :
            self._path.pen = MuphynPens.SelectedLinkPen if bool(value) else MuphynPens.UnSelectedLinkPen
            self.updateLink()

        return super().itemChange(change, value)

    # --------------
    # Static Methods
    # --------------
    def calc_path_points(startPoint: QPointF, endPoint: QPointF):
        """
        This function assumes that the link start from the input of a box
        & ends in the output of the other box
        """
        # 2 points case
        """
        startPoint[]--x
                      |
                      x--[] endPoint
        """

        # Round points position
        # startPoint = QPointF(startPoint.toPoint())
        # endPoint = QPointF(endPoint.toPoint())

        if (endPoint.x() - AbstractLinkModel.LinkToBoxMargin) > (startPoint.x() + AbstractLinkModel.LinkToBoxMargin):
            # On the same height → 0 points to generate
            if endPoint.y() == startPoint.y():
                return [
                    startPoint,
                    endPoint
                ]
            # Not on the same heigth → 2 points to generate
            else:
                # Calculate intermediate X
                x_intermediate = (endPoint.x() + startPoint.x()) / 2

                # Append Intermediate points
                return [
                    startPoint,
                    QPointF(x_intermediate, startPoint.y()),
                    QPointF(x_intermediate, endPoint.y()),
                    endPoint,
                ]
        else:
            # 4 points case
            """
            x-[] 
            |
            x---------x
                      |     
                   []-x
            """
            # Calculate intermediate coordinates
            y_intermediate = int((endPoint.y() + startPoint.y()) / 2)

            # Append Intermediate points
            return [
                startPoint,
                startPoint + QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
                QPointF(startPoint.x() + AbstractLinkModel.LinkToBoxMargin, y_intermediate),
                QPointF(endPoint.x() - AbstractLinkModel.LinkToBoxMargin, y_intermediate),
                endPoint - QPointF(AbstractLinkModel.LinkToBoxMargin, 0),
                endPoint,
            ]

    def calc_bounding_rect(points: Iterable[QPointF]) -> QRectF:
        min_x = min([point.x() for point in points])
        max_x = max([point.x() for point in points])
        min_y = min([point.y() for point in points])
        max_y = max([point.y() for point in points])

        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        return QRectF(min_x, min_y, width, height)

    def build_straight_path(points: Iterable[QPointF]):
        return [Path.Step(point) for point in points]

    def build_curved_path(points: Iterable[QPointF]):
        factor = 0.2
        path = QtGui.QPainterPath(points[0])

        last_end_point = QPointF
        for index, corner in enumerate(points[1: -1]):
            # Calculate middle of corner segments
            middle_point_1 = (points[index] + corner) / 2
            middle_point_2 = (points[index+2] + corner) / 2

            start_point = (1-factor) * middle_point_1 + factor * corner
            end_point = (1-factor) * middle_point_2 + factor * corner

            path.cubicTo(start_point, corner, end_point)

        path.lineTo(points[-1])

        return path
    
    