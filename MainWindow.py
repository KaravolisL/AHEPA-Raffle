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
        self.menuBar = MenuBar()
        self.setMenuBar(MenuBar())

        # Creating the central widget for the window
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Setting the layout
        self.layout = QHBoxLayout()
        centralWidget.setLayout(self.layout)

        # Setting window icon
        self.setWindowIcon(QIcon('Icon.jpg'))

        self.showMaximized()

    def add(self):
        ''' Method to add a widget to the central widget's layout '''
        pass

    def showFullScreen(self):
        ''' Override showFullScreen method to hide menuBar '''
        super().showFullScreen()
        self.setMenuBar(None)

    def showMaximized(self):
        ''' Override showMaximized method to show menuBar '''
        super().showMaximized()
        self.setMenuBar(self.menuBar)