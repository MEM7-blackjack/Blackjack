from card import Card

class Player:

    def __init__(self):
        self.cardlist = []
        self.cardtotal = 0

    def getCardlist(self):
        return self.cardlist

    def getcardtotal(self,i):
        cardtotal = 0
        i = len(self.cardlist)
        return self.__totalrec(cardtotal,i)

    def __totalrec(self,cardtotal,i):
        if i != 0:
            cardtotal += self.cardlist[i-1].getNum(self.__totalrec(cardtotal,i-1))
        else:
            return cardtotal