"""Tests for the Raffle class"""

import sys
sys.path.insert(1, 'src')

from raffle import Raffle
from constants import NUMBER_OF_TICKETS

def test_restart():
    test_raffle = Raffle()
    assert test_raffle.get_last_ticket_drawn() is None

    for i in range(0, NUMBER_OF_TICKETS):
        test_raffle.draw_ticket(i + 1)

    assert test_raffle.get_last_ticket_drawn() is not None

    test_raffle.restart()

    assert test_raffle.get_last_ticket_drawn() is None
    for ticket in test_raffle.tickets:
        assert ticket.number_drawn == 0