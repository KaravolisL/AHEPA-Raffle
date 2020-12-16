"""Module providing overarching management of the user interfaces"""

from enum import Enum

import Ui.user_interface as user_interface
import Ui.view_windows as view_windows
import Ui.edit_windows as edit_windows
import Ui.prize_alert as prize_alert
from data_classes import Prize

class WindowType(Enum):
    """Enumerated type for auxiliary windows"""
    VIEW_TICKETS = 0
    VIEW_PRIZES = 1
    EDIT_TICKET = 2
    EDIT_PRIZE = 3
    EDIT_PRIZE_ALERT = 4
    EDIT_BG_COLOR = 5
    PRIZE_ALERT = 6

class GuiManager:
    """Class responsible for displaying windows and managing them"""
    def __init__(self):
        self.window_list = []

    def initialize(self):
        """Initializes the user interface"""
        self.window_list.append(user_interface.MainWindow())

    def create_window(self, window_type: WindowType):
        """Creates a window and adds it to the list

        :param WindowType window_type: Type of window to make
        """
        if window_type == WindowType.VIEW_TICKETS:
            self.window_list.append(view_windows.TicketsView())
        elif window_type == WindowType.VIEW_PRIZES:
            self.window_list.append(view_windows.PrizesView())
        elif window_type == WindowType.EDIT_TICKET:
            self.window_list.append(edit_windows.TicketEdit())
        elif window_type == WindowType.EDIT_PRIZE:
            self.window_list.append(edit_windows.PrizeEdit())
        elif window_type == WindowType.EDIT_PRIZE_ALERT:
            self.window_list.append(edit_windows.PrizeAlertEdit())
        elif window_type == WindowType.EDIT_BG_COLOR:
            self.window_list.append(edit_windows.BackgroundColorEdit())

    def create_prize_alert(self, prize: Prize):
        """Creates a prize alert window with the given text

        :param str text: Text to be displayed
        """
        self.window_list.append(prize_alert.PrizeAlert(prize.description))

    def force_main_window_refresh(self):
        """Forces the main window to refresh itself"""
        for window in self.window_list:
            if isinstance(window, user_interface.MainWindow):
                window.update_bg_color()

    def clear_windows(self):
        """Deletes all open windows"""
        for window in reversed(self.window_list):
            window.close()
        self.window_list.clear()

gui_manager = GuiManager()
