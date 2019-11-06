from graphics import *

class Card:
    def __init__(self,id,side): #id is card image name
        self.num = int(id[1:])
        self.id = id
        self.faceup = side
    
    def getNum(self,total):
        """returns the number on the card"""
        if self.num == 1:
            if total <= 10:
                return 11
            else:
                return 1
        else:
            return self.num
    
    def getID(self):
        """Example id: c1"""
        return self.id

    def setSide(self,pt,side,gamewin):
        """back is a boolean value. True means the card is facing down"""
        if self.faceup != side:
            self.faceup = side 
            #draw new side
            if self.faceup:
                cardimage = Image(pt,"playingcards/"+self.id+".gif")
                cardimage.draw(gamewin)
            else:
                cardimage = Image(pt,"playingcards/b1fv.gif")
                cardimage.draw(gamewin)

            return cardimage