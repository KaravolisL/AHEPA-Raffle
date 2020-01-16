# TODO: Do I really need to store the text? I might be able to just
# reimplement getText

from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt

class CellBase(QLabel):
    def __init__(self, text = None, id = 0):
        super().__init__()
        self.text = text
        self.id = id
        self.backgroundColor = 'white'
        self.textColor = 'black'

        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setMinimumSize(self.sizeHint())
    
    def setText(self, text):
        """
        Sets the label's text using the parent's method. Stores it in a class attribute
        :param str text: New text for label
        """
        self.text = text
        super().setText(text)

    def setBackgroundColor(self, color):
        """
        Overwrites class attribute and resets style sheet using it
        :param str color: New background color
        """
        # TODO: Validate color
        self.backgroundColor = str(color)
        self.setStyleSheet("QLabel {background-color: " + str(color) + ";color: " + self.textColor + ";}")

    def setTextColor(self, color):
        """
        Overwrites class attribute and resets style sheet using it
        :param str color: New text color
        """
        self.textColor = str(color)
        self.setStyleSheet("QLabel {background-color: " + self.backgroundColor + ";color: " + str(color) + ";}")

    def isTransparent(self):
        """
        :returns: Whether the cell is transparent or not
        :rtype: bool
        """
        return 'transparent' in self.styleSheet()

    def setTransparent(self, bool):
        """
        
        """
        if bool:
            # The class attributes will not be overwritten in this case
            self.setStyleSheet("QLabel {background-color: transparent; color: transparent;}")
        else:
            self.setBackgroundColor(self.backgroundColor)
            self.setTextColor(self.textColor)

    def mousePressEvent(self, QMouseEvent): raise NotImplementedError