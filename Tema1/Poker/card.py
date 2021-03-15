class Card:
    def __init__(self, number, suit):
        self._number = number
        self._suit = suit

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return f"Card is {self._number} {self._suit}"

    @property
    def number(self):
        return self._number

    @property
    def suit(self):
        return self._suit
