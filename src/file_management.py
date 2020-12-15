"""Module containing functions used to read from and write to files"""

import json
from typing import Any, Dict, List

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
    def default(self, o: Any):
        """Converts a python object to json"""
        if isinstance(o, Ticket):
            return {
                "name" : o.name,
                "number" : o.number,
                "number_drawn": o.number_drawn
            }
        if isinstance(o, Prize):
            return {
                "number" : o.number,
                "description" : o.description
            }
        return super().default(o)

def custom_decoder(dct: Dict) -> Any:
    """Custom json decoder to construct specific objects

    :param dict dct: Json dictionary

    :return: Decoded python object
    :rtype: Either custom object or dict
    """
    if "number_drawn" in dct:
        return Ticket(dct['number'], dct['name'], dct['number_drawn'])
    if "description" in dct:
        return Prize(dct['number'], dct['description'])
    return dct

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
        except (IOError, ValueError) as exception:
            self.create_default_save()
            raise FormatException from exception

    def create_default_save(self):
        """Creates a default save file"""
        with open(self.SAVE_FILE, 'w') as save_file:
            json.dump(
                {
                    "Tickets" : [Ticket(i + 1) for i in range(0, NUMBER_OF_TICKETS)],
                    "Prizes"  : []
                },
                save_file,
                cls=CustomEncoder,
                indent=4
            )

    def get_tickets(self) -> List[Ticket]:
        """Retrieves the list of tickets from the save file

        :return: Tickets contained in the save file
        :rtype: List[Ticket]
        """
        json_obj = json.load(open(self.SAVE_FILE, 'r'), object_hook=custom_decoder)
        return json_obj['Tickets']

    def get_prizes(self) -> List[Prize]:
        """Retrieves the list of prizes from the save file

        :return: Prizes contained in the save file
        :rtype: List[Prize]
        """
        json_obj = json.load(open(self.SAVE_FILE, 'r'), object_hook=custom_decoder)
        return json_obj['Prizes']

    def write_tickets_to_save_file(self, tickets: List[Ticket]) -> None:
        """Writes the list of tickets to the save file"""
        with open(self.SAVE_FILE, 'r+') as save_file:
            # Read in and delete existing tickets
            json_objects = json.load(save_file, object_hook=custom_decoder)
            del json_objects['Tickets']

            # Add new tickets list and write back
            json_objects['Tickets'] = tickets
            save_file.seek(0)
            json.dump(json_objects, save_file, cls=CustomEncoder, indent=4)

    def write_prizes_to_save_file(self, prizes: List[Prize]) -> None:
        """Writes the list of prizes to the save file"""
        with open(self.SAVE_FILE, 'r+') as save_file:
            # Read in and delete existing prizes
            json_objects = json.load(save_file, object_hook=custom_decoder)
            del json_objects['Prizes']

            # Add new prizes list and write back
            json_objects['Prizes'] = prizes
            save_file.seek(0)
            json.dump(json_objects, save_file, cls=CustomEncoder, indent=4)



save_file_manager = SaveFileManager()
