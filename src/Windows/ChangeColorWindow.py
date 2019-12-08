from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from FileManager.DataParser import dataParser
from Signals import Signals

class ChangeColorWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Change Background Color')

        self.makeLayout()
        self.setColorLabels()

    def makeLayout(self):
        """
        Makes four labels, two being used to display colors
        """
        self.headerColorLabel = QLabel('Header Color: ')
        self.headerColorLabel.setAlignment(Qt.AlignCenter)
        self.headerColorLabel.setMaximumHeight(35)
        self.headerColor = ClickableLabel()
        self.headerColor.setAlignment(Qt.AlignCenter)
        self.headerColor.setMaximumHeight(35)
        self.headerColor.clicked.connect(lambda: self.showColorPicker('header'))

        self.mainTableColorLabel = QLabel('Main Table Color: ')
        self.mainTableColorLabel.setAlignment(Qt.AlignCenter)
        self.mainTableColorLabel.setMaximumHeight(35)
        self.mainTableColor = ClickableLabel()
        self.mainTableColor.setAlignment(Qt.AlignCenter)
        self.mainTableColor.setMaximumHeight(35)
        self.mainTableColor.clicked.connect(lambda: self.showColorPicker('mainTable'))

        self.layout.addWidget(self.headerColorLabel, 0, 0)
        self.layout.addWidget(self.headerColor, 0, 1)
        self.layout.addWidget(self.mainTableColorLabel, 1, 0)
        self.layout.addWidget(self.mainTableColor, 1, 1)

    def setColorLabels(self):
        """
        
        """
        # Get all colors from data file
        self.headerColorInHex = dataParser.getColor('header')
        self.mainTableColorInHex = dataParser.getColor('mainTable')

        self.headerColor.setStyleSheet('QLabel {background-color: ' + self.headerColorInHex + ';}' +
                                       'QLabel:hover {border: 2px solid black;}')
        self.mainTableColor.setStyleSheet('QLabel {background-color: ' + self.mainTableColorInHex + ';}' +
                                          'QLabel:hover {border: 2px solid black;}')

    def showColorPicker(self, element):
        """
        
        """
        color = QColorDialog.getColor()
        if color.isValid():
            dataParser.setColor(element, color.name())
            self.setColorLabels()
            Signals.getInstance().colorChanged.emit()
            
    def setSize(self):
        """
        Sizes window to be 1/5 width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/4, screenHeight/5)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent = None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()
