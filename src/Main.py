# PyQt libraries
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

# Local libraries
from View.SplashScreen import SplashScreen

# System libraries
import sys
from threading import Timer
from time import sleep
from datetime import datetime

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    splash_screen = SplashScreen()
    splash_screen.show()

    # Create a Raffle instance
    from Raffle import Raffle
    raffle = Raffle()

    # Setting the flag will kill the thread
    delayThread = Timer(2, lambda: splash_screen.close())
    delayThread.start()

    app.exec_()