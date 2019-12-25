from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from Windows.WindowBase import WindowBase

class ViewWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def reevaluate(self):
        raise NotImplementedError

    def make_item(self, text):
        """
        Helper method used by subclasses to create their table cells
        :param str text: Text for the cell
        :returns: A prepared item ready to be added to a table
        :rtype: QTableWidgetItem
        """
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(Qt.AlignCenter)
        item.setFlags(Qt.ItemIsEnabled)
        return item
