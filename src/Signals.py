from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Utils.Singleton import Singleton

@Singleton
class Signals(QObject):
    colorChanged = pyqtSignal()
    prizeAlertChanged = pyqtSignal()
    ticketDrawn = pyqtSignal(int)
    ticketNameChanged = pyqtSignal(int)
    prizeChanged = pyqtSignal(int)
    