from deck import Deck
from pyjackround import PyJackRound
import os

deck = Deck()
deck.shuffle()
play_again = True
player_score = 0
house_score = 0

while play_again:

    try:
        round = PyJackRound(deck)
    except:
        deck = Deck()
        continue

    while not round.player_is_done:
        os.system("cls")
        print("Player Score: " + str(player_score) + "   ||   House Score: " + str(house_score))
        round.print_house_hand()
        round.print_player_hand()
        key = input()
        if key == "a":
            try:
                round.hit(deck)
            except:
                deck = Deck()
        elif key == "s":
            try:
                round.stand(deck)
            except:
                deck = Deck()

    if round.player_wins == None:
        player_score += 1
        house_score += 1
    elif round.player_wins:
        player_score += 1
    else:
        house_score += 1
    
    os.system("cls")
    print("Player Score: " + str(player_score) + "   ||   House Score: " + str(house_score))
    round.print_house_hand()
    round.print_player_hand()
    round.print_winner()

    key = input("Press q to quit, anything else to continue.")
    if key == 'q':
        play_again = False
