from Ticket import Ticket
from FileManager import readTicketNames
from Controller import notifyTicketNameChange
from GlobalConstants import NUMBER_OF_TICKETS

class TicketList():
    instance = None
    ticketList = []

    def __init__(self):

        assert(self.instance == None) # Assert to ensure singleton
        
        self.instance = self
        self.numOfTicketsDrawn = 0

    @staticmethod
    def getInstance():
        return TicketList.instance if TicketList.instance != None else TicketList()

    def initialize(self):
        """
        Initializes the ticket list
        """
        self.ticketList.clear()
        self.numOfTicketsDrawn = 0
        ticketNames = readTicketNames()
        for i in range(0, 225):
            self.ticketList.append(Ticket(ticketNames[i], i+1))
        notifyTicketNameChange(self.ticketList)

    def hasRaffleStarted(self):
        """
        Convenience method to determine whether ticketList is empty or not 
        :returns: Whether any tickets have been drawn
        :rtype: bool
        """
        for ticket in self.ticketList:
            if ticket.isDrawn():
                return True
    
    def getLastTicketDrawn(self):
        """
        Iterates the list and compares each ticket's numberDrawn field
        :returns: Returns the last ticket drawn
        :rtype: Ticket
        """
        lastTicket = None
        for ticket in self.ticketList:
            if ticket.isDrawn():
                if lastTicket == None:
                    lastTicket = ticket
                elif (ticket.numberDrawn > lastTicket.numberDrawn):
                    lastTicket = ticket
        return lastTicket

    def removeTicket(self, ticketNumber):
        """ 
        Sets the given tickets numberDrawn field and increments numOfTicketsDrawn
        :param int ticketNumber: Number of ticket to remove
        """
        self.ticketList[ticketNumber - 1].numberDrawn = self.numOfTicketsDrawn + 1
        self.numOfTicketsDrawn = self.numOfTicketsDrawn + 1

    def replaceTicket(self):
        """
        Sets the last ticket drawn's numberDrawn field and decrements numOfTicketsDrawn
        :returns: Last ticket drawn
        :rtype: Ticket
        """
        lastTicket = self.getLastTicketDrawn()
        if lastTicket != None:
            self.ticketList[lastTicket.number - 1].numberDrawn = 0
            self.numOfTicketsDrawn = self.numOfTicketsDrawn - 1
        return lastTicket

    def hasTicketBeenDrawn(self, ticketNumber):
        """
        Determines whether a given ticket has been drawn or not
        :param int ticketNumber: Number of ticket to investigate
        :returns: Whether ticket has been drawn or not
        :rtype: bool
        """
        return self.ticketList[ticketNumber - 1].numberDrawn != 0

    def getHeaderInfo(self):
        """
        Determines the information for the header
        :returns: list containing header information
        :rtype: list
        """
        ticketsRemaining = NUMBER_OF_TICKETS - self.numOfTicketsDrawn
        lastTicket = 0 if self.getLastTicketDrawn() is None else self.getLastTicketDrawn().number
        return [ticketsRemaining, self.numOfTicketsDrawn, lastTicket]
