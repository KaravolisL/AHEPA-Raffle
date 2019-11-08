from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from Tickets.TicketList import TicketList

class EditTicketWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Ticket')
        self.makeLayout()
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.initLineEdits()


    def setSize(self):
        """
        Sizes window to be one third width and height
        """
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth/3, screenHeight/3)

    def makeLayout(self):
        """
        Creates labels, fields, and two buttons
        """
        self.ticketNumberLabel = QLabel('Ticket Number: ')
        self.ticketNumberLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNumberLabel.setFont()
        self.ticketNumberLineEdit = QLineEdit()

        self.currentNameLabel = QLabel('Current Name: ')

        self.ticketNameLabel = QLabel('Ticket Name: ')
        self.ticketNameLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNameLabel.setFont()
        self.ticketNameLineEdit = QLineEdit()

        self.confirmButton = QPushButton('Change Name')
        # self.confirmButton.clicked.connect()
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        self.layout.addWidget(self.ticketNumberLabel, 0, 0)
        self.layout.addWidget(self.ticketNumberLineEdit, 0, 1)
        self.layout.addWidget(self.currentNameLabel, 1, 0, 2, 1)
        self.layout.addWidget(self.ticketNameLabel, 2, 0)
        self.layout.addWidget(self.ticketNameLineEdit, 2, 1)
        self.layout.addWidget(self.confirmButton, 3, 0)
        self.layout.addWidget(self.cancelButton, 3, 1)

    def initLineEdits(self):
        """
        Initialize line edit events and validation
        """
        self.ticketNumberLineEdit.textEdited.connect(self.ticketNumberEntered)
        self.ticketNumberLineEdit.setMaxLength(3)
    
    def ticketNumberEntered(self):
        numberEntered = int(self.ticketNumberLineEdit.text())
        print(numberEntered)
        self.ticketNameLineEdit.setText(str(TicketList.getInstance().getTicket(numberEntered)))

    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

        