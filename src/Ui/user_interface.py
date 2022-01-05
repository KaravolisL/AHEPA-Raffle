"""Module containing main user interface classes"""

from datetime import datetime
import os

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog

import openpyxl

from Ui.custom_widgets import ClickableLabel
from Ui.alerts import WarningAlert, Alert
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
        self.setWindowTitle("AHEPA Raffle " + str(datetime.now().year))

        # Set up the ticket labels
        self.ticket_labels = self.findChildren(ClickableLabel, QRegExp("label_[0-9]"))

        for i, label in enumerate(self.ticket_labels):
            # Fix the width, so word wrap works correctly
            label.setMaximumWidth(label.width())

            # Add the name to the label
            label.setText(str(raffle.tickets[i]))
            label.setFont(QFont(APPLICATION_FONT_FAMILY, 9))

            # We need to use a closure for i to ensure it copies it through the loop
            # pylint: disable=cell-var-from-loop
            label.clicked.connect(lambda self=self, ticket_number=(i + 1): \
                                    self.ticket_label_clicked(ticket_number))
            # pylint: enable=cell-var-from-loop

        # Set up the header cells
        self.last_ticket_drawn_label.clicked.connect(MainWindow.undo_button_clicked)

        # Update the background colors
        self.update_bg_color()
        self.refresh()

        # Connect menu bar actions
        self.restart_action.triggered.connect(self.restart_selected)
        self.clear_ticket_names_action.triggered.connect(self.clear_ticket_names)
        self.clear_prizes_action.triggered.connect(self.clear_prizes)
        self.import_ticket_names_action.triggered.connect(self.import_ticket_names_selected)
        self.import_prizes_action.triggered.connect(self.import_prizes_selected)
        self.export_results_action.triggered.connect(self.export_results_selected)
        self.view_ticket_names_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.VIEW_TICKETS)
        )
        self.view_prizes_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.VIEW_PRIZES)
        )
        self.control_panel_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.CONTROL_PANEL)
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
        self.full_screen_action.triggered.connect(self.showFullScreen)
        self.maximize_action.triggered.connect(self.showMaximized)
        self.about_action.triggered.connect(
            lambda: gm.gui_manager.create_window(gm.WindowType.ABOUT)
        )

        # Connect to signals
        for ticket in raffle.tickets:
            ticket.signals.data_changed.connect(self.refresh)
        raffle.signals.prize_next.connect(gm.gui_manager.create_prize_alert)

        self.showMaximized()

        # Check if the save file was corrupted
        if file_management.save_file_manager.save_file_corrupted:
            alert = Alert("The save file was corrupted. The program has been reset")
            alert.setWindowTitle("Corrupted Save File")
            alert.exec()

    def refresh(self):
        """Method used to refresh gui based on backend data"""
        _, table_bg_color = file_management.save_file_manager.get_bg_colors()

        # Update ticket names
        for i, label in enumerate(self.ticket_labels):
            label.setText(str(raffle.tickets[i]))

            if raffle.tickets[i].is_drawn():
                label.setStyleSheet("QLabel {background-color: transparent; color: transparent;}")
            else:
                label.setStyleSheet("QWidget { background-color: " + table_bg_color + ";}")

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
        # Check whether this ticket has been drawn
        if not raffle.tickets[ticket_number - 1].is_drawn():
            assert 'transparent' not in self.ticket_labels[ticket_number - 1].styleSheet()
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

    @classmethod
    def undo_button_clicked(cls):
        """Method to handle the undo action"""
        last_ticket_drawn = raffle.get_last_ticket_drawn()
        if last_ticket_drawn is None:
            return

        # Replace the ticket in the backend
        raffle.replace_ticket()

    def restart_selected(self):
        """Method called when the restart option is selected"""
        warning = WarningAlert("Restarting the raffle will cause all progress to"
                          " be lost! Are you sure you want to continue?")

        if warning.exec():
            logger.debug("Restarting...")

            for ticket in raffle.tickets:
                ticket.signals.data_changed.disconnect(self.refresh)

            while raffle.num_tickets_drawn != 0:
                MainWindow.undo_button_clicked()

            for ticket in raffle.tickets:
                ticket.signals.data_changed.connect(self.refresh)

            self.refresh()

    def clear_ticket_names(self):
        """Clears the names of all the tickets"""
        warning = WarningAlert("The names of all tickets will be deleted! "
                               "Are you sure you want to continue?")

        if warning.exec():
            for ticket in raffle.tickets:
                ticket.signals.data_changed.disconnect(self.refresh)
                ticket.name = ""
                ticket.signals.data_changed.connect(self.refresh)

            self.refresh()
            file_management.save_file_manager.write_tickets_to_save_file(raffle.tickets)

    @classmethod
    def clear_prizes(cls):
        """Clears all the prizes in the list"""
        warning = WarningAlert("All prizes will be deleted! Are you sure"
                               " you want to continue?")

        if warning.exec():
            raffle.prizes.clear()
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)

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
            alert = Alert("Tickets failed to import! Check the formatting of your file.")
            alert.setWindowTitle("Import Failed")
            alert.exec()
        else:
            for ticket, new_name in zip(raffle.tickets, new_names):
                ticket.signals.data_changed.disconnect(self.refresh)
                ticket.name = new_name
                ticket.signals.data_changed.connect(self.refresh)
            self.refresh()
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
            alert = Alert("Prizes failed to import! Check the formatting of your file.")
            alert.setWindowTitle("Import Failed")
            alert.exec()
        else:
            raffle.prizes = new_prizes
            file_management.save_file_manager.write_prizes_to_save_file(raffle.prizes)

    def export_results_selected(self): # pylint: disable=too-many-locals
        """Method called when user selects the export results action"""
        save_file_name, extension = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                          "Save file name",
                                                                          "",
                                                                          "CSV files (*.csv);; \
                                                                          Xlsx files (*.xlsx)")
        if not save_file_name:
            return

        # Adjust the file extension if the user hasn't added it themselves
        file_format = 'csv' if 'csv' in extension else 'xlsx'
        if os.path.splitext(save_file_name)[1] not in ('.csv', '.xlsx'):
            save_file_name += '.' + file_format
        logger.debug("Writing results to %s", save_file_name)

        # Gather results
        results = ""
        for i in range(1, raffle.num_tickets_drawn + 1):
            for ticket in raffle.tickets:
                if ticket.number_drawn == i:
                    entry = ",".join(map(str, [i,
                                               ticket.number,
                                               ticket.name]))
                    associated_prize = raffle.get_prize_from_number(ticket.number_drawn)
                    if associated_prize is not None:
                        entry += "," + associated_prize.description.strip('\n')

                    results += entry + '\n'

        # Write to file based on selected format
        if file_format == 'csv':
            with open(save_file_name, 'w', encoding='UTF-8') as save_file:
                save_file.write(results)
        else:
            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            lines = results.splitlines()
            for row, line in enumerate(lines):
                print(row)
                for col, value in enumerate(line.split(',')):
                    worksheet.cell(row + 1, col + 1, value)
            workbook.save(save_file_name)

    # pylint: disable=invalid-name
    def resizeEvent(self, event) -> None:
        """Reevaluates max widths for labels"""
        super().resizeEvent(event)

        for label in self.ticket_labels:
            label.setMaximumWidth(int(self.frameGeometry().width() / 15))

    def closeEvent(self, event) -> None:
        """Closes all windows and the application"""
        super().closeEvent(event)
        raffle.signals.prize_next.disconnect()
        gm.gui_manager.clear_windows()

    def showFullScreen(self) -> None:
        """Makes the window full screen and removes the menu bar"""
        super().showFullScreen()
        self.menu_bar.hide()

    def keyPressEvent(self, event) -> None:
        """Handles key presses by the user"""
        super().keyPressEvent(event)
        logger.debug("User pressed %d", event.key())
        if (event.key() == Qt.Key_Escape) and self.isFullScreen():
            self.showMaximized()
            self.menu_bar.show()
    # pylint: enable=invalid-name
