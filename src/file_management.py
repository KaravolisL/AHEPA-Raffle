"""Module containing functions used to read from and write to files"""

import json

from debug_logger import get_logger
from raffle import Ticket, raffle, Prize
from constants import NUMBER_OF_TICKETS

logger = get_logger(__name__)

def format_checker(func):
    """Decorator function for catching formatting errors in files"""
    def func_wrapper(*args):
        try:
            return func(*args)
        except Exception as exception:
            logger.debug("Exception caught in %s", func.__name__)
            raise FormatException from exception
    return func_wrapper

@format_checker
def import_ticket_names(file: str):
    """Reads ticket names from a give file.

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

@format_checker
def import_prizes(file: str):
    """Reads prizes from a given file. Replaced existing prizes with
    the new ones

    :param str file: File from which to read
    """
    logger.debug("Importing prizes")

    # Read from file
    prizes = []
    with open(file, 'r') as prizes_file:
        for line in prizes_file:
            number, description = line.split(" ", 1)
            prize = Prize(int(number), description)
            prizes.append(prize)

    # Replace the current prizes with the new ones
    raffle.prizes = prizes

class CustomEncoder(json.JSONEncoder):
    """Custom json encoder to handle specific classes"""
    def default(self, obj):
        """Converts a python object to json"""
        if isinstance(obj, Ticket):
            return { "name" : obj.name,
                     "number" : obj.number,
                     "number_drawn": obj.number_drawn
            }
        return super().default(obj)

class SaveFileManager:
    """Class responsible for reading and writing the save file"""
    SAVE_FILE = r'save_file.json'

    def __init__(self):
        self.tickets_json = json.loads(json.dumps(raffle.tickets, cls=CustomEncoder))
        print(self.tickets_json['name'])

save_file_manager = SaveFileManager()

class FormatException(Exception):
    """Exception used for ill-formatted files"""
