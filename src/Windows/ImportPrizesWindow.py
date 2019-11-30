from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.AlertBase import AlertBase
from FileManager.FileManager import importPrizeNames

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
        self.text = 'Importing prizes will cause all\n prizes to be overwritten.'
        super().__init__(self.text)

    def confirmationEvent(self):
        prizes = importPrizeNames(self.fname)
        # TODO: Do something with these prizes
        self.close()

