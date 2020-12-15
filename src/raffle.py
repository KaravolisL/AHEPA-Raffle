"""Module for the backend of the application"""

from typing import List

from data_classes import Prize, Ticket, Signals
import file_management
from debug_logger import get_logger
logger = get_logger(__name__)

class Raffle:
    """Class to represent the raffle"""
    def __init__(self):
        self._prizes: List[Prize] = []
        self._tickets: List[Ticket] = []
        self.signals = Signals()

        # Initialize ticket list
        self.tickets = file_management.save_file_manager.get_tickets()

        # Determine how many tickets have been drawn
        self.num_tickets_drawn = 0
        for ticket in self.tickets:
            if ticket.number_drawn > self.num_tickets_drawn:
                self.num_tickets_drawn = ticket.number_drawn

        # Initialize prize list
        self.prizes = file_management.save_file_manager.get_prizes()

    @property
    def prizes(self):
        """Returns the list of prizes"""
        return self._prizes

    @prizes.setter
    def prizes(self, val: List[Prize]):
        self._prizes = val
        self.signals.data_changed.emit()

    @property
    def tickets(self):
        """Returns the list of tickets"""
        return self._tickets

    @tickets.setter
    def tickets(self, val: List[Ticket]):
        self._tickets = val
        self.signals.data_changed.emit()

    def get_prize_from_number(self, prize_number: int) -> Prize:
        """Obtains a prize given the number

        :param int prize_number: Number of the prize to get
        """
        for prize in self.prizes:
            if prize.number == prize_number:
                return prize
        return None

    def draw_ticket(self, ticket_number) -> None:
        """Sets the given ticket's number_drawn field and increments num_tickets_drawn
        :param int ticket_number: Number of ticket to remove
        """
        assert not self.tickets[ticket_number - 1].is_drawn(), 'Ticket already removed'
        logger.debug('Removing ticket number %d', ticket_number)
        self.num_tickets_drawn += 1
        self.tickets[ticket_number - 1].number_drawn = self.num_tickets_drawn

        # Check if there is a prize next
        next_prize = self.get_prize_from_number(self.num_tickets_drawn + 1)
        if next_prize is not None:
            self.signals.prize_next.emit(next_prize)

        # Write to the save file
        file_management.save_file_manager.write_tickets_to_save_file(self.tickets)

    def replace_ticket(self) -> None:
        """Replaces the last drawn ticket"""
        last_ticket_drawn = self.get_last_ticket_drawn()
        assert last_ticket_drawn is not None, 'No tickets have been drawn'
        assert last_ticket_drawn.is_drawn(), 'Ticket has not been drawn'
        logger.debug('Replacing ticket number %d', last_ticket_drawn.number)
        self.num_tickets_drawn -= 1
        self.tickets[last_ticket_drawn.number - 1].number_drawn = 0

        # Write to the save file
        file_management.save_file_manager.write_tickets_to_save_file(self.tickets)

    def restart(self):
        """This method replaces all drawn tickets"""
        while self.num_tickets_drawn != 0:
            self.replace_ticket()

    def get_last_ticket_drawn(self) -> Ticket:
        """Iterates the list and compares each ticket's number_drawn field
        :returns: Returns the last ticket drawn, None if no tickets have been drawn
        :rtype: Ticket
        """
        if self.num_tickets_drawn != 0:
            for ticket in self.tickets:
                if ticket.number_drawn == self.num_tickets_drawn:
                    return ticket
            assert False, "Corresponding ticket not found"
        return None

raffle = Raffle()
