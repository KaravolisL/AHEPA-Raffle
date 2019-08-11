class Ticket:
    def __init__(self, name = None, number = 0):
        self.name = name
        self.number = number
        self.numberDrawn = 0

    def __str__(self):
        return self.name