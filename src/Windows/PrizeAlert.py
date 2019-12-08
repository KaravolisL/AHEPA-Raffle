from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from threading import Timer
import time

from Windows.WindowBase import WindowBase
from FileManager.DataParser import dataParser
from Signals import Signals

class PrizeAlert(WindowBase):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.background_color, self.delay, self.font_size = dataParser.getPrizeAlertPrefs()
        self.makeLayout()

        Signals.getInstance().prizeAlertChanged.connect(self.reinit)

    def makeLayout(self):
        """
        Adds and styles the description to the alert
        """
        self.desc = QLabel()
        self.desc.setAlignment(Qt.AlignCenter)
        self.desc.setFont(QFont("Arial", self.font_size))
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
