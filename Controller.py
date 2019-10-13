from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import FileManager
import RaffleList
import View

from Windows.PopupBase import PopupBase

class Controller:
    @staticmethod
    def initialize():
        """
        This method will be called once upon startup of the program. It has the following responsibilites:
        1. Read names from ticketNames.txt
        2. Initialize the fullList of tickets in RaffleList
        3. RestoreProgress from the saveFile
        4. Create the mainWindow and set it to maximized
        """
        print("Raffle initializing...")
        
        # Read names from ticketNames file
        names = FileManager.readTicketNames("ticketNames.txt")

        # Initialize the fullList using the names. Controller will be notified of name change
        RaffleList.fullListInit(names)

        # Restore progress using save file
        Controller.restoreProgress("saveFile.txt")

        # Construct MainWindow and its contents
        window = View.MainWindow()
        window.showMaximized()

    @staticmethod
    def notifyCellRemoved(id):
        """
        This method is called to handle the model's actions when a cell is removed. It's 
        responsibilties are as follows:
        1. Add the id the the drawnList in RaffleList
        2. Update the header using the new information
        """
        # Check if cell has already been removed
        if (not RaffleList.hasTicketBeenPulled(id)):
            return
        
        # Add removed cell to RaffleList
        RaffleList.appendTicket(id)

        # Update header
        View.View.getInstance().updateHeader(RaffleList.getHeaderInfo())

    @staticmethod
    def notifyTicketNameChange(tickets):
        """
        This method is called when a ticket's name was changed either during initialization or by the 
        user at runtime.
        :param list tickets: List of tickets whose names were changed
        """
        for ticket in tickets:
            View.View.getInstance().updateCell(ticket.getName(), ticket.getNumber())

    @staticmethod
    def notifyUndoClicked():
        """
        This method is called when the undo button is clicked. It's responsibilites are as follows:
        1. Pop the last ticket drawn from the RaffleList
        2. Make corresponding cell visible
        3. Update the header with new information 
        """
        # Get last ticket drawn
        lastTicketDrawn = RaffleList.pop()

        # Replace ticket if raffle has started
        if (lastTicketDrawn != None):
            View.View.getInstance().setCellTransparent(lastTicketDrawn.getNumber(), False)

            # Update header
            View.View.getInstance().updateHeader(RaffleList.getHeaderInfo())

    @staticmethod
    def saveProgress():
        """
        This method is a passthru to the FileManager's save progress function.
        """
        FileManager.saveProgress(RaffleList.drawnList)

    @staticmethod
    def restoreProgress(file):
        """
        This method uses a given file to update the Raffle to that given point.
        :param str file: File from which to restore progress
        """
        removedTicketIds = FileManager.readSaveFile(file)
        for id in removedTicketIds:
            Controller.notifyCellRemoved(id)
            View.View.getInstance().setCellTransparent(id, True)

    @staticmethod
    def restartRaffle():
        """
        This method is called when the user clicks the restart option. It replaces all the tickets drawn 
        and resets the header.
        """
        View.MainWindow.getInstance().popup = PopupBase()
        while (RaffleList.hasRaffleStarted() is not False):
            Controller.notifyUndoClicked()
