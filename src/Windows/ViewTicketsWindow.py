from PyQt5.QtWidgets import QTableWidget, QHeaderView

from Windows.ViewWindow import ViewWindow
from Tickets.TicketList import TicketList
from Signals import Signals

class ViewTicketsWindow(ViewWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('View Tickets')

        Signals().ticketDrawn.connect(self.reevaluate)
        Signals().ticketNameChanged.connect(self.reevaluate)
        Signals().undoButtonClicked.connect(self.reevaluate)

        self.makeLayout()

    def makeLayout(self):
        """
        
        """
        self.table = QTableWidget()
        self.table.setRowCount(225)
        self.table.setColumnCount(3)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(('Id', 'Ticket Names', 'Number Drawn'))
        for i in range(1, 226):
            ticket = TicketList.getInstance().getTicket(i)
            ticketIdItem = self.make_item(i)
            ticketNameItem = self.make_item(ticket.name)
            ticketDrawnItem = self.make_item(ticket.numberDrawn if ticket.isDrawn() else '')
            self.table.setItem(i - 1, 0, ticketIdItem)
            self.table.setItem(i - 1, 1, ticketNameItem)
            self.table.setItem(i - 1, 2, ticketDrawnItem)
            
        self.table.setAlternatingRowColors(True)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table, 0, 0)

    def reevaluate(self, id):
        """
        
        """
        ticket = TicketList.getInstance().getTicket(id)
        self.table.item(id - 1, 1).setText(ticket.name)
        self.table.item(id - 1, 2).setText(str(ticket.numberDrawn) if ticket.isDrawn() else '')