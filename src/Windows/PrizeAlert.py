from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from threading import Timer
import time

from Windows.WindowBase import WindowBase

class PrizeAlert(WindowBase):
    DELAY = 8
    FONT_SIZE = 16

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.makeLayout()

        # Start a timer for closing the PrizeAlert
        self.delayThread = Timer(PrizeAlert.DELAY, self.close)
        self.delayThread.start()

    def makeLayout(self):
        """
        Adds and styles the description to the alert
        """
        self.desc = QLabel()
        self.desc.setAlignment(Qt.AlignCenter)
        self.desc.setFont(QFont("Arial", PrizeAlert.FONT_SIZE))
        self.layout.addWidget(self.desc)

    def setPrize(self, prize):
        """
        Displays the prize's info in the alert
        :param Prize prize: prize for which the alert is
        """
        self.desc.setText(prize.description)

    def mousePressEvent(self, QMouseEvent):
        self.close()

    def keyPressEvent(self, e):
        self.close()