from PyQt5.QtGui import QLineEdit
from PyQt5.QtCore.Qt import Key_Enter, Key_Return

from Utils.Validators import validateTicketNumber
from Signals import Signals

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
        if event.key() in (Key_Return, Key_Enter):
            super().keyPressEvent(event)
        else:
            if validateTicketNumber(self.text()):
                Signals().ticketDrawn.emit(int(self.text()))
            self.clear()
        self.setReadOnly(True)
