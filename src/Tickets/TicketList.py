# Local imports
from Tickets.Ticket import Ticket
from FileManager.FileManager import readTicketNames, importTicketNames
from Signals import Signals
from GlobalConstants import NUMBER_OF_TICKETS

# Logging import
from Logger.Logger import logger

class TicketList():
    instance = None
    ticketList = []

    def __init__(self):

        assert(TicketList.instance == None) # Assert to ensure singleton
        TicketList.instance = self
        self.numOfTicketsDrawn = 0

        # Connect signals for removing and replacing tickets
        Signals().ticketDrawn.connect(self.removeTicket)
        Signals().undoButtonClicked.connect(self.replaceTicket)

    @staticmethod
    def getInstance():
        return TicketList.instance if TicketList.instance != None else TicketList()

    # TODO: Combine initialize methods
    def initialize(self):
        """
        Initializes the ticket list
        """
        self.ticketList.clear()
        self.numOfTicketsDrawn = 0
        ticketNames = readTicketNames()
        for i in range(0, 225):
            self.ticketList.append(Ticket(ticketNames[i], i+1))

    def reinitialize(self, file):
        """
        Reinitializes the ticket list using names from a given file
        :param str file: File from which to get ticket names
        """
        self.ticketList.clear()
        self.numOfTicketsDrawn = 0
        ticketNames = importTicketNames(file)
        for i in range(0, 225):
            self.ticketList.append(Ticket(ticketNames[i], i+1))

    def hasRaffleStarted(self):
        """
        Convenience method to determine whether ticketList is empty or not
        :returns: Whether any tickets have been drawn
        :rtype: bool
        """
        return self.numOfTicketsDrawn != 0

    def getLastTicketDrawn(self):
        """
        Iterates the list and compares each ticket's numberDrawn field
        :returns: Returns the last ticket drawn, None if no tickets have been drawn
        :rtype: Ticket
        """
        if self.numOfTicketsDrawn != 0:
            for ticket in self.ticketList:
                if ticket.numberDrawn == self.numOfTicketsDrawn:
                    return ticket
        else:
            return None

    def removeTicket(self, ticketNumber):
        """
        Sets the given tickets numberDrawn field and increments numOfTicketsDrawn
        :param int ticketNumber: Number of ticket to remove
        """
        assert(self.ticketList[ticketNumber - 1].isDrawn() is False), 'Ticket already removed'
        logger.debug('Removing ticket number {}'.format(ticketNumber))
        self.ticketList[ticketNumber - 1].numberDrawn = self.numOfTicketsDrawn + 1
        self.numOfTicketsDrawn += 1

    def replaceTicket(self):
        """
        Sets the last ticket drawn's numberDrawn field and decrements numOfTicketsDrawn
        """
        ticket = self.getLastTicketDrawn()
        assert(ticket != None), 'No tickets have been drawn'
        assert(ticket.isDrawn()), 'Ticket has not been drawn'
        logger.debug('Replacing ticket number {}'.format(ticket.number))
        self.ticketList[ticket.number - 1].numberDrawn = 0
        self.numOfTicketsDrawn -= 1

    def hasTicketBeenDrawn(self, ticketNumber):
        """
        Determines whether a given ticket has been drawn or not
        :param int ticketNumber: Number of ticket to investigate
        :returns: Whether ticket has been drawn or not
        :rtype: bool
        """
        return self.ticketList[ticketNumber - 1].isDrawn()

    def getHeaderInfo(self):
        """
        Determines the information for the header
        :returns: list containing header information
        :rtype: list
        """
        ticketsRemaining = NUMBER_OF_TICKETS - self.numOfTicketsDrawn
        lastTicket = 0 if self.getLastTicketDrawn() is None else self.getLastTicketDrawn().number
        return [ticketsRemaining, self.numOfTicketsDrawn, lastTicket]

    def getDrawnTickets(self):
        """
        Obtains a list of tickets that have been drawn
        :returns: List of tickets that were drawn
        :rtype: list
        """
        drawnTickets = []
        for ticket in self.ticketList:
            if ticket.isDrawn():
                drawnTickets.append(ticket)
        return drawnTickets

    def getTicket(self, number):
        """
        Gets a ticket from the ticketList given a number
        :param int number: number of ticket
        :returns: ticket with given number
        :rtype: Ticket
        """
        assert(number > 0 and number < 226)
        return self.ticketList[number - 1]

    def setTicketName(self, number, newName):
        """
        Changes the name of the ticket with the give number
        :param int number: Number of the ticket
        :param str newName: New name for the ticket
        """
        assert(number > 0 and number < 226)
        self.ticketList[number -1].name = newName
