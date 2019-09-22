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

# def add(input):
#     ''' Method to add a ticket to the drawnList and update the ticket's number drawn field '''
#     if (type(input) is Cell):
#         input = swap(input)
#     drawnList.append(input)
#     input.setNumberDrawn(len(drawnList))

# def remove(input):
#     ''' Method to remove a ticket from the drawnList and update the ticket's number drawn field '''
#     if (type(input) is Cell):
#         input = swap(input)
#     input.setNumberDrawn(0)
#     return drawnList.pop(drawnList.index(input))

# def removeTail():
#     ''' Method to remove the tail of the drawnList. Removes a Ticket but swaps it to return a Cell '''
#     return swap(remove(drawnList[-1]))
#     # TODO: Add error checking 

# def swap(input):
#     ''' Method to swap a cell to a ticket or vice versa with it's ticket in the fullList '''
#     if (type(input) is Cell):
#         return fullList[input.getId() - 1]
#     if (type(input) is Ticket):
#         return MainTable.getInstance().getCell(input.getNumber())
#     assert(False), "Invalid input type"

def getHeaderInfo():
    ''' Method to return a list containing the three numbers for the header '''
    ticketsRemaining = NUMBER_OF_TICKETS - len(drawnList)
    ticketsDrawn = len(drawnList)
    lastTicket = 0 if not hasRaffleStarted() else drawnList[-1].getNumber()
    return [ticketsRemaining, ticketsDrawn, lastTicket]