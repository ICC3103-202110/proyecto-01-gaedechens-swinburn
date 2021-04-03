import random
class Gameboard:
    cardsp1 = []
    def __init__(self,pairs, cardsp1):
        self.pairs = pairs
        self.cardsp1 = cardsp1
    def gameboard(self,pairs, cardsp1):
        cardsp1= list(range(1,self.pairs+1))
        cardsp1 = cardsp1*2
        self.cardsp1 = cardsp1
        random.shuffle(cardsp1)
        print ("shuffling the cards...")
        Gameboard.cardsp1 = cardsp1
        return cardsp1

     
     
