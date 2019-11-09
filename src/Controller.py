from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import FileManager
from Tickets.TicketList import TicketList
from ViewApi import *
import Prizes.PrizeApi as PrizeApi

def initialize():
    """
    This method will be called once upon startup of the program. It has the following responsibilites:
    1. Initialize the TicketList
    2. RestoreProgress from the saveFile
    3. Initialize the PrizeList
    4. Create the mainWindow and set it to maximized
    Note: Initialize PrizeList after restoring progess to prevent PrizeAlerts
    """
    print("Raffle initializing...")

    # Get the TicketList instance
    ticketList = TicketList.getInstance()

    # Initialize the TicketList
    ticketList.initialize()
    for ticket in ticketList.ticketList:
        notifyTicketNameChange(ticket)

    # Restore progress using save file
    restoreProgress("saveFile.txt")

    # Initialize the prize list
    PrizeApi.initializePrizeList()

    # Construct MainWindow and its contents
    window = getMainWindow()
    window.showMaximized()

def notifyCellRemoved(id):
    """
    This method is called to handle the model's actions when a cell is removed. It's
    responsibilties are as follows:
    1. Remove the ticket from the TicketList
    2. Update the header using the new information
    3. Execute prize check
    """
    # Get the TicketList instance
    ticketList = TicketList.getInstance()

    # Check if cell has already been removed
    if (ticketList.hasTicketBeenDrawn(id)):
        return

    # Add removed cell to RaffleList
    ticketList.removeTicket(id)

    # Update header
    updateHeader(ticketList.getHeaderInfo())

    # Check if next ticket will be a prize ticket
    if PrizeApi.prizeCheck(ticketList.numOfTicketsDrawn):
        print("Displaying prizeAlert")
        PrizeApi.displayPrizeAlert(ticketList.numOfTicketsDrawn)

def notifyTicketNameChange(ticket):
    """
    This method is called when a ticket's name was changed either during initialization or by the
    user at runtime.
    :param Ticket ticket: ticket whose names were changed
    """
    updateCell(ticket.getName(), ticket.getNumber())

def notifyUndoClicked():
    """
    This method is called when the undo button is clicked. It's responsibilites are as follows:
    1. Replace the ticket in the TicketList
    2. Make corresponding cell visible
    3. Update the header with new information
    """
    # Get last ticket drawn
    lastTicketDrawn = TicketList.getInstance().replaceTicket()

    # Replace ticket if raffle has started
    if (lastTicketDrawn != None):
        setCellTransparent(lastTicketDrawn.getNumber(), False)

        # Update header
        updateHeader(TicketList.getInstance().getHeaderInfo())

def saveProgress():
    """
    This method saves the progress of the raffle as well as any updates to the ticket names
    """
    FileManager.saveProgress(TicketList.getInstance().getDrawnTickets())
    ticketNamesFile = open('ticketNames.txt', 'r+')
    ticketNamesFile.truncate(0)
    for ticket in TicketList.getInstance().ticketList:
        ticketNamesFile.write(ticket.getName())

def restoreProgress(file):
    """
    This method uses a given file to update the Raffle to that given point.
    :param str file: File from which to restore progress
    """
    removedTicketIds = FileManager.readSaveFile(file)
    for id in removedTicketIds:
        notifyCellRemoved(id)
        setCellTransparent(id, True)

def restartRaffle():
    """
    This method is called when the user clicks the restart option. It replaces all the tickets drawn
    and resets the header.
    """
    while (TicketList.getInstance().hasRaffleStarted() is not False):
        notifyUndoClicked()
