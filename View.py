from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from math import floor
import Controller
from MenuBar import MenuBar

class View(QWidget):
    instance = None
    def __init__(self):
        super().__init__()

        # Assert to enforce singleton class
        assert(View.instance == None), "Attempt to create another instance"

        # Define instance variable
        View.instance = self

        # Create subwidgets and layout
        self.mainTable = View.MainTable()
        self.header = View.Header()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Add widgets to the layout
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.mainTable)

        # Set Layout to widget
        self.setLayout(self.layout)

    @staticmethod
    def getInstance():
        if (View.instance is None):
            View.instance = View()
        return View.instance

    def setCellTransparent(self, id, bool):
        print(self.getMainTable().getCell(id))
        self.getMainTable().getCell(id).setTransparent(bool)

    def updateHeader(self, info):
        pass

    def updateCell(self, text, id):
        self.getMainTable().updateCell(text, id)

    def getMainTable(self):
        return self.mainTable
    
    class MainTable(QWidget):
        instance = None
        def __init__(self):
            super().__init__()

            # Assert to enforce singleton class
            assert(View.MainTable.instance == None), "Attempt to create another instance"

            # Define instance variable
            View.MainTable.instance = self

            # Create 2D array of blank cells, cells will be initialized by Controller initialize
            self.cells = [[View.Cell(id = j+i) for i in range(0, 15)] for j in range(1, 226, 15)]

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

        @staticmethod
        def getInstance():
            if (View.MainTable.instance is None):
                View.MainTable.instance = View.MainTable()
            return View.MainTable.instance

        def getCell(self, id):
            return self.cells[floor((id-1)/15)][(id-1)%15]

        def updateCell(self, text, id):
            self.getCell(id).setText(text)

    class Header(QWidget):
        instance = None
        def __init__(self):
            super().__init__()

            # Assert to enforce singleton class
            assert(View.Header.instance == None), "Attempt to create another instance"

            # Define singleton instance
            View.Header.instance = self

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

            # Restricting size
            self.setMaxHeight(120)

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

        @staticmethod
        def getInstance():
            if (View.Header.instance is None):
                View.Header.instance = View.Header()
            return View.Header.instance

        def setMaxHeight(self, height):
            for cell in self.cells:
                cell.setFixedHeight(height)
            self.textBox.setFixedHeight(height)

        class TextBox(QLineEdit):
            instance = None
            def __init__(self):
                super().__init__()

                # Assert to enforce singleton class
                assert(View.Header.TextBox.instance == None), "Attempt to create another instance"

                # Make background of lineEdit transparent
                self.setStyleSheet("QLineEdit {background-color: purple; color: transparent;}")

            @staticmethod
            def getInstance():
                if (View.Header.TextBox.instance is None):
                    View.Header.TextBox.instance = View.Header.TextBox()
                return View.Header.TextBox.instance

    class Cell(QLabel):
        def __init__(self, text = None, id = 0):
            super().__init__()

            # Set text and id
            self.text = text
            self.id = id
            self.test = 0
            self.setText(text)

            # Set sizing
            self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.sizePolicy().setRetainSizeWhenHidden(True)
            self.setAlignment(Qt.AlignCenter)
            self.setWordWrap(True)

            # Members for background and text color
            self.backgroundColor = 'red'
            self.textColor = 'black'

            # DEBUG
            self.setBackgroundColor('red')
        
        def setId(self, id):
            self.id = id

        def getId(self):
            return self.id

        def setText(self, text):
            ''' Override setText method to include id for main table cells '''
            self.text = text
            if (self.isInHeader()):
                super().setText(text)
            else:
                super().setText(str(self.id) + "\n" + str(text))
            return self.getText()

        def getText(self):
            return self.text

        def __str__(self):
            return self.getText()

        def mousePressEvent(self, QMouseEvent):
            ''' Method to handle a cell being clicked '''
            if (not self.isInHeader()):
                Controller.Controller.notifyCellRemoved(self)
                self.setTransparent(True)
            elif (self.getId() == -3):
                # Implement undo button feature here
                print('Undo button clicked')
                Controller.Controller.notifyUndoClicked()

        def setBackgroundColor(self, color = 'red'): # Update with raffle background color
            ''' Method to set background color of cell '''
            self.backgroundColor = str(color)
            self.setStyleSheet("QLabel {background-color: " + self.backgroundColor + ";color: " + self.textColor + ";}")

        def setTextColor(self, color = 'black'): # Update with raffle text color
            ''' Method to set text color of cell '''
            self.textColor = str(color)
            self.setStyleSheet("QLabel {background-color: " + self.backgroundColor + ";color: " + self.textColor + ";}")

        def setTransparent(self, bool):
            ''' Method to make cells transparent or not '''
            if (bool):
                self.setStyleSheet("QLabel {background-color: transparent;color: transparent;}")
            else:
                self.setTextColor()
                self.setBackgroundColor()

        def isInHeader(self):
            ''' Convenience method to distinguish header cells from main table cells '''
            return self.id < 0

class MainWindow(QMainWindow):
    instance = None
    def __init__(self):
        super(MainWindow, self).__init__()

        # Assert to enforce singleton class
        assert(MainWindow.instance == None), "Attempt to create another instance"

        # Define instance variable
        MainWindow.instance = self

        # Setting up the menu bar
        self.setMenuBar(self.createMenuBar())

        # Creating the central widget for the window
        centralWidget = View()
        self.setCentralWidget(centralWidget)

        # Setting window icon
        self.setWindowIcon(QIcon('Icon.jpg'))

    def createMenuBar(self):
        ''' Creates a MenuBar instance and sets the actions '''
        menuBar = MenuBar()
        menuBar.setResponse(menuBar.viewFullScreenAction, self.showFullScreen)
        menuBar.setResponse(menuBar.viewMaximizedAction, self.showMaximized)
        # TODO: Set remaining responses
        return menuBar

    def keyPressEvent(self, e):
        ''' Override keyPressEvent to handle Esc pressed '''
        if e.key() == Qt.Key_Escape:
            self.showMaximized()

    def showFullScreen(self):
        ''' Override showFullScreen method to hide menuBar '''
        super().showFullScreen()
        self.setMenuBar(None)

    def showMaximized(self):
        ''' Override showMaximized method to show menuBar '''
        super().showMaximized()
        self.setMenuBar(self.createMenuBar())

    def closeEvent(self, e):
        # TODO: Go through Controller
        # saveProgress()
        pass