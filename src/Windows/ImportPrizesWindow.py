from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.AlertBase import AlertBase
import Controller
import FileManager
import RaffleList

class ImportPrizesWindow(QWidget):
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
        self.text = 'Fill in later'
        super().__init__(self.text)

    def confirmationEvent(self):
        self.close()

