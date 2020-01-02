from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
from PyQt5.QtGui import QIcon

class WindowBase(QWidget):
    def __init__(self):
        super().__init__()

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Setting window icon
        self.setWindowIcon(QIcon(r'..\images\Icon.jpg'))

    def setSizeAndCenter(self, width_factor=(2/3), height_factor=(2/3)):
        """
        Sizes window using given factors and moves it to the center of the screen
        :param float width_factor: Number to multiply screenWidth by
        :param float height_factor: Number to mulitply screenHeight by 
        """
        # Set Size
        screen = QApplication.primaryScreen()
        size = screen.size()
        screenWidth = size.width()
        screenHeight = size.height()
        self.setGeometry(0, 0, screenWidth * width_factor, screenHeight * height_factor)

        # Center
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def makeLayout(self):
        raise NotImplementedError