import random
class Gameboard:
    def __init__(self,pairs):
        self.pairs = pairs
    def gameboard(self,pairs):
        cardsp1 = [] #cards
        cardsp1= list(range(1,self.pairs+1))
        cardsp1 = cardsp1*2
        random.shuffle(cardsp1)
        print ("shuffling the cards...")
        return cardsp1

     
     
     
     
     
 