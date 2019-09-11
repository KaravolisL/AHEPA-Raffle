from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from math import floor
from Controller import Controller

class View(QWidget):
    instance = None
    def __init__(self):
        super().__init__()

        # Assert to enforce singleton class
        assert(View.instance == None), "Attempt to create another instance"

        # Create subwidgets and layout
        self.mainTable = View.MainTable()
        self.header = View.Header()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0,0,0,0)

        # Add widgets to the layout
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.mainTable)

        # Set Layout to widget
        self.setLayout(self.layout)

    def getInstance():
        if (View.instance is None):
            View.instance = View()
        return View.instance

    def setCellVisibility(self, id):
        pass

    def updateHeader(self, info):
        pass
    
    class MainTable(QWidget):
        instance = None
        def __init__(self):
            super().__init__()

            # Assert to enforce singleton class
            assert(View.MainTable.instance == None), "Attempt to create another instance"

            # Create 2D array of blank cells, cells will be initialized by Controller.initialize
            self.cells = [[View.Cell() for i in range(0, 15)] for j in range(1, 226, 15)]

            # Create and set layout
            self.layout = QGridLayout()
            self.setLayout(self.layout)
            self.layout.setSpacing(0)

            # Grow vertically and horizontally
            self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            # Adding cells to the layout
            for i in range(0, 15):
                for j in range(0, 15):
                    self.layout.addWidget(self.cells[i][j], i, j)

            # Set spacing
            self.layout.setSpacing(1)

        def getInstance():
            if (View.MainTable.instance is None):
                View.MainTable.instance = View.MainTable()
            return View.MainTable.instance

        def getCell(self, id):
            return self.cells[floor((id-1)/15)][(id-1)%15]

    class Header(QWidget):
        instance = None
        def __init__(self):
            super().__init__()

            # Assert to enforce singleton class
            assert(View.Header.instance == None), "Attempt to create another instance"

            # Make cells
            self.ticketsRemainingCell = View.Cell("Tickets Remaining: 225", -1)
            self.ticketsDrawnCell = View.Cell("Tickets Drawn: 0", -2)
            self.lastTicketDrawnCell = View.Cell("Last Ticket Drawn: ", -3)

            # Make text box 
            self.textBox = View.Header.TextBox()

            # Make list of cells to simplify operations
            self.cells = [self.ticketsRemainingCell, self.ticketsDrawnCell, self.lastTicketDrawnCell]

            # DEBUG
            self.ticketsRemainingCell.setBackgroundColor("transparent")
            self.ticketsDrawnCell.setBackgroundColor("yellow")
            self.lastTicketDrawnCell.setBackgroundColor("green")

            for cell in self.cells:
                # Restricting size
                # TODO: Dynamic sizing
                cell.setFixedHeight(100)

            # Preferred size for horizontal and fixed maximum height
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
            leftLayout.addWidget(self.ticketsRemainingCell)
            leftLayout.addWidget(self.textBox)

            middleWrapper = QWidget()
            middleLayout = QStackedLayout()
            middleWrapper.setLayout(middleLayout)
            middleLayout.addWidget(self.ticketsDrawnCell)

            rightWrapper = QWidget()
            rightLayout = QStackedLayout()
            rightWrapper.setLayout(rightLayout)
            rightLayout.addWidget(self.lastTicketDrawnCell)

            # Final part of the crazy shit
            self.layout.addWidget(leftWrapper)
            self.layout.addWidget(middleWrapper)
            self.layout.addWidget(rightWrapper)

        def getInstance():
            if (View.Header.instance is None):
                View.Header.instance = View.Header()
            return View.Header.instance

        class TextBox(QLineEdit):
            instance = None
            def __init__(self):
                super().__init__()

                # Assert to enforce singleton class
                assert(View.Header.TextBox.instance == None), "Attempt to create another instance"

                # Make background of lineEdit transparent
                self.setStyleSheet("QLineEdit {background-color: purple;}")

                # TODO: Dynamic sizing
                self.setMaximumHeight(100)

            def getInstance():
                if (View.Header.TextBox.instance is None):
                    View.Header.TextBox.instance = View.Header.TextBox()
                return View.Header.TextBox.instance

    class Cell(QLabel):
        def __init__(self, text = 'None', id = 0):
            super().__init__()

            # Set text and id
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
            Controller.notifyCellRemoved(self.id)

        def setBackgroundColor(self, color):
            ''' DEBUG '''
            self.setStyleSheet("QLabel {background-color: " + str(color) + ";}")

        def isInHeader(self):
            ''' Convenience method to distinguish header cells from main table cells '''
            return self.id < 0