import random
class Gameboard:
    cardsp1 = []
    def __init__(self,pairs, cardsp1):
        self.pairs = pairs
        self.cardsp1 = cardsp1
    def gameboard(self,pairs, cardsp1):
        cardsp1= list(range(1,self.pairs+1)) #crating the cards for the game
        cardsp1 = cardsp1*2
        self.cardsp1 = cardsp1
        random.shuffle(cardsp1) #shuffling the cards
        print ("shuffling the cards...")
        Gameboard.cardsp1 = cardsp1 #saving the cards on the constant
        return cardsp1

     
     
