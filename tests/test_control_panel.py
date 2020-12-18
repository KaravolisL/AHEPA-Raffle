"""Suite of tests to verify the control panel window"""
# pylint: disable=wrong-import-order,wrong-import-position
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from pytestqt import qtbot
from pytest_mock.plugin import MockerFixture
from time import sleep
from random import shuffle
import sys

sys.path.insert(1, 'src')
from Ui.gui_manager import gui_manager, WindowType
from raffle import raffle

def test_import_ticket_names(qtbot: qtbot.QtBot, mocker: MockerFixture):
    """Tests the import ticket names feature"""
    gui_manager.clear_windows()

    gui_manager.initialize()
    gui_manager.create_window(WindowType.CONTROL_PANEL)

    for window in gui_manager.window_list:
        qtbot.addWidget(window)

    # Import ticket names and prizes
    mocker.patch('PyQt5.QtWidgets.QFileDialog.exec')
    mocker.patch('PyQt5.QtWidgets.QFileDialog.selectedFiles',
                 return_value=['examples/ticket_names.txt'])
    gui_manager.window_list[0].import_ticket_names_action.trigger()
    mocker.patch('PyQt5.QtWidgets.QFileDialog.selectedFiles',
                 return_value=['examples/prizes.txt'])
    gui_manager.window_list[0].import_prizes_action.trigger()

    # Restart before starting
    raffle.restart()

    # Mock prize alerts
    mocker.patch('Ui.prize_alert.PrizeAlert')

    control_panel = gui_manager.window_list[1]

    ticket_numbers = list(range(1, 226))
    shuffle(ticket_numbers)
    for i, ticket_number in enumerate(ticket_numbers):
        # Draw the next ticket
        control_panel.ticket_number_line_edit.clear()
        qtbot.keyClicks(control_panel.ticket_number_line_edit, str(ticket_number))
        qtbot.mouseClick(control_panel.draw_ticket_button, Qt.LeftButton)
        QApplication.processEvents()
        sleep(0.05)

        # Check the header info
        assert "Tickets Remaining: {}".format(len(ticket_numbers) - (i + 1)) == \
                control_panel.tickets_remaining_label.text()
        assert "Tickets Drawn: {}".format(i + 1) == control_panel.tickets_drawn_label.text()
        assert "Last Ticket Drawn: {}".format(ticket_number) == \
                control_panel.last_ticket_drawn_label.text()

        # Go through the tickets and do some checks
        for j, _ in enumerate(ticket_numbers):
            # Enter the ticket number
            control_panel.ticket_number_line_edit.clear()
            qtbot.keyClicks(control_panel.ticket_number_line_edit, str(ticket_numbers[j]))
            # If this ticket has been drawn
            if j <= i:
                assert str(j + 1) in control_panel.number_drawn_label.text()
            else:
                assert 'Not Drawn Yet' in control_panel.number_drawn_label.text()

        # Check the prize that is displayed
        next_prize = None
        for j in range(i + 2, len(ticket_numbers) + 1):
            next_prize = raffle.get_prize_from_number(j)
            if next_prize is not None:
                break

        if next_prize is not None:
            assert str(next_prize.number) in control_panel.next_prize_number_label.text()
            assert str(next_prize.description) in control_panel.next_prize_description_label.text()
        else:
            assert control_panel.next_prize_number_label.text() == "-"
            assert control_panel.next_prize_description_label.text() == "-"
