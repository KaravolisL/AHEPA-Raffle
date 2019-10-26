
from Windows.AlertBase import AlertBase

class ImportWarningWindow(AlertBase):
    def __init__(self):
        self.text = 'Fill in later'
        super().__init__(self.text)