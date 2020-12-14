"""Main file to be run"""

import sys
from datetime import datetime
from argparse import ArgumentParser

from PyQt5 import QtWidgets

from Ui.gui_manager import gui_manager
import file_management

EXIT_SUCCESS = 0

def main():
    """Main entry point of the application"""
    argument_parser = ArgumentParser(
        prog='python main.py'
    )
    argument_parser.add_argument('--no_gui', action='store_true',
                                 help='Launches application without the user interface')
    argument_parser.add_argument('--import_names', '-n', action='store_true',
                                 help='Auto imports the example names')
    argument_parser.add_argument('--import_prizes', '-p', action='store_true',
                                 help='Auto imports the example prizes')
    args = argument_parser.parse_args()

    if args.import_names:
        file_management.import_ticket_names(r'examples/ticket_names.txt')

    if args.import_prizes:
        file_management.import_prizes(r'examples/prizes.txt')

    if args.no_gui:
        return EXIT_SUCCESS

    # Initialize the user interface
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    gui_manager.initialize()

    app.exec_()

    return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main())
