class PokerStats:
    def __init__(self, players, bet):
        self.players = players
        self.current_bet = bet
        self.deck_bet = 0
        self.revealed_cards = []
        self.can_bet = True
        pass

    def updateBet(self, value):
        self.current_bet = value

    def updatePlayers(self, value):
        self.players = value

    def updateDeckBet(self, value):
        self.deck_bet = value

    def updateRevealedCards(self, value):
        self.revealed_cards.extend(value)
