"""Module containing functions used to read from and write to files"""

from raffle import raffle
from constants import NUMBER_OF_TICKETS
from logger import get_logger

logger = get_logger(__name__)

def import_ticket_names(file: str):
    """Reads ticket names from a give file. Overwrites the current ticket names in
    data.xml and returns a list of the names

    :param str file: File from which to read
    """
    logger.debug("Importing ticket names")

    # Read from file
    names = []
    with open(file, 'r') as names_file:
        for _ in range(0, NUMBER_OF_TICKETS):
            names.append(names_file.readline().strip('\n'))
    
    # Set the ticket names
    for new_name, ticket in zip(names, raffle.tickets):
        ticket.name = new_name

class FormatException(Exception):
    """Exception used for ill-formatted files"""
