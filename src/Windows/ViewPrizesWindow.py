from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.ViewWindow import ViewWindow
import Prizes.PrizeApi as PrizeApi
from Signals import Signals

class ViewPrizesWindow(ViewWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('View Prizes')
        self.prizeList = PrizeApi.getList()

        Signals().prizeChanged.connect(self.reevaluate)

        self.makeLayout()

    def makeLayout(self):
        """

        """
        self.table = QTableWidget()
        self.table.setRowCount(len(self.prizeList))
        self.table.setColumnCount(2)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(('Prize Number', 'Prize Description'))
        for i, prize in enumerate(self.prizeList):
            prizeNumberItem = self.make_item(prize.number)
            prizeDescItem = self.make_item(prize.description)
            self.table.setItem(i, 0, prizeNumberItem)
            self.table.setItem(i, 1, prizeDescItem)

        self.table.setAlternatingRowColors(True)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 0, 0)

    def reevaluate(self, prizeNumber):
        """
        
        """
        print('Signal received for prize number {}'.format(prizeNumber))
        for i in range(self.table.rowCount()):
            print(self.table.item(i, 0).text())
            if int(self.table.item(i, 0).text()) == prizeNumber:
                # We've found the correct line
                associatedPrize =  PrizeApi.getAssociatedPrize(prizeNumber)
                print(associatedPrize)
                if associatedPrize == None:
                    # Prize was deleted
                    self.table.removeRow(i)
                    break
                else:
                    # Prize was changed
                    self.table.item(i, 1).setText(associatedPrize.description)
                    break
        else:
            # Prize was added
            numOfPrizes = len(self.prizeList)
            addedPrize = PrizeApi.getAssociatedPrize(prizeNumber)
            assert(addedPrize != None), 'Prize was not added'
            self.table.setRowCount(numOfPrizes)
            prizeNumberItem = self.make_item(addedPrize.number)
            prizeDescItem = self.make_item(addedPrize.description)
            self.table.setItem(numOfPrizes - 1, 0, prizeNumberItem)
            self.table.setItem(numOfPrizes - 1, 1, prizeDescItem)
