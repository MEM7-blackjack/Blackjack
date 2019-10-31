from card import *
from deck import *
from graphics import *
from button import *

def main():
    hit, stand, end, reset, win = graphic()

    deck = DeckList()
    
def graphic():
    win = GraphWin("Blackjack!", 800,500)
    background_image = Image(Point(400,200),"table.png")
    background_image.draw(win)

    hit = Button(win, Point(300,300),60,30,"HIT")
    stand = Button(win, Point(500,300),60,30,"STAND")
    end = Button(win, Point(100,300),60,30,"EXIT")
    reset = Button(win, Point(400,400),60,30,"RESET")

    hit.activate()
    stand.activate()
    end.activate()
    reset.activate()
    return hit, stand, end, reset, win


def drawcardgraphics(loc,id,win): #loc is location of the new card represented by number of card in the list, win is for window
# Add code for displaying drawing new card here: animation that draws a new card and moves it to the right place. 


    
main() 
