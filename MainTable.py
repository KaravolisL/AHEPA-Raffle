from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Cell import Cell

class MainTable(QGridLayout):
    def __init__(self):
        super().__init__()

        # Create 2D array of cells with corresponding ids
        self.cells = [[Cell(str(i+j), i+j) for i in range(0, 15)] for j in range(1, 256, 15)]

        for i in range(0, 15):
            for j in range(0, 15):
                self.addWidget(self.cells[i][j], i, j)