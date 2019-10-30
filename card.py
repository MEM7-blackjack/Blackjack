class Card:
    def __init__(self,num,id): #id is card image name
        self.num = num
        self.id = id
    
    def getNum(self,total):
        if self.num == "A":
            if total <= 21:
                return 11
            else:
                return 1
        else:
            return self.num
    
    def getID(self):
        return self.id