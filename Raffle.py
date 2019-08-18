from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import sys
from datetime import datetime

from MainWindow import MainWindow
from Header import Header
from MainTable import MainTable




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    # Construct MainWindow and its contents
    window = MainWindow()
    window.addLayout(Header())
    window.addLayout(MainTable())

    app.exec_()