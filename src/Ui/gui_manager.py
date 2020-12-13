"""Module providing overarching management of the user interfaces"""

from enum import Enum

import Ui.user_interface as user_interface
import Ui.view_windows as view_windows

class WindowType(Enum):
    """Enumerated type for auxiliary windows"""
    VIEW_TICKETS = 0
    VIEW_PRIZES = 1

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

    def clear_windows(self):
        """Deletes all open windows"""
        self.window_list.clear()

gui_manager = GuiManager()