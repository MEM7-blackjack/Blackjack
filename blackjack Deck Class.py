from card import *
from random import *
class DeckList:
    def __init__(self):
        self.reset()
    


    def reset(self):
        self.deck = []
        suits = ["c","d","h","s"]
        for num in range(1,14):
            for suit in suits:
                self.deck.append(Card(suit+str(num)))

    def draw(self):
        card = randrange(0,len(self.deck))
        return self.deck[card]
        
