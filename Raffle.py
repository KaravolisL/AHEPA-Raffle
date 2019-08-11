from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import sys

from MainWindow import MainWindow

from datetime import datetime











if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    window = MainWindow()

    app.exec_()