import random


class Player:
    def __init__(self, id, name, chips):
        self._id = id
        self.name = name
        self.chips = chips
        self.total_value = 0
        self.current_bet = 0
        self._cards = []
        self._actions = ["Check", "Raise", "Bet", "Call", "Fold"]

    def __str__(self):
        return f"Id: {self._id} Name: {self.name}"

    def take_action(self):
        self.total_value = self.get_total_value()
        if self.total_value == 0:
            return "Check", 0
        action = random.choice(self._actions)
        if action == "Check":
            return action, 0
        else:
            # de refacut si check pe chipsuri
            random_bet = random.randint(1, self.total_value)
            self.current_bet = random_bet
            return action, random_bet

    @property
    def id(self):
        return self._id

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = list(value)

    def get_total_value(self):
        total = 0
        for c in self.chips:
            total += c.value
        return total
