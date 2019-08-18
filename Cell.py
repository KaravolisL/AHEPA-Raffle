from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

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
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)

        # DEBUG
        self.setStyleSheet("QLabel {background-color: red;}")
    
    def __initWithTicket__(cls, ticket):
        ''' Contructor to create Cell from Ticket instance'''
        return Cell(ticket.name, ticket.number)

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getText(self):
        return self.text

    def __str__(self):
        return self.getText()

    def mousePressEvent(self, QMouseEvent):
        ''' Method to handle a cell being clicked '''
        if (self.isVisible() and self.id > 0):
            self.setVisible(False)

    def setBackgroundColor(self, color):
        ''' DEBUG '''
        self.setStyleSheet("QLabel {background-color: " + str(color) + ";}")