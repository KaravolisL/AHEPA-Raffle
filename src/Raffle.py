"""Module for the backend of the application"""
# from Tickets.TicketList import TicketList
# import Prizes.PrizeApi as PrizeApi
# import FileManager.FileManager as FileManager
# from View.MainWindow import MainWindow
# from Signals import Signals
# from Prizes.PrizeApi import getList

# # Logger import
# from Logger.Logger import logger

# class Raffle():
#     def __init__(self):
#         logger.debug('Raffle initializing')

#         # Initialize the TicketList
#         TicketList.getInstance().initialize()

#         # Construct the MainWindow
#         mainWindow = MainWindow()

#         # Restore progress
#         self.restoreProgress()

#         # Initialize the PrizeList
#         PrizeApi.initializePrizeList()

#         # Show the main window
#         mainWindow.showMaximized()

#         # Connect additional signals
#         Signals().raffleExited.connect(self.saveProgress)
#         Signals().restartRaffle.connect(self.restartRaffle)

#     def saveProgress(self):
#         """
#         This method saves the progress of the raffle and any changes made
#         to tickets or prizes
#         """
#         FileManager.saveProgress(TicketList.getInstance().getDrawnTickets())
#         FileManager.writePrizes(PrizeApi.getList())
#         FileManager.writeTickets(TicketList.getInstance().ticketList)

#     def restoreProgress(self):
#         """
#         This method reads from the save file and updates the raffle to
#         that given point.
#         """
#         removedTickets = FileManager.readSaveFile()
#         if len(removedTickets) == 0:
#             return
#         for id in [ticket.getNumber() for ticket in removedTickets]:
#             Signals().ticketDrawn.emit(id)

#     def restartRaffle(self):
#         """
#         This method is called when the user clicks the restart option. It replaces all
#         the tickets drawn and resets the header.
#         """
#         lastTicketDrawn = TicketList.getInstance().getLastTicketDrawn()
#         while lastTicketDrawn != None:
#             Signals().undoButtonClicked.emit(lastTicketDrawn.number)
#             lastTicketDrawn = TicketList.getInstance().getLastTicketDrawn()

class Raffle:
    """Class to represent the raffle"""
    def __init__(self):
        self.prizes = []
        self.tickets = []

        # Initialize ticket list
        self.num_tickets_drawn = 0
        for i in range(0, 225):
            self.tickets.append(Ticket("", i+1))

        # Initialize prize list
        # prizeDict = readPrizes()
        prize_dict = {}
        for prize_number, prize_description in prize_dict.items():
            self.prizes.append(Prize(prize_number, prize_description))

class Prize:
    """Class to represent a single prize"""
    def __init__(self, number, description = ""):
        self.number = number
        self.description = description

    def __str__(self):
        return str(self.number) + " " + self.description

class Ticket:
    """Class to represent a single ticket"""
    def __init__(self, name = "", number = 0):
        self.name = name
        self.number = number
        self.number_drawn = 0

    def __str__(self):
        return self.name

    def is_drawn(self) -> bool:
        """Returns whether this ticket has been drawn or not"""
        return self.number_drawn != 0

raffle = Raffle()