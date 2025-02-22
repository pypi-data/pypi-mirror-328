
# General imports
from typing import Any, Union

# PyQt6 imports
from PyQt6.QtCore import QMarginsF, QPointF, QRectF, QSizeF, Qt
from PyQt6.QtWidgets import QGraphicsItem

# Project imports
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import Icon, AbstractImage, GroupedShapes, Text, VerticalLayout
from muphyn.packages.interface.application.utils.constants import MuphynFonts

class BoxModelInfoArea(GroupedShapes):

    # -------------
    # Constants
    # -------------
    ItemSpacing = 5

    def __init__(self, box_body_size: QSizeF, name: str, image_path: str = None, 
            value: Any = None, margins: Union[int, float, QMarginsF] = None, parent: QGraphicsItem = None) -> None:
        
        # Handle box details
        self._value = value
        self._image_path: str = image_path
        self._name: str = name

        # Init Grouped Shapes
        super().__init__(QPointF(), parent=parent)

        # Handle Margins
        self.set_margins(margins)

        # Calculate marginized bounding rect
        box_body_bounding_rect = QRectF(QPointF(0, 0), box_body_size)
        marginized_bounding_rect = box_body_bounding_rect.marginsRemoved(self.margins)

        # Add Layout
        self.layout = VerticalLayout(group_position=marginized_bounding_rect.topLeft(), parent=self)
        self.layout.setMaximumWidth(marginized_bounding_rect.size().width())
        self.layout.setMaximumHeight(marginized_bounding_rect.size().height())
        self.layout.setSpacing(BoxModelInfoArea.ItemSpacing)

        if image_path is not None:
            # Icon
            self.icon_shape: AbstractImage = Icon(image_path)

            # Add to layout
            self.layout.addItem(self.icon_shape)

        if value is not None:
            # Text Flag
            self.text_align = Qt.AlignmentFlag.AlignHCenter

            # Value Label
            self.value_label: Text = Text(
                str(value), text_max_width=self.layout.maximumWidth,
                font=MuphynFonts.BoxModelDetailsFont, alignment=self.text_align)
                
            # Add to layout
            self.layout.addItem(self.value_label, height=self.value_label.size.height())

    def set_value(self, value: str):
        if not hasattr(self, "value_label"):
                        # Text Flag
            self.text_align = Qt.AlignmentFlag.AlignHCenter

            # Value Label
            self.value_label: Text = Text(
                str(value), text_max_width=self.layout.maximumWidth,
                font=MuphynFonts.BoxModelDetailsFont, alignment=self.text_align)
                
            # Add to layout
            self.layout.addItem(self.value_label, height=self.value_label.size.height())
        else:
            self.value_label.text = str(value)

    def setIcon(self, icon):
        # Create Icon shape object
        icon_shape: AbstractImage = Icon(icon)

        if not hasattr(self, "icon_shape"):
            # Icon
            self.icon_shape: AbstractImage = icon_shape
        else:
            self.layout.removeItem(self.icon_shape)

        # Icon
        self.icon_shape: AbstractImage = icon_shape

        # Add to layout
        self.layout.addItem(self.icon_shape)

    def set_bounding_rect(self, new_bounding_rect_size: QSizeF):
        # 
        marginized_bounding_rect_size = new_bounding_rect_size.shrunkBy(self.margins)

        # Update max height/width
        self.layout.setMaximumWidth(marginized_bounding_rect_size.width())
        self.layout.setMaximumHeight(marginized_bounding_rect_size.height())

        # Update layout child items position
        self.layout.recomputeChildrenPosition()

    def set_margins(self, new_margins: Union[int, float, QMarginsF]):
        # Handle margins format
        if new_margins is None:
            new_margins = QMarginsF(0, 0, 0, 0)
        elif type(new_margins) == float or type(new_margins) == int:
            new_margins = QMarginsF(new_margins, new_margins, new_margins, new_margins)
        elif type(new_margins) != QMarginsF:
            LogManager().error(f"BoxModelInfoArea: Wrong margins format {type(new_margins)} instead of {type(QMarginsF)}")
            return

        self.margins = new_margins