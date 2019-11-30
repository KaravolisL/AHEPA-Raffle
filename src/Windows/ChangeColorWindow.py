from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase

class ChangeColorWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Change Background Color')

        self.makeLayout()
        self.initColorLabels()

    def makeLayout(self):
        """
        Makes four labels, two being used to display colors
        """
        self.headerColorLabel = QLabel('Header Color: ')
        self.headerColorLabel.setAlignment(Qt.AlignCenter)
        self.headerColorLabel.setMaximumHeight(25)
        self.headerColor = QLabel()
        self.headerColor.setAlignment(Qt.AlignCenter)
        self.headerColor.setStyleSheet('QLabel {background-color: red;}')
        self.headerColor.setMaximumHeight(25)

        self.mainTableColorLabel = QLabel('Main Table Color: ')
        self.mainTableColorLabel.setAlignment(Qt.AlignCenter)
        self.mainTableColorLabel.setMaximumHeight(25)
        self.mainTableColor = QLabel()
        self.mainTableColor.setAlignment(Qt.AlignCenter)
        self.mainTableColor.setMaximumHeight(25)

        self.layout.addWidget(self.headerColorLabel, 0, 0)
        self.layout.addWidget(self.headerColor, 0, 1)
        self.layout.addWidget(self.mainTableColorLabel, 1, 0)
        self.layout.addWidget(self.mainTableColor, 1, 1)

    def initColorLabels(self):
        self.headerColor.setStyleSheet('QLabel {}')

    def makeAndSetStyleSheet(self):
        """
        Constructs a style sheet using the fields stored in the class and sets it to each widget
        """
        

    def setSize(self):
        """
        Sizes window to be 1/5 width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/5, screenHeight/5)
