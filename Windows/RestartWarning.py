from Windows.AlertBase import AlertBase
import Controller

class RestartWarning(AlertBase):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Warning!!')


    def confirmationEvent(self):
        Controller.restartRaffle()
        self.close()

    def rejectEvent(self):
        self.close()

    def closeEvent(self, e):
        pass
