from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.string = ""

    def add_card(self, card):
        self.cards.append(card)
        self.total += card.value
        if len(self.cards) == 1:
            self.string += ", "
        self.string += str(card.value)