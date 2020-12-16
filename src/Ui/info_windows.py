"""Module containing the about window"""

from PyQt5 import QtWidgets, uic

class About(QtWidgets.QMainWindow):
    """Window to display information about the application"""
    def __init__(self):
        super().__init__()
        uic.loadUi('src/Ui/about.ui', self)

        # Resize the picture
        self.picture_label.resize(self.picture_label.pixmap().width(),
                                  self.picture_label.pixmap().height())

        self.show()
