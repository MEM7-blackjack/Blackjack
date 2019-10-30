class Card:
    def __init__(self,id): #id is card image name
        self.num = id[1:]
        self.id = id
    
    def getNum(self,total):
        if self.num == 1:
            if total <= 21:
                return 11
            else:
                return 1
        else:
            return self.num
    
    def getID(self):
        return self.id