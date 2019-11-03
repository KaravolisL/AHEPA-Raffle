from Windows.RestartWarning import RestartWarning
from Windows.ImportTicketsWindow import ImportTicketsWindow
from Windows.ImportPrizesWindow import ImportPrizesWindow

class WindowRepository():
    instance = None
    windowList = None

    def __init__(self):

        assert(WindowRepository.instance == None) # Assert to ensure singleton

        WindowRepository.instance = self

        self.windowList = {
            'restartWarning': RestartWarning(),
            'importTicketsWindow': ImportTicketsWindow(),
            'importPrizesWindow': ImportPrizesWindow(),
            'prizeAlertWindow': RestartWarning(), # TODO: Change this
        }

    @classmethod
    def getInstance(cls):
        return cls.instance if cls.instance != None else WindowRepository()

    def getWindow(self, windowType):
        window = self.windowList.get(windowType, None)
        assert(window != None), 'Window type not supported'
        return window