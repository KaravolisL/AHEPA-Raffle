"""Module containing windows used for editing aspects of the program"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

from constants import NUMBER_OF_TICKETS
from raffle import raffle

class TicketEdit(QtWidgets.QMainWindow):
    """Window used to edit a ticket"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/edit_ticket.ui', self)

        # Set validator
        self.ticket_number_line_edit.setValidator(QIntValidator(1, NUMBER_OF_TICKETS))

        # Connect to signals
        self.ticket_number_line_edit.textEdited.connect(self.ticket_number_edited)
        self.button_box.clicked.connect(self.apply)

        self.show()

    def ticket_number_edited(self):
        """Method to handle the user entering a ticket number"""
        if self.ticket_number_line_edit.hasAcceptableInput():
            ticket_number = int(self.ticket_number_line_edit.text())
            self.ticket_name_line_edit.setText(raffle.tickets[ticket_number - 1].name)
        else:
            self.ticket_number_line_edit.clear()

    def apply(self):
        """Method to apply the name change to the ticket"""
        if self.ticket_number_line_edit.hasAcceptableInput():
            ticket_number = int(self.ticket_number_line_edit.text())
            raffle.tickets[ticket_number - 1].name = self.ticket_name_line_edit.text()

    # pylint: disable=invalid-name
    def keyPressEvent(self, event):
        """Connects the enter key to changeNameEvent
        
        :param QKeyEvent event: Key that was pressed
        """
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.apply()
    # pylint: enable=invalid-name
