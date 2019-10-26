class Validator:
    def __init__(self):
        pass

    def validate(self, string):
        """ Verifies that input is an int between 0 and 226 """
        try:
            number = int(string)
            if (number > 0 and number < 226):
                return True
        except:
            pass
        return False
        