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
        print("Cell #" + str(cell.getId()) + " has been removed.\n")
        cell.setText("clicked")

    @staticmethod
    def initialize():
        print("Raffle initializing...")
        
        # Read names from ticketNames file
        names = FileManager.readNames("ticketNames.txt")

        # Initialize the fullList using the names. Controller will be notified of name change
        RaffleList.fullListInit(names)

    @staticmethod
    def notifyTicketNameChange(tickets):
        # for ticket in tickets:
            # View.View.getInstance().updateCell(ticket.getName(), ticket.getNumber())
        View.View.getInstance().updateCell('dfasdfas', 11)
        View.View.getInstance().getMainTable().getCell(-1).setText('made it here')
        print('Here')
        print(View.View.getInstance().getMainTable().getCell(11).text)

    def test(text):
        View.View.getInstance().updateCell(text, 0)
        View.View.getInstance().mainTable.getCell(0).update()
