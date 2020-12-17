"""Suite of tests pertaining to the overall user interface"""
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from pytestqt import qtbot
from pytest_mock.plugin import MockerFixture
from time import sleep
from random import shuffle
import sys

sys.path.insert(1, 'src')
from Ui.user_interface import MainWindow
from Ui.prize_alert import PrizeAlert
from Ui.gui_manager import gui_manager, WindowType
from raffle import raffle

def test_import_ticket_names(qtbot: qtbot.QtBot, mocker: MockerFixture):
    """Tests the import ticket names feature"""
    mocker.patch('PyQt5.QtWidgets.QFileDialog.exec')
    mocker.patch('PyQt5.QtWidgets.QFileDialog.selectedFiles',
                 return_value=['examples/ticket_names.txt'])

    main_window = MainWindow()
    qtbot.addWidget(main_window)

    for value in WindowType:
        gui_manager.create_window(value)

    main_window.import_ticket_names_action.trigger()

    with open("examples/ticket_names.txt", 'r') as names_file:
        for ticket_label, ticket in zip(main_window.ticket_labels, raffle.tickets):
            line = names_file.readline().strip('\n')
            assert line in ticket_label.text()
            assert line == ticket.name

def test_import_prizes(qtbot: qtbot.QtBot, mocker: MockerFixture):
    """Tests the import prizes feature"""
    mocker.patch('PyQt5.QtWidgets.QFileDialog.exec')
    mocker.patch('PyQt5.QtWidgets.QFileDialog.selectedFiles',
                 return_value=['examples/prizes.txt'])

    # Open all windows
    main_window = MainWindow()
    for value in WindowType:
        gui_manager.create_window(value)

    for window in gui_manager.window_list:
        qtbot.addWidget(window)

    main_window.import_prizes_action.trigger()

    with open("examples/prizes.txt", 'r') as prize_file:
        for prize in raffle.prizes:
            splits = prize_file.readline().split(maxsplit=1)
            assert int(splits[0]) == prize.number
            assert splits[1] == prize.description

def test_prize_alerts(qtbot: qtbot.QtBot, mocker: MockerFixture):
    """Ensures that all prize alerts are displayed with the correct text"""
    test_import_prizes(qtbot, mocker)

    raffle.restart()

    ticket_numbers = list(range(1, 226))
    shuffle(ticket_numbers)
    prize_alert_count = 0
    for i, ticket_number in enumerate(ticket_numbers):
        raffle.draw_ticket(ticket_number)
        QApplication.processEvents()
        sleep(0.05)

        # If a prize alert is next...
        if raffle.get_prize_from_number(i + 2) is not None:
            # Ensure a prize alert is shown
            assert isinstance(gui_manager.window_list[-1], PrizeAlert)
            qtbot.addWidget(gui_manager.window_list[-1])
            prize_alert_count += 1

            # Ensure the text is correct
            next_prize = raffle.get_prize_from_number(i + 2)
            assert next_prize.description == gui_manager.window_list[-1].prize_description.text()
            qtbot.mouseClick(gui_manager.window_list[-1], Qt.LeftButton)

            # Force gui manager to do housekeeping
            gui_manager.create_window(WindowType.INVALID)

    assert len(raffle.prizes) == prize_alert_count
