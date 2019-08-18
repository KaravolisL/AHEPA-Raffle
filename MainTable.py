from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Cell import Cell
from RaffleList import RaffleList

class MainTable(QGridLayout):
    def __init__(self):
        super().__init__()

        # Create 2D array of cells with corresponding ids
        self.cells = [[Cell(ticket = RaffleList.fullList[i+j-1]) for i in range(0, 15)] for j in range(1, 226, 15)]

        # Adding cells to the layout
        for i in range(0, 15):
            for j in range(0, 15):
                print(str(self.cells[i][j]))
                self.addWidget(self.cells[i][j], i, j)

        # Set spacing
        self.setSpacing(1)