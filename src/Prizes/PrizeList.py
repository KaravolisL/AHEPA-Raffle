from Prizes.Prize import Prize
from FileManager import readPrizes

class PrizeList():
    instance = None
    prizeList = []
    alert = None

    def __init__(self):

        assert(PrizeList.instance == None) # Assert to ensure singleton
        PrizeList.instance = self

    @staticmethod
    def getInstance():
        return PrizeList.instance if PrizeList.instance != None else PrizeList()

    def initialize(self):
        prizeDict = readPrizes()
        for prize in prizeDict:
            self.prizeList.append(Prize(prize, prizeDict[prize]))

    def getPrizeFromNumber(self, number):
        """
        Looks for a prize associated with a given number
        :param int number: Ticket number associated with a prize
        :returns: Prize in PrizeList with given number, None if one is not found
        :rtype: Prize
        """
        for prize in self.prizeList:
            if prize.number == number:
                return prize
        return None

    def getNextPrize(self, numOfTicketsDrawn):
        """
        Iterates the PrizeList and returns the prize with the next highest number than the number 
        passed in
        :param int numOfTicketsDrawn: Number of tickets currently drawn
        :returns: Next prize to be given out, None if no more prizes exist
        :rtype: Prize
        """
        nextPrize = None
        for prize in self.prizeList:
            if prize.number > numOfTicketsDrawn:
                if ((nextPrize == None) or 
                    (prize.number < nextPrize.number)):
                    nextPrize = prize
        return nextPrize

    def setAlert(self, alert, numOfTicketsDrawn):
        """
        Attaches the given alert to the PrizeList, sets it's prize, and displays it
        :param PrizeAlert alert: alert to attach
        :param int numOfTicketsDrawn: current number of tickets drawn
        """
        print("Showing Alert")
        self.alert = alert
        self.alert.setPrize(self.getNextPrize(numOfTicketsDrawn))
        self.alert.show()


    

    

