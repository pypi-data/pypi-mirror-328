from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QWidget
from PyQt6.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs

PythonKeywords = [
    "from",
]

class MuphynPythonLexer(QsciLexerPython):
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)

        self.setColor(Qt.GlobalColor.darkBlue, QsciLexerPython.Keyword)
        self.setColor(QColor(13, 152, 186), QsciLexerPython.Default)
        self.setColor(Qt.GlobalColor.darkGreen, QsciLexerPython.Comment)
        self.setColor(Qt.GlobalColor.darkGreen, QsciLexerPython.CommentBlock)
        self.setColor(Qt.GlobalColor.darkRed, QsciLexerPython.DoubleQuotedString)
        self.setColor(Qt.GlobalColor.darkRed, QsciLexerPython.DoubleQuotedFString)
        self.setColor(Qt.GlobalColor.darkRed, QsciLexerPython.SingleQuotedString)
        self.setColor(Qt.GlobalColor.darkRed, QsciLexerPython.SingleQuotedFString)
        self.setColor(Qt.GlobalColor.red, QsciLexerPython.UnclosedString)
        self.setColor(QColor(148, 0, 211), QsciLexerPython.Number)
        self.setColor(Qt.GlobalColor.black, QsciLexerPython.Operator)

        font = QFont("DejaVu sans Mono")
        font.setFixedPitch(True)
        self.setFont(font)


class CodeEditor(QsciScintilla):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        # Set End of line (EOL)
        self.setEolMode(QsciScintilla.EolMode.EolWindows)

        # Set Utf 8
        self.setUtf8(True)

        # Wrap mode
        self.setWrapMode(QsciScintilla.WrapMode.WrapNone)

        # Indentation
        self.setIndentationsUseTabs(False) # indent = whitespaces
        self.setTabWidth(4) # 4 withspaces
        self.setIndentationGuides(True)
        self.setTabIndents(True) # Indent next non-whitespace character to next tab
        self.setAutoIndent(True) # Next line start at the same indent as previous line

        # Caret
        self.setCaretForegroundColor(QColor(219, 125, 40))
        self.setCaretWidth(2) # Caret width
        self.setCaretLineVisible(True) # Current line background visible
        self.setCaretLineBackgroundColor(QColor(255, 247, 239)) # Current line background color

        # Margins
        self.setMargins(1)

        ## Line number margin
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, '0' * 7)
        
        # Lexer
        self._lexer = MuphynPythonLexer(self)
        self.setLexer(self._lexer)

        # Auto completion
        self._apis = QsciAPIs(self._lexer)
        for keyword in PythonKeywords:
            self._apis.add(keyword)
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)


