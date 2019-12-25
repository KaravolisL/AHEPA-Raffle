from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from FileManager.DataParser import dataParser
from Signals import Signals

class EditPrizeAlertWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Prize Alert')

        # Select the current font size
        self.color, self.delay, self.font_size = dataParser.getPrizeAlertPrefs()

        self.makeLayout()
        self.setColorLabel()

    def makeLayout(self):
        """
        Makes four labels, two being used to display colors
        """
        self.prizeAlertColorLabel = QLabel('Prize Alert Color: ')
        self.prizeAlertColorLabel.setAlignment(Qt.AlignCenter)
        self.prizeAlertColorLabel.setMaximumHeight(35)
        self.prizeAlertColor = ClickableLabel()
        self.prizeAlertColor.setAlignment(Qt.AlignCenter)
        self.prizeAlertColor.setMaximumHeight(35)
        self.prizeAlertColor.clicked.connect(lambda: self.showColorPicker('prizeAlert'))

        self.prizeAlertFontSizeLabel = QLabel('Font Size: ')
        self.prizeAlertFontSizeLabel.setAlignment(Qt.AlignCenter)
        self.prizeAlertFontSizeOptions = QComboBox()
        for i in range(2, 37, 2):
            self.prizeAlertFontSizeOptions.addItem(str(i))
        self.prizeAlertFontSizeOptions.setCurrentText(str(self.font_size))

        self.prizeAlertDelayLabel = QLabel('Delay (In seconds): ')
        self.prizeAlertDelayLabel.setAlignment(Qt.AlignCenter)
        self.prizeAlertDelayOptions = QComboBox()
        for i in range(1, 21):
            self.prizeAlertDelayOptions.addItem(str(i))
        self.prizeAlertDelayOptions.setCurrentText(str(self.delay))

        self.confirmButton = QPushButton('Ok')
        self.confirmButton.clicked.connect(self.confirmationEvent)
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.close)

        self.layout.addWidget(self.prizeAlertColorLabel, 0, 0)
        self.layout.addWidget(self.prizeAlertColor, 0, 1)
        self.layout.addWidget(self.prizeAlertFontSizeLabel, 1, 0)
        self.layout.addWidget(self.prizeAlertFontSizeOptions, 1, 1)
        self.layout.addWidget(self.prizeAlertDelayLabel, 2, 0)
        self.layout.addWidget(self.prizeAlertDelayOptions, 2, 1)
        self.layout.addWidget(self.confirmButton, 3, 0)
        self.layout.addWidget(self.cancelButton, 3, 1)

    def setColorLabel(self):
        """
        
        """
        # Get color from data file
        self.prizeAlertColorInHex = dataParser.getColor('prizeAlert')

        self.prizeAlertColor.setStyleSheet('QLabel {background-color: ' + self.prizeAlertColorInHex + ';}' +
                                           'QLabel:hover {border: 2px solid black;}')

    def showColorPicker(self, element):
        """
        
        """
        color = QColorDialog.getColor()
        if color.isValid():
            dataParser.setColor(element, color.name())
            self.setColorLabel()
            
    def setSize(self):
        """
        Sizes window to be 1/5 width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/4, screenHeight/5)

    def closeEvent(self, ev):
        """
        
        """
        Signals().prizeAlertChanged.emit()
        super().closeEvent(ev)

    def confirmationEvent(self):
        """
        
        """
        dataParser.setPrizeAlertPref('delay', self.prizeAlertDelayOptions.currentText())
        dataParser.setPrizeAlertPref('fontSize', self.prizeAlertFontSizeOptions.currentText())
        Signals().prizeAlertChanged.emit()
        self.close()

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent = None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()