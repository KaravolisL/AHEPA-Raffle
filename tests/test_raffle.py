"""Tests for the Raffle class"""

import sys
sys.path.insert(1, 'src')

from raffle import Raffle
from constants import NUMBER_OF_TICKETS
import file_management

def test_draw_ticket():
    """Unit test for draw ticket method"""
    file_management.save_file_manager.create_default_save()
    test_raffle = Raffle()

    for i in range(0, NUMBER_OF_TICKETS):
        test_raffle.draw_ticket(i + 1)

        assert test_raffle.num_tickets_drawn == i + 1
        assert test_raffle.tickets[i].number_drawn == i + 1
        assert test_raffle.tickets[i].is_drawn()
        assert test_raffle.tickets[i] == test_raffle.get_last_ticket_drawn()

def test_restart():
    """Unit test for the restart method"""
    file_management.save_file_manager.create_default_save()
    test_raffle = Raffle()
    assert test_raffle.get_last_ticket_drawn() is None

    for i in range(0, NUMBER_OF_TICKETS):
        test_raffle.draw_ticket(i + 1)

    assert test_raffle.get_last_ticket_drawn() is not None

    test_raffle.restart()

    assert test_raffle.get_last_ticket_drawn() is None
    for ticket in test_raffle.tickets:
        assert ticket.number_drawn == 0

def test_replace_ticket():
    """Unit test for the replace ticket method"""
    file_management.save_file_manager.create_default_save()
    test_raffle = Raffle()

    for i in range(0, NUMBER_OF_TICKETS):
        test_raffle.draw_ticket(i + 1)
        assert test_raffle.num_tickets_drawn == 1

        test_raffle.replace_ticket()
        assert test_raffle.num_tickets_drawn == 0

        for ticket in test_raffle.tickets:
            assert not ticket.is_drawn()
