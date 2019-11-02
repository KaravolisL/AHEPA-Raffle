# TODO: Modify Ticket class to include a drawn boolean then remove drawnList

import Controller
from Ticket import Ticket
from GlobalConstants import NUMBER_OF_TICKETS

''' Contains the list of tickets read from "ticketNames.txt" on start up 
or from a file provided by the user '''
fullList = []

''' Contains the tickets in the order they are drawn in the raffle '''
drawnList = []

def hasRaffleStarted():
    ''' Convenience method to determine whether drawnList is empty or not '''
    return len(drawnList) != 0

def fullListInit(names):
    ''' Clears fullList then fills it with Tickets made using names provided '''
    fullList.clear()
    for i in range(0, 225):
        fullList.append(Ticket(names[i], i+1))
    Controller.Controller.notifyTicketNameChange(fullList)

def getLastTicketDrawn():
    ''' Method to get the last ticket drawn '''
    return None if not hasRaffleStarted() else drawnList[-1]

def appendTicket(cellNumber):
    ''' Method to add a ticket from the fullList to the end of the drawnList given it's number '''
    drawnList.append(fullList[cellNumber-1])

def pop():
    ''' 
    Pops the last ticket off of the drawnList 
    :returns: Last ticket drawn
    :rtype: Ticket
    '''
    return drawnList.pop() if hasRaffleStarted() else None

def hasTicketBeenPulled(cellNumber):
    ''' Checks if a ticket is in the drawnList '''
    return not fullList[cellNumber-1] in drawnList

def getHeaderInfo():
    ''' Method to return a list containing the three numbers for the header '''
    ticketsRemaining = NUMBER_OF_TICKETS - len(drawnList)
    ticketsDrawn = len(drawnList)
    lastTicket = 0 if getLastTicketDrawn() is None else getLastTicketDrawn().getNumber()
    return [ticketsRemaining, ticketsDrawn, lastTicket]