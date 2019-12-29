from PyQt5.QtGui import QWidget, QSizePolicy, QGridLayout

from math import floor

from CellPkg.TableCell import TableCell
from FileManager.DataParser import dataParser
from Signals import Signals

class MainTable(QWidget):
    def __init__(self):
        super().__init__()

        # Create 2D array of blank cells, cells will be initialized by Controller initialize
        self.cells = [[TableCell(id=j+i) for i in range(0, 15)] for j in range(1, 226, 15)]

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(1)

        # Grow vertically and horizontally
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Adding cells to the layout
        for i in range(0, 15):
            for j in range(0, 15):
                self.layout.addWidget(self.cells[i][j], i, j)

        # Set color and connect signal
        self.setColor()
        Signals().colorChanged.connect(self.setColor)

    def getCell(self, id):
        """
        Helper method to obtain cell from 2D array given id
        :param int id: Id of cell to obtain
        """
        return self.cells[floor((id-1)/15)][(id-1)%15]

    def updateCell(self, text, id):
        """
        Helper method to update a cell with new text given an id.
        :param str text: New text for cell
        :param int id: Id of cell being updated
        """
        self.getCell(id).setText(text)

    def setColor(self):
        """
        This method is used to change the color of the main table's cell if
        it gets changed. It obtains this color from the save file.
        """
        mainTableColor = dataParser.getColor('mainTable')
        for row in self.cells:
            for cell in row:
                cell.setBackgroundColor(mainTableColor)
