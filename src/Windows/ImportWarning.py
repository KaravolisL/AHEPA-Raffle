
from Windows.AlertBase import AlertBase
import FileManager
import RaffleList
import Controller

class ImportWarningWindow(AlertBase):
    def __init__(self, fname):
        self.fname = fname
        self.text = 'Fill in later'
        super().__init__(self.text)

    def confirmationEvent(self):
        newNames = FileManager.readTicketNames(self.fname)
        RaffleList.fullListInit(newNames)
        Controller.restartRaffle()
        self.close()