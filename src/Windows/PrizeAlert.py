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

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.delayThread = Timer(PrizeAlert.DELAY, self.close)
        self.delayThread.start()

    def mousePressEvent(self, QMouseEvent):
        self.close()

    def keyPressEvent(self, e):
        self.close()