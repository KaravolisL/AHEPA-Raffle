# Window Package

```plantuml

hide empty members

package WindowRepository {

class WindowBase
class WarningBase
class AlertBase
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
class CorruptedFileAlertWindow

WindowBase <|-- WarningBase
WindowBase <|-- AlertBase
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
AlertBase <|-- CorruptedFileAlertWindow

}

```