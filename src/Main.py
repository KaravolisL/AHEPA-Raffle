# PyQt libraries
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

# System libraries
import sys
from datetime import datetime

# Local libraries
import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))
    app.setWindowIcon(QIcon(r'..\images\Icon.jpg'))
    
    # Initialize view and model
    Controller.initialize()

    app.exec_()