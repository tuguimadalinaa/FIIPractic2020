from Poker.generators import cardsGenerator, playersGenerator, chips_generator
from Poker.deck import Deck
import json


def players_flow(players_input, current_bet):
    for player in players_input:
        action, chips_value = player.take_action()
        if action == "Check":
            players_input.remove(player)
        elif action == "Raise":
            current_bet += chips_value
        elif action == "Call":
            pass


if __name__ == "__main__":
    configurations = json.load(open("Poker/game_config.json", "r"))
    cards = cardsGenerator.generate_cards()
    rounds = configurations["rounds"]
    chips_config = configurations["chips"]
    game_chips = list(chips_generator.generate_chips(chips_config))
    current_bet = configurations["entry_sum"]
    if configurations["type_of_game"] == "texas_holden":
        for round in range(rounds):
            deck = Deck(cards)
            deck.shuffle()
            players = list(playersGenerator.generate_players(configurations["number_of_players"]))
            for player in players:
                player.cards = deck.get_random_cards(2)
            players_flow(players, current_bet)
            deck.burn()
            flop = deck.get_random_cards(3)
            players_flow(players, current_bet)
            deck.burn()
            turn = deck.get_random_cards(1)
            players_flow(players, current_bet)
            deck.burn()
            river = deck.get_random_cards(1)
            players_flow(players, current_bet)
