import random


class Player:
    def __init__(self, id, name, chips):
        self._id = id
        self.name = name
        self.chips = chips
        self.total_value = 0
        self.current_hand = None
        self._cards = []
        self._won_value = 0
        self._actions = ["Fold", "Raise", "Call"]

    def __str__(self):
        return f"Id: {self._id} Name: {self.name}"

    def take_action(self, can_bet, current_bet):
        self.total_value = self.get_total_value()
        if self.total_value == 0:
            return "Fold", 0
        if can_bet:
            action = random.choice(["Bet", "Check"])
            if action == "Bet":
                return action, self.bet()
            else:
                if action == "Check":
                    return action, 0
        action = random.choice(self._actions)
        if action == "Fold":
            return action, 0
        elif action == "Call":
            return action, current_bet
        elif action == "Raise":
            # de refacut si check pe chipsuri
            random_bet = self.total_value
            tries = 10
            while random_bet < current_bet:
                if tries == 0:
                    return "Fold", 0
                random_bet = random.randint(1, self.total_value)
                tries -= 1
            return action, random_bet

    def bet(self):
        self.get_total_value()
        bet = random.randint(1, self.total_value)
        return bet

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
        self.total_value = total
        return total
