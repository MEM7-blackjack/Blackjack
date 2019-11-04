from card import *
from random import *
from graphics import *

class Deck:
    def __init__(self,x,y,win):
        self.x = x
        self.y = y
        self.win = win
        self.reset()
        self.stack = Image(Point(x,y),"playingcards/b1fv.gif")
        self.stack.draw(self.win)
        self.cardsOnBoard = []

    def reset(self):
        #refills the deck
        self.deck = []
        suits = ["c","d","h","s"]
        for num in range(1,14):
            for suit in suits:
                self.deck.append(Card(suit+str(num)))

        # Clears the cards on the board
        if len(self.cardsOnBoard) != 0:
            for cards in self.cardsOnBoard:
                cards.undraw()

    def draw(self,pt,reveal):
        """draws from deck, animates the drawn card. pt stands for Point object that represents the destination"""
        #reveal is a boolean for whether to immediately show the card or not
        desx,desy = pt.getX(), pt.getY()
        cardindex = randrange(0,len(self.deck))
        card = self.deck[cardindex]

        # Animation
        cardimageback = Image(Point(self.x,self.y),"playingcards/b1fv.gif")
        cardimageback.draw(self.win)
        cardimageback.move(desx-self.x,desy-self.y)
        self.cardsOnBoard.append(cardimageback)
            
        if reveal:
            cardimagefront = Image(cardimageback.getAnchor(),"playingcards/"+card+".gif")
            cardimageback.undraw()
            cardimagefront.draw(self.win)
            self.cardsOnBoard.append(cardimagefront)

        return card
        
        
