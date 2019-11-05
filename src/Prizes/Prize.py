class Prize:
    def __init__(self, number, statement = None):
        self.number = number
        self.statement = statement

    def __str__(self):
        return str(self.number) + " " + self.statement