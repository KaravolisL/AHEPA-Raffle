"""Module for the backend of the application"""

from typing import List
from PyQt5.QtCore import QObject, pyqtSignal

from constants import NUMBER_OF_TICKETS

from debug_logger import get_logger
logger = get_logger(__name__)

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

class Prize:
    """Class to represent a single prize"""
    def __init__(self, number, description = ""):
        self._number = number
        self._description = description
        self.signals = Signals()

    @property
    def number(self):
        """Returns the number property"""
        return self._number

    @number.setter
    def number(self, val: int):
        self._number = val
        self.signals.dataChanged.emit()

    @property
    def description(self):
        """Returns the description property"""
        return self._description

    @description.setter
    def description(self, val: str):
        self._description = val
        self.signals.dataChanged.emit()

    def __str__(self):
        return str(self.number) + " " + self.description

class Ticket:
    """Class to represent a single ticket"""
    def __init__(self, name = "", number = 0):
        self._name = name
        self._number = number
        self._number_drawn = 0
        self.signals = Signals()

    @property
    def name(self):
        """Returns the number property"""
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val
        self.signals.dataChanged.emit()

    @property
    def number(self):
        """Returns the number property"""
        return self._number

    @number.setter
    def number(self, val: int):
        self._number = val
        self.signals.dataChanged.emit()

    @property
    def number_drawn(self):
        """Returns the description property"""
        return self._number_drawn

    @number_drawn.setter
    def number_drawn(self, val: int):
        self._number_drawn = val
        self.signals.dataChanged.emit()

    def __str__(self):
        return str(self.number) + '\n' + self.name

    def is_drawn(self) -> bool:
        """Returns whether this ticket has been drawn or not"""
        return self.number_drawn != 0

class Raffle:
    """Class to represent the raffle"""
    def __init__(self):
        self._prizes: List[Prize] = []
        self._tickets: List[Ticket] = []
        self.signals = Signals()

        # Initialize ticket list
        self.num_tickets_drawn = 0
        for i in range(0, NUMBER_OF_TICKETS):
            self.tickets.append(Ticket("", i + 1))

        # Initialize prize list
        # prizeDict = readPrizes()
        prize_dict = {}
        for prize_number, prize_description in prize_dict.items():
            self.prizes.append(Prize(prize_number, prize_description))

    @property
    def prizes(self):
        """Returns the list of prizes"""
        return self._prizes

    @prizes.setter
    def prizes(self, val: List[Prize]):
        self._prizes = val
        self.signals.dataChanged.emit()

    @property
    def tickets(self):
        """Returns the list of tickets"""
        return self._tickets

    @tickets.setter
    def tickets(self, val: List[Ticket]):
        self._tickets = val
        self.signals.dataChanged.emit()

    def draw_ticket(self, ticket_number) -> None:
        """Sets the given ticket's number_drawn field and increments num_tickets_drawn
        :param int ticket_number: Number of ticket to remove
        """
        assert not self.tickets[ticket_number - 1].is_drawn(), 'Ticket already removed'
        logger.debug('Removing ticket number %d', ticket_number)
        self.num_tickets_drawn += 1
        self.tickets[ticket_number - 1].number_drawn = self.num_tickets_drawn

    def replace_ticket(self) -> None:
        """Replaces the last drawn ticket"""
        last_ticket_drawn = self.get_last_ticket_drawn()
        assert last_ticket_drawn is not None, 'No tickets have been drawn'
        assert last_ticket_drawn.is_drawn(), 'Ticket has not been drawn'
        logger.debug('Replacing ticket number %d', last_ticket_drawn.number)
        self.num_tickets_drawn -= 1
        self.tickets[last_ticket_drawn.number - 1].number_drawn = 0

    def restart(self):
        """This method replaces all drawn tickets"""
        while self.num_tickets_drawn != 0:
            self.replace_ticket()

    def get_last_ticket_drawn(self) -> Ticket:
        """Iterates the list and compares each ticket's number_drawn field
        :returns: Returns the last ticket drawn, None if no tickets have been drawn
        :rtype: Ticket
        """
        if self.num_tickets_drawn != 0:
            for ticket in self.tickets:
                if ticket.number_drawn == self.num_tickets_drawn:
                    return ticket
            assert False, "Corresponding ticket not found"
        return None

class Signals(QObject):
    """Class to hold signals"""
    dataChanged = pyqtSignal()

raffle = Raffle()
