from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from Windows.WindowBase import WindowBase

class WarningBase(WindowBase):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle('Warning!!')
        self.setWindowModality(Qt.ApplicationModal)
        self.text = text
        self.makeLayout()
        self.setSizeAndCenter(1/6, 1/7)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    def makeLayout(self):
        """
        Creates the two buttons and label using text defined by subclass
        """
        self.confirmButton = QPushButton('Confirm')
        self.confirmButton.clicked.connect(self.confirmationEvent)
        self.confirmButton.setDefault(True)

        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.cancelEvent)

        self.label = QLabel(self.text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 11))

        self.layout.addWidget(self.label, 0 , 0, 1, 2)
        self.layout.addWidget(self.confirmButton, 1, 0)
        self.layout.addWidget(self.cancelButton, 1, 1)

    def confirmationEvent(self):
        raise NotImplementedError

    def cancelEvent(self):
        """
        Nothing will be done if cancel button is hit
        """
        self.close()

    def keyPressEvent(self, event):
        """
        Connects the enter key to confirmationEvent
        :param QKeyEvent event: Key that is pressed
        """
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.confirmationEvent()
