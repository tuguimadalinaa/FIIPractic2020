from Poker.generators import cards_generator, players_generator, chips_generator
from Poker.deck import Deck
from Poker.poker_engine import PokerEngine
import json


def players_flow(players, poker_engine):
    for player in players:
        action, chips_value = player.take_action(poker_engine.can_bet, poker_engine.current_bet)
        if action == "Fold":
            poker_engine.players.remove(player)
        elif action == "Bet":
            poker_engine.updateBet(chips_value)
            poker_engine.can_bet = False
        elif action == "Raise":
            poker_engine.updateBet(poker_engine.current_bet + chips_value)
        else:
            poker_engine.updateBet(chips_value)
        poker_engine.updateDeckBet(poker_engine.deck_bet + chips_value)


if __name__ == "__main__":
    configurations = json.load(open("Poker/game_config.json", "r"))
    cards = cards_generator.generate_cards()
    rounds = configurations["rounds"]
    chips_config = configurations["chips"]
    game_chips = list(chips_generator.generate_chips(chips_config))

    if configurations["type_of_game"] == "texas_holdem":
        for round in range(rounds):
            poker_engine = PokerEngine()
            deck = Deck(cards)
            deck.shuffle()
            players = list(players_generator.generate_players(configurations["number_of_players"], game_chips))
            poker_engine.updatePlayers(players)
            sb = players[0].bet()
            poker_engine.updateBet(sb)
            bb = players[1].bet()
            poker_engine.updateBet(bb)
            poker_engine.updateDeckBet(sb + bb)
            poker_engine.can_bet = False
            for player in players:
                player.cards = deck.get_random_cards(2)
            if len(poker_engine.players) < 2:
                print("Winner is: ", poker_engine.players[0])
                continue
            players_flow(poker_engine.players[2:], poker_engine)
            players_flow(poker_engine.players[:2], poker_engine)
            deck.burn()
            flop = deck.get_random_cards(3)
            poker_engine.updateRevealedCards(flop)
            poker_engine.updateBet(0)
            poker_engine.can_bet = True
            if len(poker_engine.players) < 2:
                print("Winner is: ", poker_engine.players[0])
                continue
            players_flow(players[2:], poker_engine)
            players_flow(players[:2], poker_engine)
            deck.burn()
            turn = deck.get_random_cards(1)
            poker_engine.updateRevealedCards(turn)
            poker_engine.can_bet = True
            if len(poker_engine.players) < 2:
                print("Winner is: ", poker_engine.players[0])
                continue
            players_flow(players[2:], poker_engine)
            players_flow(players[:2], poker_engine)
            deck.burn()
            river = deck.get_random_cards(1)
            poker_engine.updateRevealedCards(river)
            poker_engine.can_bet = True
            if len(poker_engine.players) < 2:
                print("Winner is: ", poker_engine.players[0])
                continue
            players_flow(players[2:], poker_engine)
            players_flow(players[:2], poker_engine)
            if len(poker_engine.players) < 2:
                print("Winner is: ", poker_engine.players[0])
                continue
            poker_engine.showdown(deck)
            winner = poker_engine.declare_winner()
            print("Winner is final: ", winner)
