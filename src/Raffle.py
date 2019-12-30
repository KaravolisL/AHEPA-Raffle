
from Tickets.TicketList import TicketList
import Prizes.PrizeApi as PrizeApi
import FileManager.FileManager as FileManager
from View.MainWindow import MainWindow
from Signals import Signals

class Raffle():
    def __init__(self):

        # Initialize the TicketList
        TicketList.getInstance().initialize()

        # Restore progress
        self.restoreProgress()

        # Initialize the PrizeList
        PrizeApi.initializePrizeList()

        # Construct MainWindow and show
        mainWindow = MainWindow()
        mainWindow.showMaximized()

    def restoreProgress(self):
        """
        This method reads from the save file and updates the raffle to
        that given point.
        """
        removedTickets = FileManager.readSaveFile()
        if len(removedTickets) == 0:
            return
        for id in [ticket.getNumber() for ticket in removedTickets]:
            Signals().ticketDrawn.emit(id)