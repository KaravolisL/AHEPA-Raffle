from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MenuBar import MenuBar
from FileManager import saveProgress

def debugPrint(s = "Hello"):
    print(s)

HEADER_MAINTABLE_SPACING = 3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setting up the menu bar
        self.setMenuBar(self.createMenuBar())

        # Creating the central widget for the window
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Setting the layout
        self.layout = QVBoxLayout()
        centralWidget.setLayout(self.layout)
        self.layout.setSpacing(HEADER_MAINTABLE_SPACING)
        centralWidget.layout().setContentsMargins(1,1,1,1)

        # Setting window icon
        self.setWindowIcon(QIcon('Icon.jpg'))

    def addWidget(self, widget):
        ''' Method to add a widget to the central widget's layout '''
        self.layout.addWidget(widget)

    def addLayout(self, layout):
        ''' Method to add a layout to the main window's layout '''
        self.layout.addLayout(layout)

    def createMenuBar(self):
        ''' Creates a MenuBar instance and sets the actions '''
        menuBar = MenuBar()
        menuBar.setResponse(menuBar.viewFullScreenAction, self.showFullScreen)
        menuBar.setResponse(menuBar.viewMaximizedAction, self.showMaximized)
        # TODO: Set remaining responses
        return menuBar

    def keyPressEvent(self, e):
        ''' Override keyPressEvent to handle Esc pressed '''
        if e.key() == Qt.Key_Escape:
            self.showMaximized()
        # TODO: Investigate blink upon full screen exit

    def showFullScreen(self):
        ''' Override showFullScreen method to hide menuBar '''
        super().showFullScreen()
        self.setMenuBar(None)

    def showMaximized(self):
        ''' Override showMaximized method to show menuBar '''
        super().showMaximized()
        self.setMenuBar(self.createMenuBar())

    def closeEvent(self, e):
        saveProgress()