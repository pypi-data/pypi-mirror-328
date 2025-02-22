import matplotlib as mpl

from PyQt6.QtGui import QFont, QImage

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

def generateMathExpression(mathText):
    """This function is not used for the moment
    but can be used as replacement of mathTex_to_QPixmap"""
    figure = Figure(edgecolor=(0, 0, 0), facecolor=(0, 0, 0))
    canvas = FigureCanvasQTAgg(figure)

    # l.addWidget(self._canvas)
    figure.clear()
    text = figure.suptitle(
        mathText,
        x = 0.0,
        y = 1.0,
        horizontalalignment = 'left',
        verticalalignment = 'top',
        size = QFont().pointSize()*2
    )

    #
    canvas.draw()

    (x0,y0),(x1,y1) = text.get_window_extent().get_points()
    w=x1-x0; h=y1-y0

    figure.set_size_inches(w/80, h/80)

def mathTex_to_QImage(mathTex, fs = 40):
    # Enable usetex param for Matplotlib
    textUseTexParam = mpl.rcParams['text.usetex']
    mpl.rcParams['text.usetex'] = True

    #---- set up a mpl figure instance ----

    fig = Figure(edgecolor=(0, 0, 0), facecolor="None")
    canvas = FigureCanvasQTAgg(fig)
    fig.set_canvas(canvas)
    renderer = canvas.get_renderer()

    #---- plot the mathTex expression ----

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs)

    #---- fit figure size to text artist ----

    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)

    text_bbox = t.get_window_extent(renderer)

    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height

    fig.set_size_inches(tight_fwidth, tight_fheight)

    #---- convert mpl figure to QPixmap ----

    buf, size = fig.canvas.print_to_buffer()
    qimage = QImage.rgbSwapped(QImage(buf, size[0], size[1],
        QImage.Format.Format_ARGB32))
    
    # Restore matplotlib useText param
    mpl.rcParams['text.usetex'] = textUseTexParam
    
    return qimage
