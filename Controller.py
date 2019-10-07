from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import FileManager
import RaffleList
import View

class Controller:
    @staticmethod
    def notifyCellRemoved(cell):
        # Add removed cell to RaffleList
        RaffleList.appendTicket(cell.getId())

        # Update header
        View.View.getInstance().updateHeader(RaffleList.getHeaderInfo())

    @staticmethod
    def initialize():
        print("Raffle initializing...")
        
        # Read names from ticketNames file
        names = FileManager.readNames("ticketNames.txt")

        # Initialize the fullList using the names. Controller will be notified of name change
        RaffleList.fullListInit(names)

    @staticmethod
    def notifyTicketNameChange(tickets):
        for ticket in tickets:
            View.View.getInstance().updateCell(ticket.getName(), ticket.getNumber())

    @staticmethod
    def notifyUndoClicked():
        # Get last ticket drawn
        lastTicketDrawn = RaffleList.getLastTicketDrawn()

        # Replace ticket if raffle has started
        if (lastTicketDrawn != None):
            View.View.getInstance().setCellTransparent(lastTicketDrawn.getNumber(), False)
            RaffleList.pop()

            # Update header
            View.View.getInstance().updateHeader(RaffleList.getHeaderInfo())
