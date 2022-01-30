import sys
from Pyqt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Label(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 20px;")


class TextWindow(QWidget):
    def __init__(self, label=None, parent=None):
        if font is not instanceof(QLabel):
            raise Exception("font must be a QLabel")

        super().__init__(parent)
        self.setWindowTitle("Schdule Manager")
        self.setGeometry(100, 100, 300, 200)
        self.label = label


def main():
    app = QApplication(sys.argv)
    newWindow = TextWindow(QLabel("Hello World"))
    newWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
