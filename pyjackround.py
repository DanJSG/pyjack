from card import Card
from deck import Deck

class PyJackRound:
    def __init__(self, deck):
        self.player_hand, self.house_hand = self._init_hands(deck)
        self.player_total, self.house_total = self._init_totals()
        self.player_is_done = False
        self.complete = False
        self.player_wins = None

    def hit(self, deck):
        self._add_player_card(deck.draw_card())
        if self.player_total > 21:
            self.stand(deck)
    
    def stand(self, deck):
        self.player_is_done = True
        self._run_house(deck)

    def _run_house(self, deck):
        while self.house_total < 17:
            self._add_house_card(deck.draw_card())
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
            print("              " + self._gen_hand_string(self.house_hand))
            print("              Total: " + str(self.house_total))
        else:
            print("                  " + str(self.house_hand[0].value))
        print("**************************************")

    def print_player_hand(self):
        print("My hand: " + self._gen_hand_string(self.player_hand))
        print("Total: " + str(self.player_total))

    def _decide_winner(self):
        if (self.player_total == self.house_total) or (self.player_total > 21 and self.house_total > 21):
            self.player_wins = None
        elif (self.player_total < 22 and self.house_total > 21) or (self.player_total < 22 and self.player_total > self.house_total):
            self.player_wins = True
        else:
            self.player_wins = False

    def _add_player_card(self, card):
        self.player_hand.append(card)
        self.player_total += card.value

    def _add_house_card(self, card):
        self.house_hand.append(card)
        self.house_total += card.value

    def _gen_hand_string(self, hand):
        hand_string = str(hand[0].value) + ", "
        for i in range(1, len(hand)):
            hand_string += str(hand[i].value)
            if i != (len(hand) - 1):
                hand_string += ", "
        return hand_string

    def _init_totals(self):
        player_total = 0
        house_total = 0
        for card in self.player_hand:
            player_total += card.value
        for card in self.house_hand:
            house_total += card.value
        return player_total, house_total

    def _init_hands(self, deck):
        player_hand = []
        house_hand = []
        for _ in range(0, 2):
            player_hand.append(deck.draw_card())
            house_hand.append(deck.draw_card())
        return player_hand, house_hand
