from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase

class AlertBase(WindowBase):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Warning!!')
        self.setWindowModality(Qt.ApplicationModal)
        self.text = text
        self.makeLayout()
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def setSize(self):
        """
        Sizes window to be a seventh of screen width and height 
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/6, screenHeight/7)

    def makeLayout(self):
        """
        Creates the two buttons and label using text defined by subclass
        """
        self.confirmButton = QPushButton('Confirm')
        self.confirmButton.clicked.connect(self.confirmationEvent)

        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        self.label = QLabel(self.text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 11))

        self.layout.addWidget(self.label, 0 , 0, 1, 2)
        self.layout.addWidget(self.confirmButton, 1, 0)
        self.layout.addWidget(self.cancelButton, 1, 1)

    def confirmationEvent(self):
        raise NotImplementedError

    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

    def closeEvent(self, e):
        pass