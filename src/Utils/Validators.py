def validateTicketNumber(string):
    """
    Verifies that input is an int between 0 and 226
    :param str string: Input as type str
    :returns: Whether input is valid or not
    :rtype: bool
    """
    try:
        number = int(string)
        if (number > 0 and number < 226):
            return True
    except:
        pass
    return False

def validateTicketName(string):
    """

    """
    return True

def validatePrizeNumber(string):
    """
    Same validation as validateTicketNumber
    """
    return validateTicketNumber(string)

def validatePrizeName(string):
    """

    """
    return True

