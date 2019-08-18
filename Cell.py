from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class Cell(QLabel):
    def __init__(self, text = None, id = 0):
        super().__init__()
        # Set text and id
        self.setText(text)
        self.id = id

        # Set sizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)

        # DEBUG
        self.setStyleSheet("QLabel {background-color: red;}")

    def setId(self, id):
        self.id = id

    def setBackgroundColor(self, color):
        ''' DEBUG '''
        self.setStyleSheet("QLabel {background-color: " + str(color) + ";}")
    
    def getId(self, id):
        return self.id