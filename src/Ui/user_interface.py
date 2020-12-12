"""Module containing main user interface classes"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QRegExp

from Ui.custom_widgets import ClickableLabel
from raffle import raffle
from constants import NUMBER_OF_TICKETS
from logger import get_logger

logger = get_logger(__name__)

class MainWindow(QtWidgets.QMainWindow):
    """Main window for the application"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/main_window.ui', self)

        # Set up the ticket labels
        self.ticket_labels = self.findChildren(ClickableLabel, QRegExp("label_[0-9]"))

        for i, label in enumerate(self.ticket_labels):
            label.setText(str(raffle.tickets[i]))

            # We need to use a closure for i to ensure it copies it through the loop
            label.clicked.connect((lambda ticket_number: \
                                   lambda: self.ticket_label_clicked(ticket_number))(i + 1))

        # Set up the header cells
        self.last_ticket_drawn_label.clicked.connect(self.undo_button_clicked)

        self.update_header()

        self.showMaximized()

    def ticket_label_clicked(self, ticket_number: int):
        """Function called when a ticket label is clicked

        :param int ticket_number: Number of the ticket to be removed
        """
        # Make the ticket disapper
        ticket_label = self.ticket_labels[ticket_number - 1]
        ticket_label.setStyleSheet("QLabel {background-color: transparent; color: transparent;}")

        # Check whether this ticket has been drawn
        if not raffle.tickets[ticket_number - 1].is_drawn():
            raffle.draw_ticket(ticket_number)

        # Update the information in the header
        self.update_header()

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

    def undo_button_clicked(self):
        """Method to handle the undo action"""
        last_ticket_drawn = raffle.get_last_ticket_drawn()
        if last_ticket_drawn is None:
            return

        # Make ticket visible
        ticket_label = self.ticket_labels[last_ticket_drawn.number - 1]
        ticket_label.setStyleSheet("")

        # Replace the ticket in the backend
        raffle.replace_ticket()

        # Update the header
        self.update_header()
