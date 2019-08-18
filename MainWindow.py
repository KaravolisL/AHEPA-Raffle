from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MenuBar import MenuBar

def debugPrint(s = "Hello"):
    print(s)

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

        # Setting window icon
        self.setWindowIcon(QIcon('Icon.jpg'))

        # Show the window maximized
        self.showMaximized()

    def addWidget(self, widget):
        ''' Method to add a widget to the central widget's layout '''
        self.layout.addWidget(widget)

    def addLayout(self, layout):
        '''    '''
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

    def showFullScreen(self):
        ''' Override showFullScreen method to hide menuBar '''
        super().showFullScreen()
        self.setMenuBar(None)

    def showMaximized(self):
        ''' Override showMaximized method to show menuBar '''
        super().showMaximized()
        self.setMenuBar(self.createMenuBar())