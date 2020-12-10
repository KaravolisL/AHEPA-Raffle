"""Module containing custom widgets"""

from PyQt5 import QtWidgets, QtCore

class ClickableLabel(QtWidgets.QLabel):
    """A label with a clicked signal"""
    clicked = QtCore.pyqtSignal()
    
    def __init__(self, parent = None):
        super().__init__()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)