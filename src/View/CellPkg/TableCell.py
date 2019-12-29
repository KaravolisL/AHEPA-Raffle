
from CellPkg.CellBase import CellBase
from Signals import Signals

class TableCell(CellBase):
    def __init__(self, text=None, id=0):
        super().__init__(text, id)
        self.sizePolicy().setRetainSizeWhenHidden(True)
        self.setText(self.text)

        Signals().ticketDrawn.connect(lambda: self.setTransparent(True))

    def setText(self, text):
        """
        Include the id when setting the text for a table cell
        """
        self.text = text
        super().setText("{}\n{}".format(str(self.id), str(text)))

    def mousePressEvent(self, QMouseEvent):
        """
        If a table cell is clicked, emit the ticket drawn signal and make
        the cell transparent. Do nothing if it's already transparent
        """
        if not self.isTransparent():
            Signals().ticketDrawn.emit(self.id)
