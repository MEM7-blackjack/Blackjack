from card import *
from deck import *
from graphics import *
from button import *
from window import *
from player import *

def main():
    #define window
    win = GameWindow()

    #defines and draws the deck
    deck = Deck(400,250,win.getWin())

    #defines player
    player = Player()
    dealer = Player()



def round():
    #round function runs one round. 
    # A round consists of 6 steps.

    # 1. one card for player, revealed
    # 2. one card for dealer, hidden
    # 3. one card for player, revealed
    # 4. one card for dealer, revealed
    # 3. Player decides their play
        # if hit
            # one card for player, revealed
                # check if total over 21
                    # if total below 21, go back to 3
                    # otherwise, player lose
    # 4. repeat 3 until player stands or loses
    # 5. dealer plays
        # draws until their total hits 17 or higher.
            # if dealer total over 21, player win
    # 6. compare total.
    # 7. closer to 21 wins
    
    #playerloc and dealerloc decides where the hand should be displayed
    playerLoc = Point(400,150)
    dealerLoc = Point(400,350)

    #win variable stores who wins the round.
    win = 0
    while win == 0:



    
main() 
