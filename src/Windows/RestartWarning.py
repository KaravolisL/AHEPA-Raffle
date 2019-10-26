from Windows.AlertBase import AlertBase
import Controller

class RestartWarning(AlertBase):
    def __init__(self):
        self.text = 'Restarting the raffle will cause \nall progress to be lost!'
        super().__init__(self.text)

    def confirmationEvent(self):
        """
        Calls controller's restartRaffle function and closes window
        """
        Controller.restartRaffle()
        self.close()

    def closeEvent(self, e):
        pass
