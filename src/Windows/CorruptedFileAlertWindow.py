

from Windows.AlertBase import AlertBase

class CorruptedFileAlertWindow(AlertBase):
    def __init__(self):
        super().__init__("The save file was corrupted.\nThe program has been reset")

    
