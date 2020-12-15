"""Module containing functions used to read from and write to files"""

import json
import pathlib
from typing import List

from debug_logger import get_logger
from constants import NUMBER_OF_TICKETS
from data_classes import Prize, Ticket

logger = get_logger(__name__)

class FormatException(Exception):
    """Exception used for ill-formatted files"""

def format_checker(func):
    """Decorator function for catching formatting errors in files"""
    def func_wrapper(*args):
        try:
            return func(*args)
        except Exception as exception:
            logger.debug("Exception %s caught in %s", exception, func.__name__)
            raise FormatException from exception
    return func_wrapper

@format_checker
def import_ticket_names(file: str) -> List[str]:
    """Reads ticket names from a give file.

    :param str file: File from which to read
    """
    logger.debug("Importing ticket names")

    # Read from file
    names = []
    with open(file, 'r') as names_file:
        for _ in range(0, NUMBER_OF_TICKETS):
            names.append(names_file.readline().strip('\n'))
    return names

@format_checker
def import_prizes(file: str) -> List[Prize]:
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
    return prizes

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
        # Flag to signify save file was corrupted
        self.save_file_corrupted = False

        # Verify the save file
        try:
            self.verify_save()
        except FormatException:
            self.save_file_corrupted = True

    @format_checker
    def verify_save(self):
        """Verifies the save file exists and is formatted correctly"""
        # Throw an exception if the file doesn't exist or is formatted incorrectly
        try:
            json.load(open(self.SAVE_FILE, 'r'))
        except ValueError as value_error:
            self.create_default_save()
            raise FormatException from value_error

    def create_default_save(self):
        """Creates a default save file"""
        with open(self.SAVE_FILE, 'w') as save_file:
            json.dump(
                {"Tickets" : [Ticket("", i + 1) for i in range(0, NUMBER_OF_TICKETS)]},
                save_file,
                cls=CustomEncoder,
                indent=4
            )


save_file_manager = SaveFileManager()
