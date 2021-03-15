from Poker.player import Player
import uuid
import string
import random

letters = string.ascii_lowercase


def generate_players(number_of_players):
    for player in range(number_of_players):
        id = uuid.uuid4()
        name = ''.join(random.choice(letters) for i in range(20))
        yield Player(id, name)
