
from View import setPopup
from Windows.PopupBase import PopupBase

class WindowManager():
    def __init__(self):
        pass
    
    def makeWindow(self, windowType):
        window = WindowRepository.getInstance().getWindow(windowType)
        setPopup(window)



class WindowRepository():
    instance = None
    windowList = None

    def __init__(self):

        assert(self.instance == None) # Assert to ensure singleton

        self.instance = self

        self.windowList = {
            'restartWarning': PopupBase(),
        }

    @classmethod
    def getInstance(cls):
        return cls.instance if cls.instance != None else WindowRepository()

    def getWindow(self, windowType):
        window = self.windowList.get(windowType, None)
        assert(window != None)
        return window
