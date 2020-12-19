"""Main file to be run"""

import sys
from datetime import datetime
from argparse import ArgumentParser

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from Ui.gui_manager import gui_manager
from raffle import raffle
import file_management
from debug_logger import get_logger

logger = get_logger(__name__)

EXIT_SUCCESS = 0

def main():
    """Main entry point of the application"""
    logger.info("Application launching")
    argument_parser = ArgumentParser(
        prog='python main.py'
    )
    argument_parser.add_argument('--no_gui', action='store_true',
                                 help='Launches application without the user interface')
    argument_parser.add_argument('--import_names', '-n', action='store_true',
                                 help='Auto imports the example names')
    argument_parser.add_argument('--import_prizes', '-p', action='store_true',
                                 help='Auto imports the example prizes')
    argument_parser.add_argument('--default_save', '-d', action='store_true',
                                 help='Overwrites existing save with a default one')
    args = argument_parser.parse_args()

    if args.default_save:
        file_management.save_file_manager.create_default_save()
        raffle.__init__()

    if args.import_names:
        new_names = file_management.import_ticket_names(r'examples/ticket_names.txt')
        for ticket, new_name in zip(raffle.tickets, new_names):
            ticket.name = new_name

    if args.import_prizes:
        new_prizes = file_management.import_prizes(r'examples/prizes.txt')
        raffle.prizes = new_prizes

    if args.no_gui:
        logger.info("Program exiting")
        return EXIT_SUCCESS

    # Initialize the user interface
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))
    app.setWindowIcon(QIcon(r'src/images/Icon.jpg'))
    gui_manager.initialize()

    app.exec_()

    logger.info("Program exiting")

    return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main())
