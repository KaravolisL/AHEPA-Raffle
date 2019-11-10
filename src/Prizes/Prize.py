class Prize:
    def __init__(self, number, description = None):
        self.number = number
        self.description = description

    def __str__(self):
        return str(self.number) + " " + self.description