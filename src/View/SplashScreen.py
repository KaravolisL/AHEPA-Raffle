from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

from datetime import datetime
from time import sleep

from Windows.WindowBase import WindowBase

class SplashScreen(WindowBase):

    # How long to show the splash screen
    SPLASH_SCREEN_DELAY_IN_SEC = 3

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.makeLayout()

        self.setSizeAndCenter(2/4,2/4)

    def makeLayout(self):
        self.desc = QLabel(str(datetime.now().year) + " AHEPA Scholarship Banquet")
        self.desc.setAlignment(Qt.AlignCenter)
        self.desc.setFont(QFont('Arial', 20))

        self.pictureLabel = QLabel()
        pixmap = QPixmap(r'images/Logo.jpg')
        self.pictureLabel.setPixmap(pixmap)
        self.pictureLabel.resize(pixmap.width(), pixmap.height())
        self.pictureLabel.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.desc, 0, 0)
        self.layout.addWidget(self.pictureLabel, 1, 0)
        self.layout.setContentsMargins(0, 0, 0, 75)

        self.setStyleSheet('QWidget {background-color: #f8f8ff;}')

    def show(self):
        super().show()

        # Add extra time for displaying the splash screen
        sleep(5)