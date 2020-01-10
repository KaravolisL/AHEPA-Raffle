import xml.etree.ElementTree as ET
from Tickets.Ticket import Ticket # TODO: Work to get rid of this dependency
from Prizes.Prize import Prize
from Windows.CorruptedFileAlertWindow import CorruptedFileAlertWindow

from Logger.Logger import logger

file = r'FileManager/data.xml'

def fileChecker(func):
    def func_wrapper(*args):
        try:
            return func(*args)
        except:
            DataParser.alertWindow = CorruptedFileAlertWindow()
            DataParser.alertWindow.show()
            logger.debug("Exception caught in {}".format(func.__name__))
            createDefault()
            # Reevaluate function using newly created default save file
            return func(*args)
    return func_wrapper

class DataParser():
    alertWindow = None

    @fileChecker
    def __init__(self):
        self.tree = ET.parse(file)
        self.root = self.tree.getroot() # <data>

    @fileChecker
    def readTickets(self):
        """
        Reads ticket names from data.xml and returns them in a list

        :returns: List of names for all tickets
        :rtype: list
        """
        names = []
        for ticket in self.root.findall('.//ticket'):
            names.append(ticket.get('name'))
        return names

    @fileChecker
    def writeTickets(self, names):
        """
        Clears all tickets from the data file and writes new ones. Uses the order
        of the names for the ids
        :param list names: list of names of tickets
        """
        tickets = self.root.find('.//tickets')
        tickets.clear()
        for i in range(0, len(names)):
            attribs = {'name': names[i], 'id': str(i+1)}
            ET.SubElement(tickets, 'ticket', attribs)
        self.tree.write(file)

    @fileChecker
    def writeSaveData(self, tickets):
        """
        Writes a list of tickets to the save data section of data.xml
        :param list tickets: List of drawn tickets to be saved
        """
        saveData = self.root.find('.//saveData')
        saveData.clear()
        for ticket in tickets:
            ET.SubElement(saveData, 'ticket', ticket.getAttributes())
        self.tree.write(file)

    @fileChecker
    def readSaveData(self):
        """
        Reads the list of tickets from the save data section of data.xml
        :returns: List of tickets from save data
        :rtype: list
        """
        saveData = self.root.find('.//saveData')
        tickets = []
        for ticket in saveData.findall('.//ticket'):
            name = ticket.get('name')
            id = ticket.get('id')
            tickets.append(Ticket(name, int(id)))
        return tickets

    @fileChecker
    def readPrizes(self):
        """
        Reads the prizes from the prizeInfo section of data.xml
        :returns: prizes in the form of a dictionary
        :rtype: dict
        """
        prizeInfo = self.root.find('.//prizeInfo')
        prizes = {}
        for prize in prizeInfo.findall('.//prize'):
            number = prize.get('number')
            description = prize.get('description')
            prizes.update({int(number) : description})
        return prizes

    @fileChecker
    def writePrizes(self, prizes):
        """
        Clears current prize info section and writes given prizes. This function handles either a
        list of prizes represented as dicts or a list of Prize objects.
        :param list prizes: List of prizes represented as dictionaries
        """
        prizeInfo = self.root.find('.//prizeInfo')
        prizeInfo.clear()
        for prize in prizes:
            if type(prize) is Prize:
                ET.SubElement(prizeInfo, 'prize', prize.getAttributes())
            else:
                ET.SubElement(prizeInfo, 'prize', {'number': str(prize), 'description': prizes[prize]})
        if len(prizes) != 0:
            self.tree.write(file)

    @fileChecker
    def getColor(self, forWhat):
        """

        """
        preferences = self.root.find('.//preferences')
        element = preferences.find('.//{}'.format(forWhat))
        color = element.get('color')
        if True: # TODO: Validate color
            return color
        else:
            raise Exception

    @fileChecker
    def setColor(self, forWhat, color):
        """

        """
        preferences = self.root.find('.//preferences')
        element = preferences.find('.//{}'.format(forWhat))
        element.set('color', color)

    @fileChecker
    def getPrizeAlertPrefs(self):
        """

        :warning: preferences are returned in alphabetical order
        """
        prizeAlert = self.root.find('.//prizeAlert')
        attribs = prizeAlert.attrib
        logger.debug('prizeAlert attributes: {}'.format(attribs))
        values = [attribs['color'], int(attribs['delay']), int(attribs['fontSize'])]
        # TODO: Validate color
        return values

    @fileChecker
    def setPrizeAlertPref(self, pref, value):
        """
        :param str pref: Preference to set
        :param str value: Value for preference
        """
        print('Setting {} to be {}'.format(pref, value))
        prizeAlert = self.root.find('.//prizeAlert')
        prizeAlert.set(pref, value)

def createDefault():
    """
    In the case of a corrupted data file, this function will create a default
    blank one.
    """
    data = ET.Element('data')
    preferences = ET.SubElement(data, 'preferences')
    header = ET.SubElement(preferences, 'header', {'color': '#6699ff'})
    mainTable = ET.SubElement(preferences, 'mainTable', {'color': '#6699ff'})
    prizeAlert = ET.SubElement(preferences, 'prizeAlert')
    prizeAlert.set('color', '#6699ff')
    prizeAlert.set('fontSize', '16')
    prizeAlert.set('delay', '8')
    tickets = ET.SubElement(data, 'tickets')
    for i in range(1, 226):
        ticket = ET.SubElement(tickets, 'ticket')
        ticket.set('name', '')
        ticket.set('id', str(i))
    prizeInfo = ET.SubElement(data, 'prizeInfo')
    saveData = ET.SubElement(data, 'saveData')
    with open(file, 'wb') as dataFile:
        dataFile.truncate(0)
        mydata = ET.tostring(data)
        dataFile.write(mydata)

# DataParser instance to be used
dataParser = DataParser()