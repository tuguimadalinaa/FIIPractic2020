from Poker.poker_rules import PokerRules


class PokerEngine(PokerRules):
    def __init__(self):
        super().__init__()
        self.players = []
        self.current_bet = 0
        self.deck_bet = 0
        self.revealed_cards = []
        self.can_bet = True

    def updateBet(self, value):
        self.current_bet = value

    def updatePlayers(self, value):
        self.players = value

    def updateDeckBet(self, value):
        self.deck_bet = value

    def updateRevealedCards(self, value):
        self.revealed_cards.extend(value)

    def showdown(self, deck):
        for player in self.players:
            player.current_hand = self.get_hand(self.revealed_cards, player.cards, player, deck)

    def declare_winner(self):
        players_hands = [self.hands_oredered[player.current_hand] for player in self.players]
        index = players_hands.index(min(players_hands))
        return self.players[index]
