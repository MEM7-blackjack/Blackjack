class Gambler:

    def __init__(self,bal):
        self.Bank = bal
        self.Bet = 0
    
    def bet(self,amount):
        if amount > self.Bank:
            return False
        else:
            self.Bank = self.Bank - amount
            self.Bet = amount
            return True

    def betAmount(self):
        """Returns the amount currently being bet"""
        return self.Bet

    def bal(self):
        """Returns remaining money"""
        return self.Bank

    def resolveBet(self,outcome):
        if outcome == "win":
            self.Bank = self.Bank + self.Bet*2
            self.Bet = 0
        elif outcome == "lose":
            self.Bet =0
        elif outcome == "push":
            self.Bank = self.Bank + self.Bet
            self.Bet = 0
        elif outcome == "blackjack":
            self.Bank = self.Bank + int(self.Bet*2.5)
            self.Bet = 0
        else:
            return False

    
