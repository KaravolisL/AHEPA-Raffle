"""Module providing overarching management of the user interfaces"""

from enum import Enum
from typing import List

from PyQt5.QtWidgets import QMainWindow

import Ui.user_interface as user_interface
import Ui.view_windows as view_windows
import Ui.edit_windows as edit_windows
import Ui.prize_alert as prize_alert
import Ui.info_windows as info_windows
from data_classes import Prize
from debug_logger import get_logger

logger = get_logger(__name__)

class WindowType(Enum):
    """Enumerated type for auxiliary windows"""
    VIEW_TICKETS = 0
    VIEW_PRIZES = 1
    EDIT_TICKET = 2
    EDIT_PRIZE = 3
    EDIT_PRIZE_ALERT = 4
    EDIT_BG_COLOR = 5
    PRIZE_ALERT = 6
    ABOUT = 7
    CONTROL_PANEL = 8
    INVALID = 9

class GuiManager:
    """Class responsible for displaying windows and managing them"""
    def __init__(self):
        self.window_list: List[QMainWindow] = []

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
        elif window_type == WindowType.ABOUT:
            self.window_list.append(info_windows.About())
        elif window_type == WindowType.CONTROL_PANEL:
            self.window_list.append(view_windows.ControlPanel())

        # Clean out closed windows
        self.window_list = [window for window in self.window_list if window.isVisible()]

    def create_prize_alert(self, prize: Prize):
        """Creates a prize alert window with the given text

        :param Prize prize: Prize to be used
        """
        logger.debug("Creating alert for prize number %d", prize.number)
        window = prize_alert.PrizeAlert(prize.description)

        # Clean out closed windows
        self.window_list = [x for x in self.window_list if x.isVisible()]

        self.window_list.append(window)

        # Fix the sizing
        screen = self.window_list[0].screen()
        screen_width = screen.size().width()
        screen_height = screen.size().height()
        window.setGeometry(0, 0, int(screen_width * 2/3), int(screen_height * 2/3))

        # Center it
        frame_geometry = window.frameGeometry()
        center_point = screen.availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        window.move(frame_geometry.topLeft())

        window.show()

    def force_main_window_refresh(self):
        """Forces the main window to refresh itself"""
        for window in self.window_list:
            if isinstance(window, user_interface.MainWindow):
                window.update_bg_color()

    def clear_windows(self):
        """Deletes all open windows"""
        for window in reversed(self.window_list):
            window.close()
            del window
        self.window_list.clear()

gui_manager = GuiManager()
