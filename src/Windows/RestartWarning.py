from Windows.WarningBase import WarningBase
from Signals import Signals

class RestartWarning(WarningBase):
    def __init__(self):
        self.text = 'Restarting the raffle will cause \nall progress to be lost!'
        super().__init__(self.text)

    def confirmationEvent(self):
        """
        Emit the restartRaffle signal and close window
        """
        Signals().restartRaffle.emit()
        self.close()

    def closeEvent(self, e):
        pass
