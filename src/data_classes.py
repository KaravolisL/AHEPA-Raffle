"""Module containing classes meant only for data"""

from typing import Tuple, Union
from PyQt5.QtCore import QObject, pyqtSignal

class Prize:
    """Class to represent a single prize"""
    def __init__(self, number, description = ""):
        self._number = number
        self._description = description
        self.signals = Signals()

    @property
    def number(self):
        """Returns the number property"""
        return self._number

    @number.setter
    def number(self, val: int):
        self._number = val
        self.signals.data_changed.emit()

    @property
    def description(self):
        """Returns the description property"""
        return self._description

    @description.setter
    def description(self, val: str):
        self._description = val
        self.signals.data_changed.emit()

    def __str__(self):
        return str(self.number) + " " + self.description

class Ticket:
    """Class to represent a single ticket"""
    def __init__(self, number = 0, name = "", number_drawn = 0):
        self._name = name
        self._number = number
        self._number_drawn = number_drawn
        self.signals = Signals()

    @property
    def name(self):
        """Returns the number property"""
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val
        self.signals.data_changed.emit()

    @property
    def number(self):
        """Returns the number property"""
        return self._number

    @number.setter
    def number(self, val: int):
        self._number = val
        self.signals.data_changed.emit()

    @property
    def number_drawn(self):
        """Returns the description property"""
        return self._number_drawn

    @number_drawn.setter
    def number_drawn(self, val: int):
        self._number_drawn = val
        self.signals.data_changed.emit()

    def __str__(self):
        return str(self.number) + '\n' + self.name

    def is_drawn(self) -> bool:
        """Returns whether this ticket has been drawn or not"""
        return self.number_drawn != 0

    @staticmethod
    def is_acceptable_name(name: str) -> str:
        """Returns an invalid character if one was found"""
        if ',' in name:
            return ','
        return ''

class Signals(QObject):
    """Class to hold signals"""
    data_changed = pyqtSignal()
    prize_next = pyqtSignal(Prize)
