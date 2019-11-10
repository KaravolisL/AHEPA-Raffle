from Prizes.PrizeList import PrizeList
from Prizes.Prize import Prize
import Windows.WindowRepository as WR

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
    alert = WR.WindowRepository.getInstance().getWindow('prizeAlertWindow')
    PrizeList.getInstance().setAlert(alert, numOfTicketsDrawn)

def getAssociatedPrize(ticketNumber):
    """
    Returns a Prize if there exists one associated with the given ticket number
    :param int ticketNumber: number of ticket for prize
    :returns: Prize associated for this ticket number, None if one is not found
    :rtype: Prize
    """
    return PrizeList.getInstance().getPrizeFromNumber(ticketNumber)

def setPrizeDescription(prizeNumber, newDesc):
    """
    Sets a given prize to have a new description
    :param int prizeNumber: number of the prize
    :param str newDesc: New description for the prize
    """
    prize = getAssociatedPrize(prizeNumber)
    assert(prize != None), 'Can only set description of a prize that exists'
    prize.description = newDesc

def addPrize(prizeNumber, desc):
    """
    Adds a new prize using the parameters
    :param int prizeNumber: number for the prize
    :param str desc: description for the prize
    """
    assert(getAssociatedPrize(prizeNumber) == None), 'Prize already exists'
    PrizeList.getInstance().prizeList.append(Prize(prizeNumber, desc))

def deletePrize(prizeNumber):
    """
    Delets a prize for the PrizeList
    :param int prizeNumber: number of the prize
    """
    PrizeList.getInstance().remove(prizeNumber)
