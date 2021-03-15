import random


class Player:
    def __init__(self, id, name):
        self._id = id
        self.name = name
        self._cards = []
        self._actions = ["Check", "Raise", "Bet", "Call"]

    def __str__(self):
        return f"Id: {self._id} Name: {self.name}"

    def take_action(self):
        action = random.choice(self._actions)
        if action == "Check":
            return action, 0
        else:
            return action, 10

    @property
    def id(self):
        return self._id

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = list(value)
