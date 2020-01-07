# Window Package

```plantuml

hide empty members

package WindowRepository {

class WindowBase
class WarningBase
class PrizeAlert
class RestartWarning
class ImportTicketsWindow
class ImportPrizesWindow
class EditTicketWindow
class EditPrizeWindow
class EditPrizeAlertWindow
class ChangeColorWindow
class ViewWindow
class ViewTicketsWindow
class ViewPrizesWindow

class ImportWarningWindow

WindowBase <|-- WarningBase
WindowBase <|-- PrizeAlert
WindowBase <|-- EditTicketWindow
WindowBase <|-- EditPrizeWindow
WindowBase <|-- EditPrizeAlertWindow
WindowBase <|-- ChangeColorWindow
WindowBase <|-- ViewWindow
ViewWindow <|-- ViewTicketsWindow
ViewWindow <|-- ViewPrizesWindow
WarningBase <|-- RestartWarning
WarningBase <|-- ImportWarningWindow

}

```