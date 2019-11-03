from Prizes.PrizeList import PrizeList

def initializePrizeList():
    """
    Initialize the prize subsystem
    """
    PrizeList.getInstance().initialize()

def prizeCheck(numOfTicketsDrawn):
    """
    
    :param int numOfTicketsDrawn: Number of tickets drawn
    :returns: Whether a prize exists for the next ticket
    :rtype: bool
    """
    nextPrize = PrizeList.getInstance().getNextPrize(numOfTicketsDrawn)
    return (nextPrize != None) and (numOfTicketsDrawn == nextPrize.number - 1)
