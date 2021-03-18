from copy import deepcopy


class PokerRules:
    def __init__(self):
        self.hands_oredered = {"Royal flush": 1, "Four straigh flush": 2, "Four of the kind": 3, "Flush": 4,
                               "Full House": 5,
                               "Straight": 6, "Three of a kind": 7, "Two Pair": 8, "One Pair": 9, "None": 10}

    def is_one_pair(self, revealed_cards, cards, player):
        first_card = cards[0].number
        second_card = cards[1].number
        for card in revealed_cards:
            if card.number == first_card:
                player.wining_cards = [card]
                return True
            if card.number == second_card:
                player.wining_cards = [card]
                return True
        return False

    def is_two_pair(self, revealed_cards, cards, player):
        is_two_pair = 0
        first_card = cards[0].number
        second_card = cards[1].number
        winning_cards = []
        for card in revealed_cards:
            card_number = card.number
            if card_number == first_card or card_number == second_card:
                is_two_pair += 1
                winning_cards.append(card)
            if is_two_pair == 2:
                player.wining_cards = winning_cards
                return True
        return False

    def is_three_of_a_kind(self, revealed_cards, cards, player):
        is_two_pair = 0
        first_card = cards[0].number
        second_card = cards[1].number
        winning_cards = []
        for card in revealed_cards:
            card_number = card.number
            if card_number == first_card or card_number == second_card:
                is_two_pair += 1
                winning_cards.append(card)
            if is_two_pair == 3:
                player.wining_cards = winning_cards
                return True
        return False

    def is_straight(self, revealed_cards, cards, player):
        new_list = deepcopy(revealed_cards)
        new_list.append(cards[0])
        new_list.append(cards[1])
        if cards[0] == cards[1]:
            return False
        rank_set = {card.number for card in new_list}
        player.wining_cards = [max(rank_set)]
        return (max(rank_set) - min(rank_set) + 1) == 5

    def is_full_house(self, revealed_cards, cards, player, deck):
        revealed_numbers = deck.get_numbers_in_given_cards(revealed_cards)
        first_number = cards[0].number
        second_number = cards[0].number
        if first_number != second_number:
            if first_number in revealed_numbers and second_number in revealed_numbers:
                if revealed_numbers.count(first_number) > 2 and revealed_numbers.count(second_number) > 1:
                    player.wining_cards = [card for card in revealed_cards if card.number == first_number]
                    player.wining_cards.append(cards[0])
                    player.wining_cards.append(cards[1])
                    return True
                if revealed_numbers.count(second_number) > 2 and revealed_numbers.count(first_number) > 1:
                    return True
        return False

    def is_flush(self, revealed_cards, cards, player, deck):
        first_suit = cards[0].suit
        second_suit = cards[0].suit
        if first_suit != second_suit:
            return False
        suits = deck.get_suits_in_given_cards(revealed_cards)
        d = {item: suits.count(item) for item in suits}
        result = max(d.items(), key=lambda x: x[1])
        if result[1] < 3:
            return False
        if result[0] == first_suit == second_suit:
            winning_suit_cards = [card for card in revealed_cards if card.suit == result[0]]
            winning_cards = [cards[0], cards[1], winning_suit_cards[0], winning_suit_cards[1], winning_suit_cards[2]]
            player.wining_cards = winning_cards
            return True
        return False

    def is_four_of_the_kind(self, revealed_cards, cards, player, deck):
        first_number = cards[0].number
        second_number = cards[0].number
        if first_number != second_number:
            return False
        revealed_numbers = deck.get_numbers_in_given_cards(revealed_cards)
        if revealed_numbers.count(first_number) == 2:
            return True
        return False

    def is_straight_flush(self, revealed_cards, cards, player, deck):
        return self.is_flush(revealed_cards, cards, player, deck) and self.is_straight(revealed_cards, cards, player)

    def is_royal_flush(self, revealed_cards, cards, deck):
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

    def get_hand(self, revealed_cards, cards, player, deck):
        if self.is_royal_flush(revealed_cards, cards, deck):
            return "Royal flush"
        if self.is_straight_flush(revealed_cards, cards, player, deck):
            return "Four straigh flush"
        if self.is_four_of_the_kind(revealed_cards, cards, player, deck):
            return "Four of the kind"
        if self.is_flush(revealed_cards, cards, player, deck):
            return "Flush"
        if self.is_full_house(revealed_cards, cards, player, deck):
            return "Full House"
        if self.is_straight(revealed_cards, cards, player):
            return "Straight"
        if self.is_three_of_a_kind(revealed_cards, cards, player):
            return "Three of a kind"
        if self.is_two_pair(revealed_cards, cards, player):
            return "Two Pair"
        if self.is_one_pair(revealed_cards, cards, player):
            return "One Pair"
        return "None"
