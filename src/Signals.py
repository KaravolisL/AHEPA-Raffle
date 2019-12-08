from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class Signals(QObject):
    instance = None
    colorChanged = pyqtSignal()
    prizeAlertChanged = pyqtSignal()
    def __init__(self):
        super().__init__()

        Signals.instance = self

    @staticmethod
    def getInstance():
        if (Signals.instance is None):
            Signals.instance = Signals()
        return Signals.instance
    