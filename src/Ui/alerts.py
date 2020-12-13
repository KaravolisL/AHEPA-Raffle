"""Module containing a collection of alert dialogs"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

from debug_logger import get_logger

logger = get_logger(__name__)

class Warning(QtWidgets.QDialog):
    """Warning popup"""
    def __init__(self, text):
        super().__init__()
        uic.loadUi('src/Ui/warning.ui', self)

        self.warning_text.setText(text)

        # Hide help button
        self.setWindowFlags(Qt.WindowCloseButtonHint)