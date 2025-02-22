# General import
from enum import Enum
import numpy as np

# PyQt imports
from PyQt6.QtGui import QColor, QImage, QPixmap

class PatternBuilder:

    class PatternType(Enum):
        CrossPattern = 0
        SquarePattern = 1

    # -------------
    # Constants
    # -------------
    DefaultGridColor = QColor(200, 200, 200)

    @staticmethod
    def buildPixmap(gridSize: int, patternType: PatternType, color: QColor = DefaultGridColor) -> QPixmap:
        if patternType == PatternBuilder.PatternType.CrossPattern:
            return PatternBuilder.buildCrossPattern(gridSize, color)
        elif patternType == PatternBuilder.PatternType.SquarePattern:
            return PatternBuilder.buildSquarePattern(gridSize, color)
        else:
            raise(ValueError(f"PatternBuilder.buildPixmap(): Pattern type not supported {patternType}"))
            return QPixmap(gridSize, gridSize)

    @staticmethod
    def buildCrossPattern(gridSize: int, color: QColor = DefaultGridColor) -> QPixmap:
        # Convetr color to list
        colorList = [color.red(), color.green(), color.blue()]

        # Init numpy array
        npPattern = np.full((gridSize, gridSize, 3), 255, np.uint8)

        # Change numpy array pattern
        ## Top left corner
        npPattern[0,:3] = colorList
        npPattern[:3,0] = colorList

        ## Top right corner
        npPattern[0,-2:] = colorList

        ## Bottom left corner
        npPattern[-2:,0] = colorList

        bytesPerLine = 3 * gridSize
        return QImage(npPattern.data, gridSize, gridSize, bytesPerLine, QImage.Format.Format_RGB888)

    @staticmethod
    def buildSquarePattern(gridSize: int, color: QColor = DefaultGridColor) -> QPixmap:
        # Convetr color to list
        colorList = [color.red(), color.green(), color.blue()]

        # Init numpy array
        npPattern = np.full((gridSize, gridSize, 3), 255, np.uint8)

        # Change numpy array pattern
        ## Replace first row
        npPattern[0,:] = colorList
        ## Replace first column
        npPattern[1:,0] = colorList

        bytesPerLine = 3 * gridSize
        return QImage(npPattern.data, gridSize, gridSize, bytesPerLine, QImage.Format.Format_RGB888)