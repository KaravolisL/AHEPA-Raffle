"""Module containing windows used for editing aspects of the program"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator

from constants import NUMBER_OF_TICKETS
from raffle import raffle
from data_classes import Prize
import file_management

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
            file_management.save_file_manager.write_tickets_to_save_file(raffle.tickets)

    # pylint: disable=invalid-name
    def keyPressEvent(self, event):
        """Connects the enter key to changeNameEvent

        :param QKeyEvent event: Key that was pressed
        """
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.apply()
    # pylint: enable=invalid-name

class PrizeEdit(QtWidgets.QMainWindow):
    """Window used to edit a prize"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/edit_prize.ui', self)

        # Set validator
        self.prize_number_line_edit.setValidator(QIntValidator(1, NUMBER_OF_TICKETS))

        # Connect to signals
        self.prize_number_line_edit.textEdited.connect(self.prize_number_edited)
        self.add_prize_button.clicked.connect(self.add_prize)
        self.delete_prize_button.clicked.connect(self.delete_prize)
        self.change_description_button.clicked.connect(self.change_description)

        self.show()

    def prize_number_edited(self):
        """Method to handle the user entering a prize number"""
        if self.prize_number_line_edit.hasAcceptableInput():
            prize_number = int(self.prize_number_line_edit.text())
            prize = raffle.get_prize_from_number(prize_number)

            # Update the description and enable correct buttons
            if prize is not None:
                self.prize_description_line_edit.setText(prize.description)
                self.add_prize_button.setEnabled(False)
                self.delete_prize_button.setEnabled(True)
                self.change_description_button.setEnabled(True)
            else:
                self.prize_description_line_edit.clear()
                self.add_prize_button.setEnabled(True)
                self.delete_prize_button.setEnabled(False)
                self.change_description_button.setEnabled(False)

    def add_prize(self):
        """Method to add a prize given the user's input"""
        if self.prize_number_line_edit.hasAcceptableInput():
            prize_number = int(self.prize_number_line_edit.text())
            raffle.prizes.append(Prize(prize_number,
                                       self.prize_description_line_edit.text()))
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)
        self.prize_number_edited()

    def delete_prize(self):
        """Method called to delete a prize from the list"""
        if self.prize_number_line_edit.hasAcceptableInput():
            prize_number = int(self.prize_number_line_edit.text())
            raffle.prizes = [prize for prize in raffle.prizes if prize.number != prize_number]
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)
        self.prize_number_edited()

    def change_description(self):
        """Method called to change the description of a given prize"""
        if self.prize_number_line_edit.hasAcceptableInput():
            prize_number = int(self.prize_number_line_edit.text())
            prize = raffle.get_prize_from_number(prize_number)
            prize.description = self.prize_description_line_edit.text()
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)
        self.prize_number_edited()
