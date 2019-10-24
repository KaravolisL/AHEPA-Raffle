from Windows.RestartWarning import RestartWarning

class WindowRepository():
    instance = None
    windowList = None

    def __init__(self):

        assert(self.instance == None) # Assert to ensure singleton

        self.instance = self

        self.windowList = {
            'restartWarning': RestartWarning(),
        }

    @classmethod
    def getInstance(cls):
        return cls.instance if cls.instance != None else WindowRepository()

    def getWindow(self, windowType):
        window = self.windowList.get(windowType, None)
        assert(window != None)
        return window