from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class WindowBase(QWidget):
    def __init__(self):
        super().__init__()

        self.setSize()

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.makeLayout()

        self.center()

    def center(self):
        """
        Used to center window in middle of screen
        """
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def setSize(self):
        """
        Sizes window to be half of screen width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/2, screenHeight/2)

    def makeLayout(self):
        raise NotImplementedError