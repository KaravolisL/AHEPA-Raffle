from PyQt5.QtCore import QObject
from PyQt5.Qt import pyqtSignal

from Utils.Singleton import Singleton

@Singleton
class Signals(QObject):
    colorChanged = pyqtSignal()
    prizeAlertChanged = pyqtSignal()
    ticketDrawn = pyqtSignal(int)
    ticketNameChanged = pyqtSignal(int)
    prizeChanged = pyqtSignal(int)
    undoButtonClicked = pyqtSignal(int)
    raffleExited = pyqtSignal()
    raffleInitialized = pyqtSignal()
    restartRaffle = pyqtSignal()