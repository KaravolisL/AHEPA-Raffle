from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MenuBar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setting up the menu bar
        self.setMenuBar(MenuBar())

        # Creating the central widget for the window
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Setting the layout
        self.layout = QHBoxLayout()
        centralWidget.setLayout(self.layout)


        self.show()