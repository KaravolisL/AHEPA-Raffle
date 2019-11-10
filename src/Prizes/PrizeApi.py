from Prizes.PrizeList import PrizeList
import Windows.WindowRepository

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
    Constructs a prize alert and displays it
    :param int numOfTicketsDrawn: Number of tickets drawn
    """
    alert = WindowRepository.getInstance().getWindow('prizeAlertWindow')
    PrizeList.getInstance().setAlert(alert, numOfTicketsDrawn)

def getAssociatedPrize(ticketNumber):
    """
    Returns a Prize if there exists one associated with the given ticket number
    :param int ticketNumber: number of ticket for prize
    :returns: Prize associated for this ticket number, None if one is not found
    :rtype: Prize
    """
    return PrizeList.getInstance().getPrizeFromNumber(ticketNumber)
