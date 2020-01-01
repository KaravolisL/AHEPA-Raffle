from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from View.MenuBar import MenuBar
from View.MainWidget import MainWidget
from Utils.Singleton import Singleton
from Windows.WindowRepository import WindowType, WindowRepository
from Signals import Signals

@Singleton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup the menu bar
        self.menuBar = self.createMenuBar()
        self.setMenuBar(self.menuBar)

        # Creating the central widget for the window
        centralWidget = MainWidget()
        self.setCentralWidget(centralWidget)

        # Setting window icon
        self.setWindowIcon(QIcon(r'..\..\images\Icon.jpg'))

        # Variable to hold additional window instances
        self.popup = None

    def keyPressEvent(self, e):
        """
        Pressing escape will exit full screen
        :param QKeyEvent e: Event passed to this method
        """
        if e.key() == Qt.Key_Escape:
            self.showMaximized()

    def showFullScreen(self):
        """
        Override original method to also hide menu bar
        """
        super().showFullScreen()
        self.setMenuBar(None)

    def showMaximized(self):
        """
        Override original method to show menu bar
        """
        super().showMaximized()
        self.setMenuBar(self.createMenuBar())

    def closeEvent(self, event):
        """
        Occurs when the main window is closed.
        :param QEvent event: Event that caused the closing
        """
        print("Raffle exited. Saving progress...")
        Signals().raffleExited.emit()

    def createMenuBar(self):
        """
        Create a MenuBar instance and sets it's actions
        :returns: A prepared MenuBar instance
        :rtype: MenuBar
        """
        menuBar = MenuBar()
        menuBar.setResponse(menuBar.viewFullScreenAction, self.showFullScreen)
        menuBar.setResponse(menuBar.viewMaximizedAction, self.showMaximized)
        menuBar.setResponse(menuBar.fileRestartAction, lambda: self.setWindow(WindowType.RESTART_WARNING))
        menuBar.setResponse(menuBar.fileImportTicketNamesAction, lambda: self.setWindow(WindowType.IMPORT_TICKETS))
        menuBar.setResponse(menuBar.fileImportPrizesAction, lambda: self.setWindow(WindowType.IMPORT_PRIZES))
        menuBar.setResponse(menuBar.editTicketAction, lambda: self.setWindow(WindowType.EDIT_TICKET))
        menuBar.setResponse(menuBar.editPrizeAction, lambda: self.setWindow(WindowType.EDIT_PRIZE))
        menuBar.setResponse(menuBar.editChangeBackgroundAction, lambda: self.setWindow(WindowType.CHANGE_COLOR))
        menuBar.setResponse(menuBar.editPrizeAlertAction, lambda: self.setWindow(WindowType.EDIT_PRIZE_ALERT))
        menuBar.setResponse(menuBar.viewTicketNamesAction, lambda: self.setWindow(WindowType.VIEW_TICKETS))
        menuBar.setResponse(menuBar.viewPrizesAction, lambda: self.setWindow(WindowType.VIEW_PRIZES))
        menuBar.setResponse(menuBar.helpAboutAction, lambda: self.setWindow(WindowType.ABOUT))
        return menuBar

    def setWindow(self, windowType):
        """
        Method to set the MainWindow's popup attribute. This allows the additional
        windows to survive as long as the MainWindow.
        :param WindowType windowType: Type of window to display
        """
        self.popup = WindowRepository().getWindow(windowType)
        self.popup.show()

    