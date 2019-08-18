from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Cell import Cell

class Header(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        # Make cell
        self.ticketsRemainingCell = Cell("Tickets Remaining: 255", -3)
        self.ticketsRemainingCell.setBackgroundColor("blue")
        self.addWidget(self.ticketsRemainingCell)

        self.ticketsDrawnCell = Cell("Tickets Drawn: 0", -2)
        self.ticketsDrawnCell.setBackgroundColor("yellow")
        self.addWidget(self.ticketsDrawnCell)

        self.lastTicketDrawnCell = Cell("Last Ticket Drawn: ", -1)
        self.lastTicketDrawnCell.setBackgroundColor("green")
        self.addWidget(self.lastTicketDrawnCell)