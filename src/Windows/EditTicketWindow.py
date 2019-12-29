from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from Tickets.TicketList import TicketList
from Utils.Validators import validateTicketName, validateTicketNumber
import Controller

class EditTicketWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Ticket')
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
        self.ticketNumberLabel = QLabel('Ticket Number: ')
        self.ticketNumberLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNumberLabel.setFont()
        self.ticketNumberLineEdit = QLineEdit()

        self.ticketNameLabel = QLabel('Ticket Name: ')
        self.ticketNameLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNameLabel.setFont()
        self.ticketNameLineEdit = QLineEdit()

        self.confirmButton = QPushButton('Change Name')
        self.confirmButton.clicked.connect(self.changeNameEvent)
        self.confirmButton.setDefault(True)
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        self.layout.addWidget(self.ticketNumberLabel, 0, 0)
        self.layout.addWidget(self.ticketNumberLineEdit, 0, 1)
        self.layout.addWidget(self.ticketNameLabel, 1, 0)
        self.layout.addWidget(self.ticketNameLineEdit, 1, 1)
        self.layout.addWidget(self.confirmButton, 2, 0)
        self.layout.addWidget(self.cancelButton, 2, 1)

    def initLineEdits(self):
        """
        Initialize line edit events and validation
        """
        self.numberEntered = 0
        self.ticketNumberLineEdit.textEdited.connect(self.ticketNumberEntered)
        self.ticketNumberLineEdit.setMaxLength(3)

    def ticketNumberEntered(self):
        """
        Validates the input then displays the ticket's current name
        """
        numberEnteredAsStr = self.ticketNumberLineEdit.text()
        if validateTicketNumber(numberEnteredAsStr):
            self.numberEntered = int(numberEnteredAsStr)
            self.ticketNameLineEdit.setText(str(TicketList.getInstance().getTicket(self.numberEntered)))
        else:
            self.numberEntered = 0
            self.ticketNameLineEdit.clear()

    def changeNameEvent(self):
        """
        Validates the entered name and notifies it's name has changed
        """
        if self.numberEntered == 0:
            return

        newName = self.ticketNameLineEdit.text()
        if validateTicketName(newName):
            TicketList.getInstance().setTicketName(self.numberEntered, newName)
            Signals().ticketNameChanged.emit(self.numberEntered)
        else:
            # User tried entering an invalid ticket name
            pass

    def keyPressEvent(self, event):
        """
        Connects the enter key to changeNameEvent
        :param QKeyEvent event: Key that was pressed
        """
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.changeNameEvent()

    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

