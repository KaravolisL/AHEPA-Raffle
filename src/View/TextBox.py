from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

from Utils.Validators import validateTicketNumber
from Signals import Signals

# Logger import
from Logger.Logger import logger

class TextBox(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QLineEdit {color: transparent;}")
        self.setEchoMode(QLineEdit.NoEcho)

        self.setMaxLength(3)
        self.setReadOnly(True)

    def keyPressEvent(self, event):
        """
        Method to handle enter being pressed. Read-only is toggled to prevent
        the cursor from blinking. The ticketDrawn signal is emitted only if the
        entered number is valid
        :param QKeyEvent event: Key that was pressed
        """
        self.setReadOnly(False)
        if event.key() not in (Qt.Key_Return, Qt.Key_Enter):
            super().keyPressEvent(event)
        else:
            logger.debug('Key press detected on TextBox, text is {}'.format(self.text()))
            if validateTicketNumber(self.text()):
                Signals().ticketDrawn.emit(int(self.text()))
            self.clear()
        self.setReadOnly(True)
