from PyQt5.QtWidgets import QWidget, QSizePolicy, QGridLayout

from math import floor

from View.CellPkg.TableCell import TableCell
from FileManager.DataParser import dataParser
from FileManager.FileManager import readTicketNames
from Tickets.TicketList import TicketList
from Signals import Signals

# Logger import
from Logger.Logger import logger

class MainTable(QWidget):
    def __init__(self):
        super().__init__()

        # Create 2D array of blank cells
        self.cells = [[None for i in range(0, 15)] for j in range(0, 15)]

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(1)

        # Grow vertically and horizontally
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Adding cells to the layout
        for i in range(0, 15):
            for j in range(0, 15):
                ticketId = (i*15) + (j+1)
                name = TicketList.getInstance().getTicket(ticketId).name
                self.cells[i][j] = TableCell(text=name, id=ticketId)
                self.layout.addWidget(self.cells[i][j], i, j)

        # Set color and connect signal
        self.setColor()
        Signals().colorChanged.connect(self.setColor)

        # Connect the ticketDrawn and undoButtonClicked signals
        Signals().ticketDrawn.connect(lambda id: self.getCell(id).setTransparent(True))
        Signals().undoButtonClicked.connect(lambda id: self.getCell(id).setTransparent(False))
        Signals().ticketNameChanged.connect(self.updateCell)

    def getCell(self, id):
        """
        Helper method to obtain cell from 2D array given id
        :param int id: Id of cell to obtain
        """
        return self.cells[floor((id-1)/15)][(id-1)%15]

    def updateCell(self, id, text=None):
        """
        Helper method to update a cell with new text given an id.
        :param str text: New text for cell
        :param int id: Id of cell being updated
        """
        if text is None:
            ticket = TicketList.getInstance().getTicket(id)
            text = ticket.name
        self.getCell(id).setText(text)

    def setColor(self):
        """
        This method is used to change the color of the main table's cell if
        it gets changed. It obtains this color from the save file.
        """
        mainTableColor = dataParser.getColor('mainTable')
        for row in self.cells:
            for cell in row:
                cell.setBackgroundColor(mainTableColor)
