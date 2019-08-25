from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import RaffleList
from math import floor

class Header(QHBoxLayout):
    instance = None
    def __init__(self):
        super().__init__()

        # Assert to enforce singleton class
        assert(Header.instance == None), "Attempt to create another instance"
        
        # Make cells
        self.ticketsRemainingCell = Cell("Tickets Remaining: 225", -1)
        self.ticketsDrawnCell = Cell("Tickets Drawn: 0", -2)
        self.lastTicketDrawnCell = Cell("Last Ticket Drawn: ", -3)

        # Make list of cells to simplify operations
        self.cells = [self.ticketsRemainingCell, self.ticketsDrawnCell, self.lastTicketDrawnCell]

        # DEBUG
        self.ticketsRemainingCell.setBackgroundColor("blue")
        self.ticketsDrawnCell.setBackgroundColor("yellow")
        self.lastTicketDrawnCell.setBackgroundColor("green")

        for cell in self.cells:
            # Restricting size
            # TODO: Dynamic sizing
            cell.setFixedHeight(100)

        # Creating stack layout for text box and first cell
        stackedLayout = QStackedLayout()
        self.ticketsRemainingCell.setLayout(stackedLayout)
        # stackedLayout.addWidget(self.ticketsRemainingCell)
        # stackedLayout.addWidget(self.TextBox.getInstance())
        stackedLayout.setStackingMode(QStackedLayout.StackAll)
        # stackedLayout.setSizeConstraint(QLayout.SetFixedSize)
        
        # Add cells/layout to the parent layout
        self.addLayout(stackedLayout)
        self.addWidget(self.ticketsDrawnCell)
        self.addWidget(self.lastTicketDrawnCell)

    def updateHeader(self, info):
        self.ticketsRemainingCell.setText("Tickets Remaining: " + str(info[0]))
        self.ticketsDrawnCell.setText("Tickets Drawn: " + str(info[1]))
        self.lastTicketDrawnCell.setText("Last Ticket Drawn: " + str(info[2]))

    def getInstance():
        if (Header.instance is None):
            Header.instance = Header()
        return Header.instance

    class TextBox(QLineEdit):
        instance = None
        def __init__(self):
            super().__init__()

            # Assert to enforce singleton class
            assert(Header.instance == None), "Attempt to create another instance"

            # Make background of lineEdit transparent
            self.setStyleSheet("QLineEdit {background-color: transparent;}")

            # TODO: Dynamic sizing
            self.setMaximumHeight(100)

        def getInstance():
            if (Header.TextBox.instance is None):
                Header.TextBox.instance = Header.TextBox()
            return Header.TextBox.instance

class MainTable(QGridLayout):
    instance = None
    def __init__(self):
        super().__init__()

        # Assert to enforce singleton class
        assert(MainTable.instance == None), "Attempt to create another instance"

        # Create 2D array of cells with corresponding ids
        self.cells = [[Cell(ticket = RaffleList.fullList[i+j-1]) for i in range(0, 15)] for j in range(1, 226, 15)]

        # Adding cells to the layout
        for i in range(0, 15):
            for j in range(0, 15):
                self.addWidget(self.cells[i][j], i, j)

        # Set spacing
        self.setSpacing(1)

    def getInstance():
        if (MainTable.instance is None):
            MainTable.instance = MainTable()
        return MainTable.instance

    def getCell(self, id):
        return self.cells[floor((id-1)/15)][(id-1)%15]

class Cell(QLabel):
    def __init__(self, text = None, id = 0, ticket = None):
        super().__init__()

        # Set text and id with or without ticket
        if (ticket != None):
            self.text = ticket.name
            self.id = ticket.number
        else:
            self.text = text
            self.id = id
        self.setText(self.text)

        # Set sizing
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.sizePolicy().setRetainSizeWhenHidden(True)
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

        # DEBUG
        self.setStyleSheet("QLabel {background-color: red;}")

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setText(self, text):
        ''' Override setText method to include id for main table cells '''
        if (self.isInHeader()):
            super().setText(text)
        else:
            super().setText(str(self.id) + "\n" + self.text)

    def getText(self):
        return self.text

    def __str__(self):
        return self.getText()

    def mousePressEvent(self, QMouseEvent):
        ''' Method to handle a cell being clicked '''
        if (self.isVisible() and not self.isInHeader()):
            self.setVisible(False) # TODO: Investigate difference between setVisible and setHidden
            RaffleList.add(self)
            Header.getInstance().updateHeader(RaffleList.getHeaderInfo())
        if (self.id == -3 and RaffleList.hasRaffleStarted()): # Undo button
            MainTable.getInstance().getCell(RaffleList.removeTail().getId()).setVisible(True)
            Header.getInstance().updateHeader(RaffleList.getHeaderInfo())

    def setBackgroundColor(self, color):
        ''' DEBUG '''
        self.setStyleSheet("QLabel {background-color: " + str(color) + ";}")

    def isInHeader(self):
        ''' Convenience method to distinguish header cells from main table cells '''
        return self.id < 0