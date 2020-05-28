from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.size = 52
        self.cards = self._generate()

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self):
        self.size -= 1
        if self.size < 1:
            raise Exception()
        return self.cards.pop()

    def _generate(self):
        cards = []
        for i in range(0, self.size):
            cards.append(Card(i))
        return cards
