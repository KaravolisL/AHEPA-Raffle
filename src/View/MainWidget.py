from PyQt5.QtGui import QWidget, QVBoxLayout

from MainTable import MainTable
from Header import Header

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create subwidgets and layout
        self.mainTable = MainTable()
        self.header = Header()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Add widgets to the layout
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.mainTable)

        # Set Layout to widget
        self.setLayout(self.layout)