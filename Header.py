from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Cell import Cell

class Header(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        # Make cells
        self.ticketsRemainingCell = Cell("Tickets Remaining: 225", -3)
        self.ticketsDrawnCell = Cell("Tickets Drawn: 0", -2)
        self.lastTicketDrawnCell = Cell("Last Ticket Drawn: ", -1)

        # DEBUG
        self.ticketsRemainingCell.setBackgroundColor("blue")
        self.ticketsDrawnCell.setBackgroundColor("yellow")
        self.lastTicketDrawnCell.setBackgroundColor("green")

        # Add cells to the layout
        self.addWidget(self.ticketsRemainingCell)
        self.addWidget(self.ticketsDrawnCell)
        self.addWidget(self.lastTicketDrawnCell)