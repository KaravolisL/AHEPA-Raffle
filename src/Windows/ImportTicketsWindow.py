from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.AlertBase import AlertBase
import FileManager
import RaffleList
import Controller

class ImportTicketsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.warning = None

    def show(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '', ('Text Files (*.txt)'))[0]
        print(fname)
        if fname == '':
            return
        self.warning = ImportWarningWindow(fname)
        self.warning.show()

class ImportWarningWindow(AlertBase):
    def __init__(self, fname):
        self.fname = fname
        self.text = 'Importing tickets will cause all progress\n to be lost and ticket names to be overwritten.'
        super().__init__(self.text)

    def confirmationEvent(self):
        newNames = FileManager.readTicketNames(self.fname)
        RaffleList.fullListInit(newNames)
        Controller.restartRaffle()
        self.close()
