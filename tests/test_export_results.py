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
from Ui.gui_manager import gui_manager
from raffle import raffle

def test_import_ticket_names(qtbot: qtbot.QtBot, mocker: MockerFixture):
    """Tests the import ticket names feature"""
    gui_manager.clear_windows()

    gui_manager.initialize()

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

    # Draw all of the tickets in a random order
    ticket_numbers = list(range(1, 226))
    shuffle(ticket_numbers)
    for ticket_number in ticket_numbers:
        qtbot.mouseClick(gui_manager.window_list[0].ticket_labels[ticket_number - 1], Qt.LeftButton)

        # Draw the next ticket
        QApplication.processEvents()
        sleep(0.01)

    # Export the results to a csv file
    mocker.patch('PyQt5.QtWidgets.QFileDialog.getSaveFileName',
                 return_value=['results.csv', 'CSV files (*.csv)'])
    gui_manager.window_list[0].export_results_action.trigger()
    QApplication.processEvents()

    with open("results.csv", 'r') as results:
        for i, ticket_number in enumerate(ticket_numbers):
            values = results.readline().strip().split(',')

            # Verify information is present in results
            assert values[0] == str(i + 1)
            assert values[1] == str(ticket_number)
            assert values[2] == raffle.tickets[ticket_number - 1].name

            if raffle.get_prize_from_number(i + 1):
                assert values[3] == raffle.get_prize_from_number(i + 1).description.strip()
