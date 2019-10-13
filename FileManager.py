# TODO: Add support for csv/excel files

def readTicketNames(file = 'ticketNames.txt'):
    """
    Reads ticket names from a given file and returns them in a list.
    Catches expection for nonexistent file.
    :param str file: File from which to read
    """
    names = []
    try:
        namesFile = open(file, 'r')
    except:
        print('{} not found'.format(file))
        for i in range(0, 225):
            names.append('')
    else:
        for i in range(0, 225):
            names.append(namesFile.readline())
        namesFile.close()
    return names

def readSaveFile(file = 'saveFile.txt'):
    """
    Read the ids stored in a save file. Exceptions are caught for nonexistent
    and poorly formatted save files.
    :param str file: Save file from which to read
    """
    ids = []
    try:
        saveFile = open(file, 'r')
    except:
        print('{} not found'.format(file))
    else:
        try:
            for line in saveFile:
                ids.append(int(line))
        except:
            print('{} is corrupted'.format(file))
        saveFile.close()
    return ids

def saveProgress(tickets, file = None):
    """
    Takes given tickets and writes it to a blank save file
    :param list tickets: List of tickets to be saved
    :param str file: File to save to
    """
    if (file is None):
        saveFile = open("saveFile.txt", "r+")
        saveFile.truncate(0)
        for ticket in tickets:
            saveFile.write(str(ticket.getNumber()) + '\n')
        saveFile.close()
    else:
        # Hook to add save feature
        pass
