
from Tickets.TicketList import TicketList
import Prizes.PrizeApi as PrizeApi
import FileManager.FileManager as FileManager
from View.MainWindow import MainWindow
from Signals import Signals
from Prizes.PrizeApi import getList

class Raffle():
    def __init__(self):
        # Construct the MainWindow
        mainWindow = MainWindow()

        # Initialize the TicketList
        TicketList.getInstance().initialize()

        # Restore progress
        self.restoreProgress()

        # Initialize the PrizeList
        PrizeApi.initializePrizeList()

        # Show the main window
        mainWindow.showMaximized()

        # Connect additional signals
        Signals().raffleExited.connect(self.saveProgress)
        Signals().restartRaffle.connect(self.restartRaffle)

    def saveProgress(self):
        """
        This method saves the progress of the raffle and any changes made
        to tickets or prizes
        """
        FileManager.saveProgress(TicketList.getInstance().getDrawnTickets())
        FileManager.writePrizes(PrizeApi.getList())
        FileManager.writeTickets(TicketList.getInstance().ticketList)

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

    def restartRaffle(self):
        """
        This method is called when the user clicks the restart option. It replaces all
        the tickets drawn and resets the header.
        """
        while (TicketList.getInstance().hasRaffleStarted() is not False):
            Signals().ticketDrawn.emit(id)