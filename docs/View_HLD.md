# View

```plantuml

hide empty members

class MainWindow <<Singleton>>
class MainWidget
class MainTable
class Header
class MenuBar

MainWindow *-- MainWidget: > has
MainWindow *-- MenuBar: > has
MainWidget *-- Header: > has
MainWidget *-- MainTable: > has

```