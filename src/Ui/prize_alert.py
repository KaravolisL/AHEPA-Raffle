"""Module containing the prize alert window"""

import threading

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from constants import APPLICATION_FONT_FAMILY
import file_management

class PrizeAlert(QtWidgets.QMainWindow):
    """Window to be displayed prior to a prize being given"""
    def __init__(self, text: str):
        super().__init__()
        uic.loadUi('src/Ui/prize_alert.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Obtain the preferences
        bg_color, font_size, delay = \
            file_management.save_file_manager.get_prize_alert_preferences()

        # Set the text
        self.prize_description.setText(text)
        self.prize_description.setFont(QFont(APPLICATION_FONT_FAMILY, font_size))

        # Set the background color
        self.setStyleSheet('QWidget {background-color: ' + bg_color +  ';}')

        self.show()

        # Start a timer for closing the PrizeAlert
        self.delay_thread = threading.Timer(delay, self.close)
        self.delay_thread.start()

    # pylint: disable=invalid-name
    def mousePressEvent(self, event):
        """Clicking will cause the alert to disappear"""
        super().mousePressEvent(event)
        self.close()

    def keyPressEvent(self, event):
        """Pressing any key will cause the alert to disapper"""
        super().keyPressEvent(event)
        self.close()

    def close(self):
        """Closes the window and cancels any outstanding timers"""
        super().close()
        self.delay_thread.cancel()
    # pylint: enable=invalid-name
