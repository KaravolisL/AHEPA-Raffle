"""Module containing views for tickets and prizes"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QStandardItem, QStandardItemModel

from raffle import raffle
from constants import NUMBER_OF_TICKETS

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

class ControlPanel(QtWidgets.QMainWindow):
    """Window used by the user to control the application"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/control_panel.ui', self)

        # Set validator
        self.ticket_number_line_edit.setValidator(QIntValidator(1, NUMBER_OF_TICKETS))

        # Update the interface
        self.refresh()

        # Connect to signals
        for ticket in raffle.tickets:
            ticket.signals.data_changed.connect(self.refresh)
        raffle.signals.data_changed.connect(self.refresh)
        self.replace_last_ticket_button.clicked.connect(ControlPanel.undo_button_clicked)
        self.draw_ticket_button.clicked.connect(self.draw_ticket)
        self.ticket_number_line_edit.textEdited.connect(self.ticket_number_edited)

        self.show()

    def refresh(self):
        """Updates the information displayed in the interface"""
        # Updates the labels in the header
        self.update_header()

        next_prize = min([prize for prize in raffle.prizes if prize.number > raffle.num_tickets_drawn], key=lambda x: x.number, default=None)
        if next_prize is not None:
            self.next_prize_number_label.setText("Ticket Number: {}".format(next_prize.number))
            self.next_prize_description_label.setText(next_prize.description)
        else:
            self.next_prize_number_label.setText("-")
            self.next_prize_description_label.setText("-")

        self.ticket_number_edited()

    def update_header(self):
        """Method used to update the information in the header cells"""
        num_tickets_remaining = NUMBER_OF_TICKETS - raffle.num_tickets_drawn
        self.tickets_remaining_label.setText("Tickets Remaining: {}".format(num_tickets_remaining))

        self.tickets_drawn_label.setText("Tickets Drawn: {}".format(raffle.num_tickets_drawn))

        last_ticket_drawn = raffle.get_last_ticket_drawn()
        if last_ticket_drawn is None:
            self.last_ticket_drawn_label.setText("Last Ticket Drawn: ")
        else:
            self.last_ticket_drawn_label.setText(
                "Last Ticket Drawn: {}".format(last_ticket_drawn.number)
            )

    def ticket_number_edited(self):
        """Method to handle the user entering a ticket number"""
        if self.ticket_number_line_edit.hasAcceptableInput():
            ticket = raffle.tickets[int(self.ticket_number_line_edit.text()) - 1]
            self.ticket_name_label.setText("Ticket Name: \n{}".format(ticket.name))
            if ticket.is_drawn():
                self.number_drawn_label.setText("Number Drawn: \n{}".format(ticket.number_drawn))
            else:
                self.number_drawn_label.setText("Number Drawn: \nNot Drawn Yet")
        else:
            self.ticket_name_label.setText("Ticket Name: \n")
            self.number_drawn_label.setText("Number Drawn: \n")

    def draw_ticket(self):
        """Function called when a ticket label is clicked

        :param int ticket_number: Number of the ticket to be removed
        """
        if self.ticket_number_line_edit.hasAcceptableInput():
            ticket_number = int(self.ticket_number_line_edit.text())
            # Check whether this ticket has been drawn
            if not raffle.tickets[ticket_number - 1].is_drawn():
                raffle.draw_ticket(ticket_number)
                self.refresh()

    @classmethod
    def undo_button_clicked(cls):
        """Method to handle the undo action"""
        last_ticket_drawn = raffle.get_last_ticket_drawn()
        if last_ticket_drawn is None:
            return

        # Replace the ticket in the backend
        raffle.replace_ticket()
