from Cell import Cell

''' Contains the list of names read from "ticketNames.txt" on start up 
or from a file provided by the user '''
fullList = []

''' Contains the tickets in the order they are drawn in the raffle '''
drawnList = []

def hasRaffleStarted():
    ''' Convenience method to determine whether drawnList is empty or not '''
    return len(drawnList) != 0

def add(input):
    ''' Method to add a ticket to the drawnList and update the ticket's number drawn field '''
    if (type(input) is Cell):
        input = correlate(input)
    drawnList.append(input)
    input.setNumberDrawn(len(drawnList))

def remove(input):
    ''' Method to remove a ticket from the drawnList and update the ticket's number drawn field '''
    if (type(input) is Cell):
        input = correlate(input)
    input.setNumberDrawn(0)
    return drawnList.remove(input)

def correlate(cell):
    ''' Method to correlate a cell with it's ticket in the fullList '''
    return fullList[cell.getId() - 1]