from Prizes.Prize import Prize
from Tickets.TicketList import TicketList
from Signals import Signals
from FileManager.FileManager import readPrizes

class PrizeList():
    instance = None
    prizeList = []
    alert = None

    def __init__(self):

        assert(PrizeList.instance == None) # Assert to ensure singleton
        PrizeList.instance = self

        # Connect the ticketDrawn signal to check for prizes
        Signals().ticketDrawn.connect(self.prizeCheck)

    @staticmethod
    def getInstance():
        return PrizeList.instance if PrizeList.instance != None else PrizeList()

    def initialize(self):
        prizeDict = readPrizes()
        for prize in prizeDict:
            self.prizeList.append(Prize(prize, prizeDict[prize]))
            Signals().prizeChanged.emit(prize)

    def remove(self, prizeNumber):
        """
        Removes a Prize from the list
        :param int prizeNumber: number of the prize to remove
        """
        for prize in self.prizeList:
            if prizeNumber == prize.number:
                self.prizeList.remove(prize)

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

    def prizeCheck(self):
        """
        Checks to see if a prize is registered for the next ticket to be drawn
        This method is connected to the ticketDrawn signal. If a prize is found,
        a prize alert will be displayed.
        """
        numOfTicketsDrawn = TicketList.getInstance().numOfTicketsDrawn
        nextPrize = self.getNextPrize(numOfTicketsDrawn)
        if (nextPrize is None) or (numOfTicketsDrawn != nextPrize.number - 1):
            return
        else:
            from Windows.WindowRepository import WindowRepository, WindowType
            self.alert = WindowRepository().getWindow(WindowType.PRIZE_ALERT)
            self.alert.setPrize(nextPrize)
            self.alert.show()