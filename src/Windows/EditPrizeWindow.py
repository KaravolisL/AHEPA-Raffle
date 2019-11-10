from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from Prizes.PrizeApi import getAssociatedPrize
from Utils.Validators import validatePrizeName, validatePrizeNumber
import Controller

class EditPrizeWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Prize')
        self.makeLayout()
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.initLineEdits()

    def setSize(self):
        """
        Sizes window to be one fifth width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/5, screenHeight/5)

    def makeLayout(self):
        """
        Creates labels, fields, and two buttons
        """
        self.prizeNumberLabel = QLabel('Prize Number: ')
        self.prizeNumberLabel.setAlignment(Qt.AlignCenter)
        # self.prizeNumberLabel.setFont()
        self.prizeNumberLineEdit = QLineEdit()

        self.prizeDescLabel = QLabel('Prize Description: ')
        self.prizeDescLabel.setAlignment(Qt.AlignCenter)
        # self.prizeDescLabel.setFont()
        self.prizeDescLineEdit = QLineEdit()

        self.changeButton = QPushButton('Change Description')
        self.changeButton.clicked.connect(self.changeDescEvent)
        self.changeButton.setDefault(True)
        self.deleteButton = QPushButton('Delete Prize')
        self.deleteButton.clicked.connect(self.deleteEvent)
        self.addButton = QPushButton('Add Prize')
        self.addButton.clicked.connect(self.addEvent)
        self.addButton.setDefault(True)
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        # Hide these two buttons as setButtons will handle them
        self.changeButton.hide()
        self.deleteButton.hide()

        self.layout.addWidget(self.prizeNumberLabel, 0, 0)
        self.layout.addWidget(self.prizeNumberLineEdit, 0, 1, 1, 2)
        self.layout.addWidget(self.prizeDescLabel, 1, 0)
        self.layout.addWidget(self.prizeDescLineEdit, 1, 1, 1, 2)
        self.layout.addWidget(self.changeButton, 2, 0)
        self.layout.addWidget(self.deleteButton, 2, 1)
        self.layout.addWidget(self.addButton, 2, 0, 1, 2)
        self.layout.addWidget(self.cancelButton, 2, 2)

    def initLineEdits(self):
        """
        Initialize line edit events and validation
        """
        self.numberEntered = 0
        self.prizeNumberLineEdit.textEdited.connect(self.prizeNumberEntered)
        self.prizeNumberLineEdit.setMaxLength(3)

    def setButtons(self, action):
        """
        Switches the confirm button to be either add or change
        :param str action: Either 'add' or 'change/delete'
        """
        assert(action == 'add' or action == 'change/delete')
        if action == 'add':
            self.addButton.show()
            self.changeButton.hide()
            self.deleteButton.hide()
        else:
            self.addButton.hide()
            self.changeButton.show()
            self.deleteButton.show()

    def prizeNumberEntered(self):
        """
        Validates the input then displays the prize's current description
        """
        numberEnteredAsStr = self.prizeNumberLineEdit.text()
        if not validatePrizeNumber(numberEnteredAsStr):
            # Invalid number so clear field and return
            self.numberEntered = 0
            self.prizeDescLineEdit.clear()
            return
        # Entered number is valid
        self.numberEntered = int(numberEnteredAsStr)
        currentPrize = getAssociatedPrize(self.numberEntered)
        if currentPrize == None:
            # No associated Prize, add one?
            self.setButtons('add')
        else:
            # Already a prize
            self.setButtons('change/delete')
            self.prizeDescLineEdit.setText(currentPrize.description)

    def changeDescEvent(self):
        """
        Validates the entered name and notifies it's name has changed
        """
        if self.numberEntered == 0:
            return

        newName = self.prizeDescLineEdit.text()
        if validatePrizeName(newName):
            PrizeList.getInstance().setPrizeName(self.numberEntered, newName)
            Controller.notifyPrizeNameChange(PrizeList.getInstance().getPrize(self.numberEntered))
        else:
            # User tried entering an invalid prize name
            pass

    def deleteEvent(self):
        pass

    def addEvent(self):
        pass

    def keyPressEvent(self, event):
        """
        Connects the enter key to changeDescEvent
        :param QKeyEvent event: Key that was pressed
        """
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.changeDescEvent()

    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

