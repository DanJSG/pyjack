from card import Card
from deck import Deck
from hand import Hand

class PyJackRound:
    def __init__(self, deck):
        self.player_hand, self.house_hand = self._init_hands(deck)
        self.player_is_done = False
        self.complete = False
        self.player_wins = None

    def hit(self, deck):
        self.player_hand.add_card(deck.draw_card())
        if self.player_hand.total > 21:
            self.stand(deck)
    
    def stand(self, deck):
        self.player_is_done = True
        self._run_house(deck)

    def _run_house(self, deck):
        while self.house_hand.total < 17:
            self.house_hand.add_card(deck.draw_card())
        self.complete = True
        self._decide_winner()

    def print_winner(self):
        if self.player_wins == None:
            print("Draw!")
        elif self.player_wins:
            print("Player wins!")
        else:
            print("House wins!")

    def print_house_hand(self):
        print("*************** House ***************")
        if self.player_is_done:
            print("              " + self.house_hand.string)
            print("              Total: " + str(self.house_hand.total))
        else:
            print("                  " + str(self.house_hand.cards[0].value))
        print("**************************************")

    def print_player_hand(self):
        print("My hand: " + self.player_hand.string)
        print("Total: " + str(self.player_hand.total))

    def _decide_winner(self):
        if (self.player_hand.total == self.house_hand.total) or (self.player_hand.total > 21 and self.house_hand.total > 21):
            self.player_wins = None
        elif (self.player_hand.total < 22 and self.house_hand.total > 21) or (self.player_hand.total < 22 and self.player_hand.total > self.house_hand.total):
            self.player_wins = True
        else:
            self.player_wins = False

    def _init_hands(self, deck):
        player_hand = Hand()
        house_hand = Hand()
        for _ in range(0, 2):
            player_hand.add_card(deck.draw_card())
            house_hand.add_card(deck.draw_card())
        return player_hand, house_hand
