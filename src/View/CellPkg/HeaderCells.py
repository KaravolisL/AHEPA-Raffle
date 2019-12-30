from View.CellPkg.CellBase import CellBase
from Signals import Signals
from Windows.WindowRepository import WindowType
import View.MainWindow as MainWindow

class HeaderCellBase(CellBase):
    def __init__(self, base_text):
        super().__init__()
        self.base_text = base_text

    def setText(self, text):
        """
        Setting the text of header cells involves just updating the 
        trailing number.
        :param str text: Number to be added to the end of the string
        """
        super().setText('{} {}'.format(self.base_text, str(text)))

    def isTransparent(self):
        """
        Header cells should never be transparent
        """
        raise TypeError

    def setTransparent(self, bool):
        """
        Header cells should never be transparent
        """
        raise TypeError

class TicketsRemainingCell(HeaderCellBase):
    def __init__(self):
        base_text = 'Tickets Remaining:'
        super().__init__(base_text)
        self.setText('225')

    def mousePressEvent(self, QMouseEvent):
        """
        The TicketsRemainingCell is reserved for the line edit
        """
        pass

class TicketsDrawnCell(HeaderCellBase):
    def __init__(self):
        base_text = 'Tickets Drawn:'
        super().__init__(base_text)
        self.setText('0')

    def mousePressEvent(self, QMouseEvent):
        """
        Clicking the TicketsDrawnCell will cause the ViewTicketsWindow
        to be shown
        """
        MainWindow.MainWindow().setWindow(WindowType.VIEW_TICKETS)

class LastTicketDrawnCell(HeaderCellBase):
    def __init__(self):
        base_text = 'Last Ticket Drawn:'
        super().__init__(base_text)
        self.setText('')

    def mousePressEvent(self, QMouseEvent):
        """
        Pressing the LastTicketDrawnCell replaces the last drawn ticket
        """
        Signals().undoButtonClicked.emit()
