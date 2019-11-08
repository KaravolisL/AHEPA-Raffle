from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase

class EditTicketWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.makeLayout()
        self.setWindowFlags(Qt.WindowCloseButtonHint)


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
        self.confirmButton = QPushButton('Change Name')
        # self.confirmButton.clicked.connect()

        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        self.ticketNumberLabel = QLabel('Ticket Number: ')
        self.ticketNumberLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNumberLabel.setFont()

        self.ticketNumberLineEdit = QLineEdit()

        self.ticketNameLabel = QLabel('Ticket Name: ')
        self.ticketNameLabel.setAlignment(Qt.AlignCenter)
        # self.ticketNameLabel.setFont()

        self.ticketNameLineEdit = QLineEdit()

        self.layout.addWidget(self.ticketNumberLabel, 0, 0)
        self.layout.addWidget(self.ticketNumberLineEdit, 0, 1)
        self.layout.addWidget(self.ticketNameLabel, 1, 0)
        self.layout.addWidget(self.ticketNameLineEdit, 1, 1)
        self.layout.addWidget(self.confirmButton, 2, 0)
        self.layout.addWidget(self.cancelButton, 2, 1)

    
    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

        