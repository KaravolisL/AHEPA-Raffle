from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase
from Tickets.TicketList import TicketList

class ViewTicketsWindow(WindowBase):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('View Tickets')
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.makeLayout()


    def makeLayout(self):
        """
        
        """
        self.table = QTableWidget()
        self.table.setRowCount(225 + 1)
        self.table.setColumnCount(3)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(('Id', 'Ticket Names', 'Drawn?'))
        for i in range(1, 226):
            ticket = TicketList.getInstance().getTicket(i)
            self.table.setItem(i - 1, 0, QTableWidgetItem(str(i)))
            self.table.item(i - 1, 0).setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i - 1, 1, QTableWidgetItem(str(ticket.name)))
            self.table.item(i - 1, 1).setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i - 1, 2, QTableWidgetItem('Yes' if ticket.isDrawn() else 'No'))
            self.table.item(i - 1, 2).setTextAlignment(Qt.AlignCenter)
            
        self.table.setAlternatingRowColors(True)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 0, 0)