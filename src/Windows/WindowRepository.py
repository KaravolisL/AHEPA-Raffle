# System libraries
from enum import Enum, auto

# Local libraries
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
from Utils.Singleton import Singleton

@Singleton
class WindowRepository():
    windowList = None

    def __init__(self):

        self.windowList = {
            WindowType.RESTART_WARNING: RestartWarning(),
            WindowType.IMPORT_TICKETS: ImportTicketsWindow(),
            WindowType.IMPORT_PRIZES: ImportPrizesWindow(),
            WindowType.PRIZE_ALERT: PrizeAlert(),
            WindowType.EDIT_TICKET: EditTicketWindow(),
            WindowType.EDIT_PRIZE: EditPrizeWindow(),
            WindowType.CHANGE_COLOR: ChangeColorWindow(),
            WindowType.EDIT_PRIZE_ALERT: EditPrizeAlertWindow(),
            WindowType.VIEW_TICKETS: ViewTicketsWindow(),
            WindowType.VIEW_PRIZES: ViewPrizesWindow(),
        }

    def getWindow(self, windowType):
        window = self.windowList.get(windowType, None)
        assert(window != None), 'Window type not supported'
        return window

class WindowType(Enum):
    RESTART_WARNING = auto()
    IMPORT_TICKETS = auto()
    IMPORT_PRIZES = auto()
    PRIZE_ALERT = auto()
    EDIT_TICKET = auto()
    EDIT_PRIZE = auto()
    CHANGE_COLOR = auto()
    EDIT_PRIZE_ALERT = auto()
    VIEW_TICKETS = auto()
    VIEW_PRIZES = auto()
    ABOUT = auto()
