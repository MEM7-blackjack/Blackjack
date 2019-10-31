class Card:
    def __init__(self,id): #id is card image name
        self.num = id[1:]
        self.id = id
        self.facedown = False
    
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

    def setSide(self,back):
        """back is a boolean value. True means the card is facing down"""
        self.facedown = back 

    def getSide(self):
        """returns True if the card is facing down"""
        return self.facedown