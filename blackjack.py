from card import *
from deck import *
from graphics import *
from button import *

def main():
    hit, stand, end, reset, win = graphic()
    
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
    
graphic()
 
