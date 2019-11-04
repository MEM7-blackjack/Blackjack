from card import Card

class Player:
    """Player is a class that holds the cardlist and calculates the total value of the cards. Call __init__ to reset card hand"""
    def __init__(self):
        self.cardlist = []
        self.cardtotal = 0

    def addCard(self,cardobj):
        """Adds a card object to the cardlist"""
        self.cardlist.append(cardobj)

    def getCardlist(self):
        """Returns cardlist"""
        return self.cardlist

    def getCardTotal(self):
        cardtotal = 0
        if self.cardlist != []:
            i = len(self.cardlist)
            self.__totalrec(cardtotal,i)
            return self.cardtotal
        else:
            return "Null"

    def __totalrec(self,cardtotal,i):
        if i != 0:
            
            cardtotal = int(self.cardlist[i-1].getNum(self.__totalrec(cardtotal,i-1)))
            print(cardtotal)
            self.cardtotal += cardtotal
            return cardtotal
        else:
            return cardtotal

def main():
    print("Testing player Class")
    player = Player()
    card1 = Card("d1")
    card2 = Card("s1")
    card3 = Card("h4")
    player.addCard(card1)
    player.addCard(card2)
    player.addCard(card3)

    print(player.getCardlist())
    print(player.getCardTotal())
    

if __name__ == "__main__":
    main()
