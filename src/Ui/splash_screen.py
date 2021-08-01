"""Module for the application's splash screen"""

from datetime import datetime

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

SPLASH_SCREEN_DURATION = 5

class SplashScreen(QtWidgets.QMainWindow):
    """Window to be displayed upon application startup"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/splash_screen.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setStyleSheet("MainWindow {border: 5px solid #555;}")
        self.label.setText("AHEPA Raffle " + str(datetime.now().year))

        self.show()
