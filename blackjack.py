from card import *
from deck import *
from graphics import *
from button import *
from window import *
from player import *
from time import sleep

def main():
    #define window
    gamewin = GameWindow()
    #background_image = Image(Point(400,200),"table.gif")
    #background_image.draw(win.getWin())

    #defines and draws the deck
    deck = Deck(400,250,gamewin.getWin())

    #defines player
    player = Player()
    dealer = Player()

    x = 400
    y = 450
    
    pt = gamewin.getWin().getMouse()

    # button check
    while gamewin.clickCheck(pt) != "end":

        if gamewin.clickCheck(pt) == "start":
            winner = round(gamewin,deck,player,dealer)
            if winner == "Player":
                text = drawtext(x,y,"Player Won","Black",gamewin.getWin())
            elif winner == "Dealer":
                text = drawtext(x,y,"House Won","Black",gamewin.getWin())
            else:
                text = drawtext(x,y,"Tie","Black",gamewin.getWin())
            sleep(1)
            text.undraw()
            pt = gamewin.getWin().getMouse()

    gamewin.getWin().close()

def round(gamewin,deck,player,dealer):
    gamewin.end.deactivate()
    gamewin.start.deactivate()
    deck.reset()
    #playerloc and dealerloc decides where the hand should be displayed
    pCardLoc = Point(300,350)
    dCardLoc = Point(300,150)

    
    playerturn = True
    playerLose = False
    dealerLose = False

    pturnloopcount = 0
    dturnloopcount = 0
    #round function runs one round. 
    # A round consists of 6 steps.
    # 1. one card for player, revealed
    # 2. one card for dealer, hidden
    # 3. one card for player, revealed
    # 4. one card for dealer, revealed
    #roundwin variable stores who wins the round. 1 means player, 2 means dealer

    drawPlayer(pturnloopcount,pCardLoc,player,deck,True)
    pturnloopcount += 1
    sleep(0.1)
    drawDealer(dturnloopcount,dCardLoc,dealer,deck,True)
    dturnloopcount += 1
    sleep(0.1)
    drawPlayer(pturnloopcount,pCardLoc,player,deck,True)
    pturnloopcount += 1
    sleep(0.1)
    if player.getCardTotal() == 21:
        return "Player"
    drawDealer(dturnloopcount,dCardLoc,dealer,deck,False)
    dturnloopcount += 1
    sleep(0.1)

    gamewin.hit.activate()
    gamewin.stand.activate()

    pt = gamewin.getWin().getMouse()
    # 5. Player decides their play
    while playerturn == True and playerLose == False:
        # 6. repeat 5 until player stands or loses
        if gamewin.clickCheck(pt) == "hit":
            drawPlayer(pturnloopcount,pCardLoc,player,deck,True)
            if player.getCardTotal() > 21:
                playerLose = True
            # if hit
            # one card for player, revealed
                # check if total over 21
                    # if total below 21, go back to 3
                    # otherwise, player lose
            else:
                pt = gamewin.getWin().getMouse()
                pturnloopcount += 1

        elif gamewin.clickCheck(pt) == "stand":
            # dealer turn
            playerturn = False
    
    if playerLose == False:
        # 7. dealer plays
        while dealer.getCardTotal() < 17 and dealerLose == False:
            sleep(0.1)
            drawDealer(dturnloopcount,dCardLoc,dealer,deck,True)
            if dealer.getCardTotal() > 21:
                dealerLose = True
            else:
                dturnloopcount += 1
        # draws until their total hits 17 or higher.
            # if dealer total over 21, player win
    
     # 8. compare total.
     # 9. closer to 21 wins
    if playerLose == False and dealerLose == False:
        if player.getCardTotal() > dealer.getCardTotal():
            dealerLose = True
        elif player.getCardTotal() < dealer.getCardTotal():
            playerLose = True
        else:
            return "Tie"
        
    if playerLose == True:
        return "Dealer"
    elif dealerLose == True:
        return "Player"
    
def drawPlayer(pturnloopcount,pCardLoc,player,deck,reveal):
    pCardLoc.move(pturnloopcount*20,0)
    player.addCard(deck.draw(pCardLoc,reveal))

def drawDealer(dturnloopcount,dCardLoc,dealer,deck,reveal):
    dCardLoc.move(dturnloopcount*20,0)
    dealer.addCard(deck.draw(dCardLoc,reveal))

def drawtext(x,y,string,col,win): # Simple function to handle common operations for Text objects
    text = Text(Point(x,y),string)
    text.setFill(col)
    text.draw(win)
    return text

    
main() 
