from deck import Deck
from pyjackround import PyJackRound
import os

deck = Deck()
deck.shuffle()
play_again = True

while play_again:

    round = PyJackRound(deck)

    while not round.player_is_done:
        os.system("cls")
        round.print_house_hand()
        round.print_player_hand()
        key = input()
        if key == "a":
            round.hit(deck)
        elif key == "s":
            round.stand(deck)

    os.system("cls")
    round.print_house_hand()
    round.print_player_hand()
    round.print_winner()

    key = input("Press q to quit, anything else to continue.")
    if key == 'q':
        play_again = False
