from PyQt5.QtWidgets import QWidget, QFileDialog

from Windows.WarningBase import WarningBase
from Tickets.TicketList import TicketList
from Signals import Signals

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

class ImportWarningWindow(WarningBase):
    def __init__(self, fname):
        self.fname = fname
        self.text = 'Importing tickets will cause all progress\n to be lost and ticket names to be overwritten.'
        super().__init__(self.text)

    def confirmationEvent(self):
        """
        Handles the event of the user confirming raffle restart. Note: Raffle must be restarted first
        before reinitializing the TicketList with new names.
        """
        Signals().restartRaffle.emit()
        TicketList.getInstance().reinitialize(self.fname)
        for ticket in TicketList.getInstance().ticketList:
            Signals().ticketNameChanged.emit(ticket.number)
        self.close()
