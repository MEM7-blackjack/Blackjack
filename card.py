from graphics import *

class Card:
    def __init__(self,id,side): #id is card image name
        self.num = int(id[1:])
        self.id = id
        self.faceup = side
        self.cardimage = ""
        self.x = 0
        self.y = 0

    def setPos(self,pt):
        self.x = pt.getX()
        self.y = pt.getY()
    
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

    def setSide(self,side,gamewin):
        """back is a boolean value. True means the card is facing down"""
        if self.faceup != side:
            self.faceup = side 

            if isinstance(self.cardimage, Image):
                self.cardimage.undraw()

            #draw new side
            if self.faceup:
                self.cardimage = Image(Point(self.x,self.y),"playingcards/"+self.id+".gif")
                self.cardimage.draw(gamewin)
            else:
                self.cardimage = Image(Point(self.x,self.y),"playingcards/b1fv.gif")
                self.cardimage.draw(gamewin)

            return self.cardimage