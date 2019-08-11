# TODO: Add separator between Maximize and View Ticket Names

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        # Creating Menu
        self.fileMenu = self.addMenu("File")
        self.editMenu = self.addMenu("Edit")
        self.viewMenu = self.addMenu("View")
        self.helpMenu = self.addMenu("Help")

        # Actions for fileMenu
        self.fileRestartAction = QAction("Restart")
        self.fileMenu.addAction(self.fileRestartAction)

        self.fileImportTicketNamesAction = QAction("Import Ticket Names")
        self.fileMenu.addAction(self.fileImportTicketNamesAction)

        self.fileImportPrizesAction = QAction("Import Prizes")
        self.fileMenu.addAction(self.fileImportPrizesAction)

        # Action for editMenu
        self.editTicketAction = QAction("Edit Ticket")
        self.editMenu.addAction(self.editTicketAction)

        self.editPrizeAction = QAction("Edit Prize")
        self.editMenu.addAction(self.editPrizeAction)

        self.editChangeBackgroundAction = QAction("Change Background Color")
        self.editMenu.addAction(self.editChangeBackgroundAction)

        self.editPrizeAlertAction = QAction("Edit Prize Alert")
        self.editMenu.addAction(self.editPrizeAlertAction)

        # Actions for viewMenu
        self.viewFullScreenAction = QAction("Full Screen")
        self.viewMenu.addAction(self.viewFullScreenAction)

        self.viewMaximizedAction = QAction("Maximize")
        self.viewMaximizedAction.setShortcut('Esc')
        self.viewMenu.addAction(self.viewMaximizedAction)

        self.viewTicketNamesAction = QAction("Ticket Names")
        self.viewMenu.addAction(self.viewTicketNamesAction)

        self.viewPrizesAction = QAction("Prizes")
        self.viewMenu.addAction(self.viewPrizesAction)

        # Actions for helpMenu
        self.helpAboutAction = QAction("About")
        self.helpMenu.addAction(helpAboutAction)

    def setResponse(self, action, response):
        ''' Used by MainWindow to set the response for the actions on the MenuBar '''
        action.triggered.connect(response)

