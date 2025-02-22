import numbers
import numpy as np
from typing import Dict, List, Optional, Tuple

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFormLayout, QHBoxLayout, QLabel,\
    QScrollArea, QSplitter, QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import Cursor

import matplotlib.style as mplstyle
from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseEvent

from muphyn.packages.core.application.box.plci_core_box import Box

def _closest(a:float, b:list) -> Tuple[float, float]:
    c = [abs(x-a) for x in b]
    i = c.index(min(c))
    return (i, b[i])

def identifySignal(signals: Dict[str, List[float]]) -> Dict[str, Dict[str, float]]:

    # Init dictionary
    signalInfos = {}

    for key, values in signals.items() :
        # Convert signal to numpy array
        values = np.array(values)

        # Calculate the mean value
        mean = np.mean(values)

        # Calculate the standard deviation
        std = np.std(values)

        # Calculate the minimum value
        min_ = np.min(values)

        # Calculate the maximum value
        max_ = np.max(values)

        # Calculate the range
        range_ = np.ptp(values)

        signalInfos[key] = {"mean": mean, "std": std, "min": min_, "max": max_, "range": range_}

    return signalInfos

class GraphWidget(QWidget):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent, Qt.WindowType.Widget)

        self.__initUi()

    def __initUi(self):
        # Init style
        mplstyle.use('fast')

        # Init figure
        self.figure = Figure()
        
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Init layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.setStretch(1, 1)

        # Set layout
        self.setLayout(layout)

    def setCursorPosition(self, x: float, y: float):
        self.annot.xy = (x,y)
        text = "({:.2g}, {:.2g})".format(x,y)
        self.annot.set_text(text)
        self.annot.set_visible(True)
        self.canvas.draw()

    def plot(self, x: List[float], y: Dict[str, List[float]], 
            xLabel: str = "Time [s]", yLabel: str = ""):
        # Clear the figure
        self.figure.clear()
        
        # Create sub plot
        ax = self.figure.add_subplot(111)

        # Enable grid
        ax.grid(True)
        
        # Set labels
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)

        # Plot data
        for key, values in y.items() :
            ax.plot(x, values, label=key)

        # Set legend
        ax.legend(loc="upper right")

        # Init the cursor
        cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color = 'r', linewidth = 1)
        self.annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox=dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
        self.annot.set_visible(False)

        # Draw the canvas
        self.canvas.draw()

class SignalInformationsWidget(QWidget):

    def __init__(self, signals: Dict[str, List[float]], parent: Optional[QWidget] = None) -> None:
        super().__init__(parent, Qt.WindowType.Widget)

        # Extract informations
        self.__signalsInfos: Dict[str, Dict[str, float]] = identifySignal(signals)

        self.__initUi()

    def __initUi(self):
        # Minimum size
        self.setMinimumWidth(300)

        # Init layout
        layout = QFormLayout()

        for signalName, signalInfos in self.__signalsInfos.items():
            layout.addRow(signalName, QLabel(""))
            layout.addRow("Mean", QLabel(str(signalInfos["mean"])))
            layout.addRow("Standard Deviation", QLabel(str(signalInfos["std"])))
            layout.addRow("Minimum", QLabel(str(signalInfos["min"])))
            layout.addRow("Maximum", QLabel(str(signalInfos["max"])))
            layout.addRow("Range", QLabel(str(signalInfos["range"])))
            layout.addRow("", QLabel())

        # Create a scroll area
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(QWidget())
        scrollArea.widget().setLayout(layout)

        # Set layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)


class GraphDialog(QDialog):

    def __init__(self, box: Box, parent = None):
        super().__init__(parent, Qt.WindowType.Window)

        # Save box
        self.__box = box

        # Init UI
        self.__initUi()

    def __initUi(self):
        # Set Window title
        self.setWindowTitle(str(self.__box.index) + '-' +  str(self.__box['title']))

        # Create Graph Widget
        self.graphWidget = GraphWidget()
        self.graphWidget.canvas.mpl_connect('button_press_event', self.onclick)

        # Create Signal Informations Widget
        self.signalInformationsWidget = SignalInformationsWidget(self.__box["data_y"])

        # Init splitter
        self.splitter = QSplitter()
        self.splitter.addWidget(self.graphWidget)
        self.splitter.addWidget(self.signalInformationsWidget)

        # Init layout
        layout = QHBoxLayout()
        layout.addWidget(self.splitter)

        # Set layout
        self.setLayout(layout)

        # Set the layout
        self.graphWidget.plot(self.__box['data_x'], self.__box['data_y'], self.__box['label_x'], self.__box['label_y'])

    def onclick(self, event: MouseEvent):
        if event.xdata is not None and isinstance(event.xdata, numbers.Number):
            # Get the closest time value
            i, x = _closest(event.xdata, self.__box['data_x'])

            # Get the closest y value
            _, y = _closest(event.ydata, [values[i] for values in self.__box['data_y'].values()])

            # Set cursor position
            print(x, y)
            self.graphWidget.setCursorPosition(x, y)

if __name__ == '__main__':
    import sys
    import numpy as np
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # Generate box with data
    box = Box(0, "GraphBox", "Boxes.sink")
    box['title'] = "Test"
    box['label_x'] = "Time [s]"
    box['label_y'] = "Value"
    box['data_x'] = np.arange(0, 5, 0.01)
    box['data_y'] = {f"Serie {i}": np.sin(2 * np.pi * box['data_x'] * i) for i in range(1, 10)}
    box['point_count'] = 5


    dialog = GraphDialog(box)
    dialog.show()

    sys.exit(app.exec())