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
            label.clicked.connect((lambda ticket_number: lambda: self.ticket_label_clicked(ticket_number))(i + 1))

        self.showMaximized()

    def ticket_label_clicked(self, ticket_number: int):
        """Function called when a ticket label is clicked
        
        :param int ticket_number: Number of the ticket to be removed
        """
        raffle.draw_ticket(ticket_number)
