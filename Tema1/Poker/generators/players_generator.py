from Poker.player import Player
import uuid
import string
import random
from Poker.chips import Chips

letters = string.ascii_lowercase


def get_chips_of_specific_value(chips_stack, value):
    for i in chips_stack:
        if i.value == value:
            chips_stack.remove(i)
            return i


def generate_players(number_of_players, chips):
    for player in range(number_of_players):
        id = uuid.uuid4()
        name = ''.join(random.choice(letters) for i in range(20))
        chips_stack_to_give = [get_chips_of_specific_value(chips, 1), get_chips_of_specific_value(chips, 1),
                               get_chips_of_specific_value(chips, 5), get_chips_of_specific_value(chips, 5)]
        yield Player(id, name, chips_stack_to_give)
