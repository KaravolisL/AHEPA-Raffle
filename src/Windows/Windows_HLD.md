# Window Package


```plantuml

package WindowRepository {

class WindowBase
class AlertBase
class PrizeAlert
class RestartWarning
class ImportTicketsWindow
class ImportPrizesWindow
class EditTicketWindow
class EditPrizeWindow
class EditPrizeAlertWindow
class ChangeColorWindow

WindowBase <|-- AlertBase
WindowBase <|-- PrizeAlert
WindowBase <|-- EditTicketWindow
WindowBase <|-- EditPrizeWindow
WindowBase <|-- EditPrizeAlertWindow
WindowBase <|-- ChangeColorWindow
AlertBase <|-- RestartWarning

}

```