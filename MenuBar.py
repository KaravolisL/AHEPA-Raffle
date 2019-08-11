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
        fileMenu = self.addMenu("File")
        editMenu = self.addMenu("Edit")
        viewMenu = self.addMenu("View")
        helpMenu = self.addMenu("Help")

        # Creating fileMenu items
        fileMenu.addAction("Restart")
        fileMenu.addAction("Import Ticket Names")
        fileMenu.addAction("Import Prizes")

        # Creating editMenu items
        editMenu.addAction("Edit Ticket")
        editMenu.addAction("Edit Prize")
        editMenu.addAction("Change Background Color")
        editMenu.addAction("Edit Prize Alert")

        # Creating viewMenu items
        viewMenu.addAction("Full Screen")
        viewMenu.addAction("Maximize")
        viewMenu.addAction("Ticket Names")
        viewMenu.addAction("Prizes")

        # Creating helpMenu items
        helpMenu.addAction("About")

