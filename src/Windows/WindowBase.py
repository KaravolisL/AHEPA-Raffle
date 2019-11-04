from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class WindowBase(QWidget):
    def __init__(self):
        super().__init__()

        # Set size and center
        self.setSize()
        self.center()

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Setting window icon
        self.setWindowIcon(QIcon(r'..\images\Icon.jpg'))

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
        Sizes window to be 1/1.5 width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/1.5, screenHeight/1.5)

    def makeLayout(self):
        raise NotImplementedError