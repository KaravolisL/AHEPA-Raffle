from PyQt5.QtWidgets import QWidget, QHBoxLayout, QStackedLayout, QSizePolicy

from FileManager.DataParser import dataParser
from View.CellPkg.HeaderCells import TicketsRemainingCell, TicketsDrawnCell, LastTicketDrawnCell
from View.TextBox import TextBox
from Signals import Signals

class Header(QWidget):
    def __init__(self):
        super().__init__()

        # Create subelements
        self.cells = [TicketsRemainingCell(), TicketsDrawnCell(), LastTicketDrawnCell()]
        self.textBox = TextBox()

        # Set cell colors and connect signal
        self.setColor()
        Signals().colorChanged.connect(self.setColor)

        # Restrict the size
        self.setMaxHeight(120)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        
         # Making and setting layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)

        # Doing some crazy shit here
        leftWrapper = QWidget()
        leftLayout = QStackedLayout()
        leftWrapper.setLayout(leftLayout)
        leftLayout.setStackingMode(QStackedLayout.StackAll)
        leftLayout.addWidget(self.cells[0])
        leftLayout.addWidget(self.textBox)

        middleWrapper = QWidget()
        middleLayout = QStackedLayout()
        middleWrapper.setLayout(middleLayout)
        middleLayout.addWidget(self.cells[1])

        rightWrapper = QWidget()
        rightLayout = QStackedLayout()
        rightWrapper.setLayout(rightLayout)
        rightLayout.addWidget(self.cells[2])

        # Final part of the crazy shit
        self.layout.addWidget(leftWrapper)
        self.layout.addWidget(middleWrapper)
        self.layout.addWidget(rightWrapper)

    def setMaxHeight(self, height):
        """
        Helper method to set the max height of each subelement
        :param int height: Max height for each element
        """
        for cell in self.cells:
            cell.setFixedHeight(height)
        self.textBox.setFixedHeight(height)

    def updateHeader(self, info):
        """
        Method used to update the three numbers displayed in the header
        :param list info: List containing three ints for the header
        """
        for cell, num in zip(self.cells, info):
            cell.setText(str(num))

    def setColor(self):
        """
        This method is used to change the color of the header cells in the
        case that it's changed. It obtains this color from the save file.
        """
        headerColor = dataParser.getColor('header')
        for cell in self.cells:
            cell.setBackgroundColor(headerColor)