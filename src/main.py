"""Main file to be run"""

import sys
from datetime import datetime
from argparse import ArgumentParser

from PyQt5 import QtWidgets

EXIT_SUCCESS = 0

def main():
    """Main entry point of the application"""
    argument_parser = ArgumentParser(
        prog='python main.py'
    )
    argument_parser.add_argument('--no_gui', action='store_true',
                                 help='Launches application without the user interface')
    args = argument_parser.parse_args()

    if args.no_gui:
        return EXIT_SUCCESS

    # Initialize the user interface
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("AHEPA Raffle " + str(datetime.now().year))

    app.exec_()

    return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main())
