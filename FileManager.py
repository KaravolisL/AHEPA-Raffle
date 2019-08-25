# TODO: Add support for csv/excel files

import RaffleList
from Ticket import Ticket

def readTickets(file):
    ''' Rewrites the nameList using the give file '''
    RaffleList.fullList.clear()
    namesFile = open(file, "r")
    for i in range(1, 226):
        RaffleList.fullList.append(Ticket(namesFile.readline(), i))
    namesFile.close()

def restoreProgress():
    pass

def saveProgress(file = None):
    if (file is None):
        saveFile = open("saveFile.txt", "w")
        for ticket in RaffleList.drawnList:
            saveFile.write(str(ticket))
        saveFile.close()
    else:
        # Hook to add save feature
        pass
        