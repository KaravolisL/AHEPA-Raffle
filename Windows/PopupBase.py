from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

<<<<<<< HEAD
=======





>>>>>>> d4a4fce54bcdaa62a7af68e2dac182c83b8d5e1f
class PopupBase(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')
        self.setGeometry(100,100,100,100)

        # Create and set layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel('TestTestTest'), 0 ,0)
        self.layout.setColumnStretch(0, 2)
        self.layout.addWidget(QPushButton('Confirm'), 1, 0)
        self.layout.addWidget(QPushButton('Cancel'), 1, 1)

        self.center()
        self.show()


    def center(self):
        """
        Used to center window in middle of screen
        """
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())