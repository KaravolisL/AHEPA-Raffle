
from PyQt5.QtGui import QFont

from View.CellPkg.CellBase import CellBase
from Signals import Signals

# Logger import
from Logger.Logger import logger

class TableCell(CellBase):
    def __init__(self, text=None, id=0):
        super().__init__(text, id)
        self.sizePolicy().setRetainSizeWhenHidden(True)
        self.setText(self.text)
        self.setFont(QFont('Arial', 9))

    def setText(self, text):
        """
        Include the id when setting the text for a table cell
        """
        logger.debug('Setting text of cell #{} to {}'.format(self.id, text))
        self.text = text
        super().setText("{}\n{}".format(str(self.id), str(text)))

    def mousePressEvent(self, QMouseEvent):
        """
        If a table cell is clicked, emit the ticket drawn signal and make
        the cell transparent. Do nothing if it's already transparent
        """
        if not self.isTransparent():
            Signals().ticketDrawn.emit(self.id)
