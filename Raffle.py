# PyQt libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

# System libraries
import sys
from datetime import datetime

# Local libraries
from Controller import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    # Initialize view and model
    Controller.initialize()

    app.exec_()