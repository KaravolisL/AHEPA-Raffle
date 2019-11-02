from Prizes.PrizeList import PrizeList

def initializePrizeList():
    """
    Initialize the prize subsystem
    """
    PrizeList.getInstance().initialize()

def prizeCheck(ticketId):
    """
    
    :param int ticketId: id of the ticket just removed
    """
    pass