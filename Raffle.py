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
import View
import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    # Restore saved progress
    # readTickets("ticketNames.txt")

    # Construct MainWindow and its contents
    window = View.MainWindow()

    # Initialize view and model
    Controller.Controller.initialize()
    
    # Show the window maximized
    window.showMaximized()

    app.exec_()

    print("Raffle exited. Saving progress...")
    Controller.Controller.saveProgress()