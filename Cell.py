from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import RaffleList
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
            super().setText(self.text)
        else:
            super().setText(str(self.id) + "\n" + self.text)

    def getText(self):
        return self.text

    def __str__(self):
        return self.getText()

    def mousePressEvent(self, QMouseEvent):
        ''' Method to handle a cell being clicked '''
        if (self.isVisible() and not self.isInHeader()):
            self.setVisible(False)
            RaffleList.add(self)
            # TODO: Update header
        if (self.id == -3): # Undo button
            RaffleList.remove(self)
            print(RaffleList)
            # TODO: update header

    def setBackgroundColor(self, color):
        ''' DEBUG '''
        self.setStyleSheet("QLabel {background-color: " + str(color) + ";}")

    def isInHeader(self):
        ''' Convenience method to distinguish header cells from main table cells '''
        return self.id < 0