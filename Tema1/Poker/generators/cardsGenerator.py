from Poker.card import Card

faces = {11: "Queen", 12: "Jack", 13: "King"}
suits = {1: "Spades", 2: "Hearts", 3: "Diamonds", 4: "Clubs"}


def generate_cards():
    for s in suits.keys():
        for value in range(1, 14):
            yield Card(value, suits[s])
            # if value > 10:
            #     yield Card(faces[value], suits[s])
            # else:
            #     yield Card(value, suits[s])