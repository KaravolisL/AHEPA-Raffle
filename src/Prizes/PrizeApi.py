from Prizes.PrizeList import PrizeList
from Windows.WindowRepository import WindowRepository

def initializePrizeList():
    """
    Initialize the prize subsystem
    """
    PrizeList.getInstance().initialize()

def prizeCheck(numOfTicketsDrawn):
    """
    Checks to see if a prize is registered for the next ticket to be drawn
    :param int numOfTicketsDrawn: Number of tickets drawn
    :returns: Whether a prize exists for the next ticket
    :rtype: bool
    """
    nextPrize = PrizeList.getInstance().getNextPrize(numOfTicketsDrawn)
    return (nextPrize != None) and (numOfTicketsDrawn == nextPrize.number - 1)

def displayPrizeAlert(numOfTicketsDrawn):
    """
    
    :param int numOfTicketsDrawn: Number of tickets drawn
    """
    alert = WindowRepository.getInstance().getWindow('prizeAlertWindow')
    PrizeList.getInstance().setAlert(alert)
