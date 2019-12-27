# Cells

```plantuml

hide empty members

package CellPackage {

class CellBase {
    + id
    + text
    + background_color
    + text_color
    + __init__(text, id): void
    + setText(text): void
    + setTextColor(color): void
    + setBackgroundColor(color): void
    + isTransparent(void): bool
    + setTransparent(bool): void
    + {abstract} mousePressEvent(QMouseEvent): void
}

class HeaderCellBase {
    + setText(text): void
    + isTransparent(void): bool
    + setTransparent(bool): void
}

class TableCell {
    + mousePressEvent(QMouseEvent): void
}

class TicketsRemainingCell {
    + __init__(void): void
    + mousePressEvent(QMouseEvent): void
}

class TicketsDrawnCell {
    + __init__(void): void
    + mousePressEvent(QMouseEvent): void
}

class LastTicketDrawnCell {
    + __init__(void): void
    + mousePressEvent(QMouseEvent): void
}

}

CellBase <|-- HeaderCellBase
CellBase <|-- TableCell

HeaderCellBase <|-- TicketsRemainingCell
HeaderCellBase <|-- TicketsDrawnCell
HeaderCellBase <|-- LastTicketDrawnCell

```