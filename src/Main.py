# PyQt libraries
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

# System libraries
import sys
from datetime import datetime

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    # Create a Raffle instance
    from Raffle import Raffle
    raffle = Raffle()

    app.exec_()