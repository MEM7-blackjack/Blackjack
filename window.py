from graphics import *
from button import *

class GameWindow(GraphWin):
    """Subclass of GraphWin designed for blackjack"""

    def __init__(self):

        self.win = GraphWin("Blackjack!",800,500)
        
        background_image = Image(Point(400,200),"table.gif")
        background_image.draw(self.win)

        self.hit = Button(self.win, Point(500,200),60,30,"HIT")
        self.stand = Button(self.win, Point(500,350),60,30,"STAND")
        self.end = Button(self.win, Point(100,350),60,30,"EXIT")
        self.start = Button(self.win, Point(100,300),60,30,"START")

        self.hit.deactivate()
        self.stand.deactivate()
        self.end.activate()
        self.start.activate()

    def clickCheck(self,pt):
        """function that returns the name of the button that was pressed. Takes in Point object"""
        if self.hit.isClicked(pt):
            return "hit"
        elif self.stand.isClicked(pt):
            return "stand"
        elif self.end.isClicked(pt):
            return "end"
        elif self.start.isClicked(pt):
            return "start"

    # if win.clickCheck(pt) = "hit"
        # 

    def getWin(self):
        return self.win

def main():
    window = GameWindow()

if __name__ == "__main__":
    main()