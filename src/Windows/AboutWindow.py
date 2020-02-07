from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from Windows.WindowBase import WindowBase

class AboutWindow(WindowBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")

        self.makeLayout()
        self.setSizeAndCenter(3/8, 1/2)

    def makeLayout(self):
        self.descriptionLabel = QLabel('This program was made by Luke Karavolis<br> \
            For more information or to report any bugs, visit <a href="https://github.com/KaravolisL/AHEPA-Raffle">GitHub</a> \
                or email karavolisl@gmail.com')
        self.descriptionLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setTextFormat(Qt.RichText)
        self.descriptionLabel.setOpenExternalLinks(True)

        self.pictureLabel = QLabel()
        pixmap = QPixmap(r'images/Logo.jpg')
        self.pictureLabel.setPixmap(pixmap)
        self.pictureLabel.resize(pixmap.width(), pixmap.height())
        self.pictureLabel.setAlignment(Qt.AlignCenter)

        self.helpLabel = QLabel('For help, visit <a href="https://github.com/KaravolisL/AHEPA-Raffle/blob/master/README.md">README</a>')
        self.helpLabel.setTextFormat(Qt.RichText)
        self.helpLabel.setOpenExternalLinks(True)
        self.helpLabel.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.descriptionLabel, 0, 0)
        self.layout.addWidget(self.pictureLabel, 1, 0)
        self.layout.addWidget(self.helpLabel, 2, 0)
