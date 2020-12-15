"""Module containing main user interface classes"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog

from Ui.custom_widgets import ClickableLabel
from Ui.alerts import WarningAlert
import Ui.gui_manager as gm
from raffle import raffle
import file_management
from constants import NUMBER_OF_TICKETS, APPLICATION_FONT_FAMILY
from debug_logger import get_logger

logger = get_logger(__name__)

class MainWindow(QtWidgets.QMainWindow):
    """Main window for the application"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/main_window.ui', self)

        # Set up the ticket labels
        self.ticket_labels = self.findChildren(ClickableLabel, QRegExp("label_[0-9]"))

        for i, label in enumerate(self.ticket_labels):
            # Fix the width, so word wrap works correctly
            label.setMaximumWidth(label.width())

            # Add the name to the label
            label.setText(str(raffle.tickets[i]))
            label.setFont(QFont(APPLICATION_FONT_FAMILY, 9))

            # We need to use a closure for i to ensure it copies it through the loop
            label.clicked.connect((lambda ticket_number: \
                                   lambda: self.ticket_label_clicked(ticket_number))(i + 1))

            # Restore progress
            if raffle.tickets[i].is_drawn():
                self.ticket_label_clicked(i + 1)

        # Set up the header cells
        self.last_ticket_drawn_label.clicked.connect(self.undo_button_clicked)
        self.update_header()

        # Update the background colors
        self.update_bg_color()

        # Connect menu bar actions
        self.restart_action.triggered.connect(self.restart_selected)
        self.import_ticket_names_action.triggered.connect(self.import_ticket_names_selected)
        self.import_prizes_action.triggered.connect(self.import_prizes_selected)
        self.view_ticket_names_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.VIEW_TICKETS)
        )
        self.view_prizes_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.VIEW_PRIZES)
        )
        self.edit_ticket_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.EDIT_TICKET)
        )
        self.edit_prize_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.EDIT_PRIZE)
        )
        self.change_bg_color_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.EDIT_BG_COLOR)
        )
        self.edit_prize_alert_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.EDIT_PRIZE_ALERT)
        )

        # Connect to signals
        for ticket in raffle.tickets:
            ticket.signals.data_changed.connect(self.refresh)
        raffle.signals.prize_next.connect(gm.gui_manager.create_prize_alert)

        self.showMaximized()

    def refresh(self):
        """Method used to refresh gui based on backend data"""
        # Update ticket names
        for i, label in enumerate(self.ticket_labels):
            label.setText(str(raffle.tickets[i]))

        # Update the header information
        self.update_header()

    def update_bg_color(self):
        """Updates the background color based on the values in the save file"""
        # Obtain current background colors
        header_bg_color, table_bg_color = \
            file_management.save_file_manager.get_bg_colors()

        self.tickets_remaining_label.setStyleSheet("QWidget { background-color: " +
                                                   header_bg_color + ";}")
        self.tickets_drawn_label.setStyleSheet("QWidget { background-color: " +
                                               header_bg_color + ";}")
        self.last_ticket_drawn_label.setStyleSheet("QWidget { background-color: " +
                                                   header_bg_color + ";}")

        for label in self.ticket_labels:
            if 'transparent' not in label.styleSheet():
                label.setStyleSheet("QWidget { background-color: " + table_bg_color + ";}")

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
        _, table_bg_color = file_management.save_file_manager.get_bg_colors()
        ticket_label.setStyleSheet("QWidget { background-color: " + table_bg_color + ";}")

        # Replace the ticket in the backend
        raffle.replace_ticket()

    def restart_selected(self):
        """Method called when the restart option is selected"""
        warning = WarningAlert("Restarting the raffle will cause all progress to"
                          " be lost! Are you sure you want to continue?")

        if warning.exec():
            logger.debug("Restarting...")
            while raffle.num_tickets_drawn != 0:
                self.undo_button_clicked()

    def import_ticket_names_selected(self):
        """Method called when the import ticket names option is selected"""
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setWindowTitle("Select Ticket Names")
        dialog.setNameFilter("Text files (*.txt)")

        if not dialog.exec():
            return

        # Try to import the names
        file_name = dialog.selectedFiles()[0]
        try:
            new_names = file_management.import_ticket_names(file_name)
        except file_management.FormatException:
            pass
        else:
            for ticket, new_name in zip(raffle.tickets, new_names):
                ticket.name = new_name
            file_management.save_file_manager.write_tickets_to_save_file(raffle.tickets)

    def import_prizes_selected(self):
        """Method called when the import prizes option is selected"""
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setWindowTitle("Select Prizes")
        dialog.setNameFilter("Text files (*.txt)")

        if not dialog.exec():
            return

        # Try to import the prizes
        file_name = dialog.selectedFiles()[0]
        try:
            new_prizes = file_management.import_prizes(file_name)
        except file_management.FormatException:
            pass
        else:
            raffle.prizes = new_prizes
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)

    # pylint: disable=invalid-name
    def resizeEvent(self, event) -> None:
        """Reevaluates max widths for labels"""
        super().resizeEvent(event)

        for label in self.ticket_labels:
            label.setMaximumWidth(self.frameGeometry().width() / 15)

    def closeEvent(self, event) -> None:
        """Closes all windows and the application"""
        super().closeEvent(event)
        gm.gui_manager.clear_windows()
    # pylint: enable=invalid-name
