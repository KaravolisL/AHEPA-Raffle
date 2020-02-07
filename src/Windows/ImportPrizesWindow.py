from PyQt5.QtWidgets import QWidget, QFileDialog

from Windows.WarningBase import WarningBase
from FileManager.FileManager import importPrizeNames
from Prizes.PrizeApi import initializePrizeList

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

class ImportWarningWindow(WarningBase):
    def __init__(self, fname):
        self.fname = fname
        self.text = 'Importing prizes will cause all\n prizes to be overwritten.'
        super().__init__(self.text)

    def confirmationEvent(self):
        prizes = importPrizeNames(self.fname)
        if len(prizes) == 0:
            # TODO: Alert user import failed
            pass
        else:
            # New prizes have been written to data.xml, so reinitialized the list
            initializePrizeList()
        self.close()

