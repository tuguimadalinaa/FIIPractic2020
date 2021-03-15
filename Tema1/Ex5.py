from Poker.generators import cardsGenerator, playersGenerator
from Poker.deck import Deck
import json


def players_flow(players_input):
    for player in players_input:
        action, chips = player.take_action()
        if action == "Check":
            players_input.remove(player)
        elif action == "Bet":
            pass
        elif action == "Raise":
            pass
        elif action == "Call":
            pass


if __name__ == "__main__":
    configurations = json.load(open("Poker/game_config.json", "r"))
    cards = cardsGenerator.generate_cards()
    rounds = configurations["rounds"]

    if configurations["type_of_game"] == "texas_holden":
        for round in range(rounds):
            deck = Deck(cards)
            deck.shuffle()
            players = list(playersGenerator.generate_players(configurations["number_of_players"]))
            for player in players:
                player.cards = deck.get_random_cards(2)
            players_flow(players)
            # oamenii se uita la carti si se gandesc daca platesc ca sa intre in joc in functie de ce carti au
            # daca da cineva raise, restul lumii tre sa egaleze suma aia de ban
            deck.burn()
            flop = deck.get_random_cards(3)
            players_flow(players)
            # oamenii se uita la carti si se gandesc daca platesc ca sa intre in joc in functie de ce carti au
            # daca da cineva raise, restul lumii tre sa egaleze suma aia de ban
            deck.burn()
            turn = deck.get_random_cards(1)
            players_flow(players)
            # oamenii se uita la carti si se gandesc daca platesc ca sa intre in joc in functie de ce carti au
            # daca da cineva raise, restul lumii tre sa egaleze suma aia de ban
            deck.burn()
            river = deck.get_random_cards(1)
            players_flow(players)
            # oamenii se uita la carti si se gandesc daca platesc ca sa intre in joc in functie de ce carti au
            # daca da cineva raise, restul lumii tre sa egaleze suma aia de ban
