"""Module containing views for tickets and prizes"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from raffle import raffle

class TicketsView(QtWidgets.QMainWindow):
    """Window used to view all tickets"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/view_window.ui', self)

        self.setWindowTitle("View Tickets")

        # Create the model
        self.model = None
        self.create_model()

        # Setup the view
        self.table_view.setAlternatingRowColors(True)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Connect to list signals
        raffle.signals.data_changed.connect(self.create_model)

        self.show()

    def create_model(self):
        """Creates the model to be used by the view"""
        # Create the model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(('Ticket Number', 'Ticket Names', 'Number Drawn'))
        for i, ticket in enumerate(raffle.tickets):
            row_items = [
                make_item(i + 1),
                make_item(ticket.name),
                make_item(ticket.number_drawn if ticket.is_drawn() else '')
            ]

            for j, item in enumerate(row_items):
                self.model.setItem(i, j, item)

            # Connect to signals
            ticket.signals.data_changed.connect(self.refresh)

        self.table_view.setModel(self.model)

    def refresh(self) -> None:
        """Runs through cells and updates them based on current data"""
        for i, ticket in enumerate(raffle.tickets):
            self.model.item(i, 1).setText(ticket.name)
            self.model.item(i, 2).setText(str(ticket.number_drawn) if ticket.is_drawn() else '')

class PrizesView(QtWidgets.QMainWindow):
    """Window used to view all tickets"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/view_window.ui', self)

        self.setWindowTitle("View Prizes")

        # Create the model
        self.model = None
        self.create_model()

        # Setup the view
        self.table_view.setAlternatingRowColors(True)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Connect to list signals
        raffle.signals.data_changed.connect(self.create_model)

        self.show()

    def create_model(self):
        """Creates the model for the view"""
        # Create the model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(('Prize Number', 'Prize Description'))
        for i, prize in enumerate(raffle.prizes):
            row_items = [
                make_item(prize.number),
                make_item(prize.description)
            ]

            for j, item in enumerate(row_items):
                self.model.setItem(i, j, item)

            # Connect to signals
            prize.signals.data_changed.connect(self.refresh)

        self.table_view.setModel(self.model)

    def refresh(self) -> None:
        """Runs through cells and updates them based on current data"""
        for i, prize in enumerate(raffle.prizes):
            self.model.item(i, 0).setText(str(prize.number))
            self.model.item(i, 1).setText(prize.description)

def make_item(text):
    """Helper method used to create table cells

    :param str text: Text for the cell
    :returns: A prepared item ready to be added to a table
    :rtype: QTableWidgetItem
    """
    item = QStandardItem(str(text))
    item.setTextAlignment(Qt.AlignCenter)
    item.setFlags(Qt.ItemIsEnabled)
    return item
