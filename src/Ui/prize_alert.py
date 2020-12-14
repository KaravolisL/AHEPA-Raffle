"""Module containing the prize alert window"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt


class PrizeAlert(QtWidgets.QMainWindow):
    """Window to be displayed prior to a prize being given"""
    def __init__(self, text: str):
        super().__init__()
        uic.loadUi('src/Ui/prize_alert.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set the text
        self.prize_description.setText(text)

        self.show()