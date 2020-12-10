"""Module providing overarching management of the user interfaces"""

from .user_interface import MainWindow

class GuiManager:
    """Class responsible for displaying windows and managing them"""
    def __init__(self):
        self.window_list = []

    def initialize(self):
        """Initializes the user interface"""
        self.window_list.append(MainWindow())
