class Ticket:
    def __init__(self, name = None, number = 0):
        self.name = name
        self.number = number
        self.numberDrawn = 0

    def __str__(self):
        return str(self.number) + " " + self.name

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        assert(number < 226 and number > 0)
        self.number = number
    
    def setNumberDrawn(self, numberDrawn):
        assert(numberDrawn < 226 and numberDrawn >= 0)
        self.numberDrawn = numberDrawn

    def isDrawn(self):
        return self.numberDrawn != 0