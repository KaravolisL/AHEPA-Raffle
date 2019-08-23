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
from MainWindow import MainWindow
from Header import Header
from MainTable import MainTable
from FileManager import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    # Restore saved progress
    readTickets("ticketNames.txt")

    # Construct MainWindow and its contents
    window = MainWindow()
    window.addLayout(Header.getInstance())
    window.addLayout(MainTable())

    # Show the window maximized
    window.showMaximized()

    app.exec_()