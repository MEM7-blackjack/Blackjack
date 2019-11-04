from graphics import *
from button import *

class GameWindow(GraphWin):
    """Subclass of GraphWin designed for blackjack"""

    def __init__(self):

        self.win = GraphWin("Blackjack!",800,500)
        background_image = Image(Point(400,200),"table.png")
        background_image.draw(win)

        self.hit = Button(win, Point(300,300),60,30,"HIT")
        self.stand = Button(win, Point(500,300),60,30,"STAND")
        self.end = Button(win, Point(100,300),60,30,"EXIT")
        self.reset = Button(win, Point(400,400),60,30,"RESET")

        self.hit.activate()
        self.stand.activate()
        self.end.activate()
        self.reset.activate()

    def clickCheck(self,pt):
        """function that returns the name of the button that was pressed. Takes in Point object"""
        if self.hit.isClicked(pt):
            return "hit"
        elif self.stand.isClicked(pt):
            return "stand"
        elif self.end.isClicked(pt):
            return "end"
        elif self.reset.isClicked(pt):
            return "reset"

    def getWin(self):
        return self.win