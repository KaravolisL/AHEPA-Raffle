from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase

class AlertBase(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)

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
        self.confirmButton = QPushButton('Confirm')
        self.confirmButton.clicked.connect(self.confirmationEvent)
        self.layout.addWidget(QLabel('TestTestTest'), 0 ,0)
        self.layout.setColumnStretch(0, 2)
        self.layout.addWidget(self.confirmButton, 1, 0)
        self.layout.addWidget(QPushButton('Cancel'), 1, 1)

    def confirmationEvent(self):
        raise NotImplementedError

    def rejectEvent(self):
        raise NotImplementedError

    def closeEvent(self, e):
        raise NotImplementedError