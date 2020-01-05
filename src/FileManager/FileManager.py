# TODO: Add support for csv/excel files
from FileManager.DataParser import dataParser

def readTicketNames(file = 'ticketNames.txt'):
    """
    Reads ticket names from a given file and returns them in a list.
    Catches expection for nonexistent file.
    :param str file: File from which to read
    :returns: list of names
    :rtype: list
    """
    names = dataParser.readTickets()
    while len(names) < 225:
        names.append('')
    return names

def importTicketNames(file):
    """
    Reads ticket names from a give file. Overwrites the current ticket names in
    data.xml and returns a list of the names
    :param str file: File from which to read
    :returns: List of names from given file
    :rtype: list
    """
    # TODO: Add handling for more file formats
    names = []
    namesFile = open(file, 'r')
    for i in range(0, 225):
        names.append(namesFile.readline().strip('\n'))
    namesFile.close()
    dataParser.writeTickets(names)
    return names

def importPrizeNames(file):
    """
    Reads prizes from a given file. Overwrites the current prizes in data.xml
    :param str file: File from which to read prizes
    :returns: Dictionary formatted as {prizeNumber : description}
    :rtype: dict
    """
    # TODO: Add handling for more file formats
    prizes = {}
    try:
        prizeFile = open(file, 'r')
    except:
        print('{} not found'.format(file))
    else:
        for line in prizeFile:
            number, desc = line.split(' ', 1)
            prizes[int(number)] = desc.strip('\n')
        prizeFile.close()
        dataParser.writePrizes(prizes)
    return prizes

def readPrizes(file = 'prizeInfo.txt'):
    """
    Reads prize info from a given file and returns Prizes in a list.
    Catches exception for nonexistent file.
    :param str file: File from which to read
    """
    return dataParser.readPrizes()

def readSaveFile():
    """
    Read the ids stored in a save file. Exceptions are caught for nonexistent
    and poorly formatted save files.
    """
    return dataParser.readSaveData()

def saveProgress(tickets, file = None):
    """
    Takes given tickets and writes it to a blank save file
    :param list tickets: List of tickets to be saved
    :param str file: File to save to
    """
    dataParser.writeSaveData(tickets)

def writeTickets(tickets):
    """
    
    """
    dataParser.writeTickets([ticket.name for ticket in tickets])

def writePrizes(prizes):
    """
    
    """
    dataParser.writePrizes(prizes)
