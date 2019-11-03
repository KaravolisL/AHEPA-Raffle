from Prizes.Prize import Prize
from FileManager import readPrizes

class PrizeList():
    instance = None
    prizeList = []

    def __init__(self):

        assert(self.instance == None) # Assert to ensure singleton
        PrizeList.instance = self

    @staticmethod
    def getInstance():
        return PrizeList.instance if PrizeList.instance != None else PrizeList()

    def initialize(self):
        prizeDict = readPrizes()
        for prize in prizeDict:
            self.prizeList.append(Prize(prize, prizeDict[prize]))

    def getPrizeFromNumber(self, number):
        for prize in prizeList:
            if prize.number == number:
                return prize

    def getNextPrize(self):
        nextPrize = prizeList[0]
        for prize in prizeList[1:]:
            if prize.getNumber < nextPrize:
                nextPrize = prize
        return nextPrize


    

    

