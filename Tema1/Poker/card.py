class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return f"Card is {self.number} {self.suit}"

    def __lt__(self, other):
        faces = {"Queen": 11, "Jack": 12, "King": 13}
        first_item = other._number
        second_item = self.number
        if isinstance(first_item, str):
            first_item = faces[other._number]
        if isinstance(self.number, str):
            second_item = faces[self.number]
        return second_item < first_item
