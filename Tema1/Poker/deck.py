import random


class Deck:
    def __init__(self, cards):
        self._cards = list(cards)

    def shuffle(self):
        return random.shuffle(self._cards)

    def burn(self):
        self._cards.remove(random.choice(self._cards))

    def get_random_cards(self, number_of_cards_to_get):
        to_return = random.sample(self._cards, number_of_cards_to_get)
        for card in to_return:
            self._cards.remove(card)
        return to_return

    @property
    def cards(self):
        return self._cards
