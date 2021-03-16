from Poker.generators import cardsGenerator, playersGenerator, chips_generator
from Poker.deck import Deck
from Poker.pokerStats import PokerStats
import json
from copy import deepcopy
from collections import defaultdict


def players_flow(players, poker_status):
    for player in players:
        action, chips_value = player.take_action(poker_status.can_bet, poker_status.current_bet)
        if action == "Fold":
            players.remove(player)
        elif action == "Bet":
            poker_status.updateBet(chips_value)
            poker_status.can_bet = False
        elif action == "Raise":
            poker_status.updateBet(poker_status.current_bet + chips_value)
        else:
            poker_status.updateBet(chips_value)
        poker_status.updateDeckBet(poker_status.deck_bet + chips_value)


def is_one_pair(revealed_cards, cards):
    first_card = cards[0].number
    second_card = cards[0].number
    for card in revealed_cards:
        if card.number == first_card or card.number == second_card:
            return True
    return False


def is_two_pair(revealed_cards, cards):
    is_two_pair = 0
    first_card = cards[0].number
    second_card = cards[1].number
    for card in revealed_cards:
        card_number = card.number
        if card_number == first_card or card_number == second_card:
            is_two_pair += 1
        if is_two_pair == 2:
            return True
    return False


def is_three_of_a_kind(revealed_cards, cards):
    is_two_pair = 0
    first_card = cards[0].number
    second_card = cards[1].number
    for card in revealed_cards:
        card_number = card.number
        if card_number == first_card or card_number == second_card:
            is_two_pair += 1
        if is_two_pair == 3:
            return True
    return False


def is_straight(revealed_cards, cards):
    new_list = deepcopy(revealed_cards)
    new_list.append(cards[0])
    new_list.append(cards[1])
    if cards[0] == cards[1]:
        return False
    rank_set = {card.number for card in new_list}
    return (max(rank_set) - min(rank_set) + 1) == 5


def is_flush(revealed_cards, cards):
    first_suit = cards[0].suit
    second_suit = cards[0].suit
    if first_suit != second_suit:
        return False
    suits = deck.get_suits_in_given_cards(revealed_cards)
    d = {item: suits.count(item) for item in suits}
    result = max(d.items(), key=lambda x: x[1])
    if result[1] < 3:
        return False
    if is_flush:
        if result[0] == first_suit == second_suit:
            return True
    return False


def is_full_house(revealed_cards, cards):
    revealed_suits = deck.get_numbers_in_given_cards(revealed_cards)
    first_suit = cards[0].number
    second_suit = cards[0].number
    if first_suit != second_suit:
        if first_suit in revealed_suits and second_suit in revealed_suits:
            if revealed_suits.count(first_suit) > 2 and revealed_suits.count(second_suit) > 1:
                return True
            if revealed_suits.count(second_suit) > 2 and revealed_suits.count(first_suit) > 1:
                return True
    return False


def is_four_of_the_kind(revealed_cards, cards):
    first_number = cards[0].number
    second_number = cards[0].number
    if first_number != second_number:
        return False
    revealed_numbers = deck.get_numbers_in_given_cards(revealed_cards)
    if revealed_numbers.count(first_number) == 2:
        return True
    return False


def is_straight_flush(revealed_cards, cards):
    return is_flush(revealed_cards, cards) and is_straight(revealed_cards, cards)


def is_royal_flush(revealed_cards, cards):
    can_be_in_royal_flush = [10, "Queen", "Jack", "King", 1]
    if cards[0].suit != cards[0].suit:
        return False
    if cards[0].suit != revealed_cards[0].suit:
        return False
    revealed_suits = deck.get_suits_in_given_cards(revealed_cards)
    if revealed_suits.count(cards[0]) < 3:
        return False
    revealed_numbers = deck.get_numbers_in_given_cards(revealed_cards)
    elements_from_royal_flush_shown = [i for i in revealed_numbers if i in can_be_in_royal_flush]
    if len(elements_from_royal_flush_shown) < 3:
        return False
    if cards[0].number in elements_from_royal_flush_shown or cards[1].number in elements_from_royal_flush_shown:
        return False
    if cards[0].number not in can_be_in_royal_flush or cards[1].number not in can_be_in_royal_flush:
        return False
    return True


def get_hand(revealed_cards, cards):
    if is_royal_flush(revealed_cards, cards):
        return "Royal flush"
    if is_straight_flush(revealed_cards, cards):
        return "Four straigh flush"
    if is_four_of_the_kind(revealed_cards, cards):
        return "Four of the kind"
    if is_flush(revealed_cards, cards):
        return "Flush"
    if is_full_house(revealed_cards, cards):
        return "Full House"
    if is_straight(revealed_cards, cards):
        return "Straight"
    if is_three_of_a_kind(revealed_cards, cards):
        return "Three of a kind"
    if is_two_pair(revealed_cards, cards):
        return "Two Pair"
    if is_one_pair(revealed_cards, cards):
        return "One Pair"


def showdown(players, poker_status):
    for player in players:
        player.current_hand = get_hand(poker_status.revealed_cards, player.cards)


if __name__ == "__main__":
    configurations = json.load(open("Poker/game_config.json", "r"))
    cards = cardsGenerator.generate_cards()
    rounds = configurations["rounds"]
    chips_config = configurations["chips"]
    game_chips = list(chips_generator.generate_chips(chips_config))
    current_bet = configurations["entry_sum"]

    if configurations["type_of_game"] == "texas_holdem":
        for round in range(rounds):
            poker_status = PokerStats([], 0)
            deck = Deck(cards)
            deck.shuffle()
            players = list(playersGenerator.generate_players(configurations["number_of_players"], game_chips))
            poker_status.updatePlayers(players)
            sb = players[0].bet()
            poker_status.updateBet(sb)
            bb = players[1].bet()
            poker_status.updateBet(bb)
            poker_status.updateDeckBet(sb + bb)
            poker_status.can_bet = False
            for player in players:
                player.cards = deck.get_random_cards(2)
            players_flow(players[2:], poker_status)
            players_flow(players[:2], poker_status)
            deck.burn()
            flop = deck.get_random_cards(3)
            poker_status.updateRevealedCards(flop)
            poker_status.updateBet(0)
            poker_status.can_bet = True
            players_flow(players[2:], poker_status)
            players_flow(players[:2], poker_status)
            deck.burn()
            turn = deck.get_random_cards(1)
            poker_status.updateRevealedCards(turn)
            poker_status.can_bet = True
            players_flow(players[2:], poker_status)
            players_flow(players[:2], poker_status)
            deck.burn()
            river = deck.get_random_cards(1)
            poker_status.updateRevealedCards(river)
            poker_status.can_bet = True
            players_flow(players[2:], poker_status)
            players_flow(players[:2], poker_status)
            showdown(players, poker_status)
