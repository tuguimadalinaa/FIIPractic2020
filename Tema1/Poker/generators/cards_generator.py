from Poker.card import Card

suits = {1: "Spades", 2: "Hearts", 3: "Diamonds", 4: "Clubs"}


def generate_cards():
    for s in suits.keys():
        for value in range(1, 14):
            yield Card(value, suits[s])