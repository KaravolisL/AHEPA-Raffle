from Windows.RestartWarning import RestartWarning
from Windows.ImportTicketsWindow import ImportTicketsWindow
from Windows.ImportPrizesWindow import ImportPrizesWindow
from Windows.PrizeAlert import PrizeAlert
from Windows.EditTicketWindow import EditTicketWindow
from Windows.EditPrizeWindow import EditPrizeWindow
from Windows.ChangeColorWindow import ChangeColorWindow
from Windows.EditPrizeAlertWindow import EditPrizeAlertWindow
from Windows.ViewTicketsWindow import ViewTicketsWindow
from Windows.ViewPrizesWindow import ViewPrizesWindow

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
            'prizeAlertWindow': PrizeAlert(),
            'editTicketWindow': EditTicketWindow(),
            'editPrizeWindow': EditPrizeWindow(),
            'changeColorWindow': ChangeColorWindow(),
            'editPrizeAlertWindow': EditPrizeAlertWindow(),
            'viewTicketsWindow': ViewTicketsWindow(),
            'viewPrizesWindow': ViewPrizesWindow(),
        }

    @classmethod
    def getInstance(cls):
        return cls.instance if cls.instance != None else WindowRepository()

    def getWindow(self, windowType):
        window = self.windowList.get(windowType, None)
        assert(window != None), 'Window type not supported'
        return window