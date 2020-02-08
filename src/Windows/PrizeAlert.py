from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# System Libraries
from threading import Timer
import time

from Windows.WindowBase import WindowBase
from FileManager.DataParser import dataParser
from Signals import Signals

class PrizeAlert(WindowBase):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.background_color, self.delay, self.font_size = dataParser.getPrizeAlertPrefs()
        self.makeLayout()

        Signals().prizeAlertChanged.connect(self.reinit)

        self.setSizeAndCenter()

    def makeLayout(self):
        """
        Adds and styles the description to the alert
        """
        self.desc = QLabel(self)
        self.desc.setAlignment(Qt.AlignCenter)
        self.desc.setFont(QFont("Arial", self.font_size))
        self.desc.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.desc.setWordWrap(True)
        self.desc.setMinimumSize(self.sizeHint())
        self.layout.addWidget(self.desc)

        # Set the background color from preferences
        self.setStyleSheet('QWidget {background-color: ' + self.background_color +  ';}')

    def setPrize(self, prize):
        """
        Displays the prize's info in the alert
        :param Prize prize: prize for which the alert is
        """
        self.desc.setText(prize.description)

    def reinit(self):
        """
        
        """
        self.background_color, self.delay, self.font_size = dataParser.getPrizeAlertPrefs()
        self.desc.setFont(QFont("Arial", self.font_size))
        self.setStyleSheet('QWidget {background-color: ' + self.background_color +  ';}')

    def mousePressEvent(self, QMouseEvent):
        self.close()

    def keyPressEvent(self, e):
        self.close()

    def show(self):
        super().show()
         # Start a timer for closing the PrizeAlert
        self.delayThread = Timer(self.delay, self.close)
        self.delayThread.start()
