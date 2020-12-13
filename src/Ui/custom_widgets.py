"""Module containing custom widgets"""

from PyQt5 import QtWidgets, QtCore

class ClickableLabel(QtWidgets.QLabel):
    """A label with a clicked signal"""
    clicked = QtCore.pyqtSignal()

    # pylint: disable=invalid-name
    def mousePressEvent(self, event):
        """Handles the mouse press event"""
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)
    # pylint: enable=invalid-name
