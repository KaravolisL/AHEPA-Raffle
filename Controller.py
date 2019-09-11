from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class Controller:
    @staticmethod
    def notifyCellRemoved(id):
        print("Cell #" + str(id) + " has been removed.\n")

    @staticmethod
    def initialize():
        print("Raffle initializing...")