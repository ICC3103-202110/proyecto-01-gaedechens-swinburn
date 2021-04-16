from gameboard import Gameboard
from points import Points

class Game(Points):
    def __init__(self, pairs, pointsp1, pointsp2, cardsp1):
        #super(Game,self).__init__(pairs,pointsp1,pointsp2, cardsp1)
        self.pairs = pairs
        self.pointsp1 = Points.pointsp1
        self.pointsp2 = Points.pointsp2
        self.cardsp1 = Gameboard.cardsp1
    

    def game(self):
        while self.pointsp1 + self.pointsp2 < self.pairs:

            
            while len(self.cardsp1) > 0 :
                print ("Player 1 turn, here are the cards:")
                censoredcardsp1 = []
                for i in self.cardsp1:
                    censoredcardsp1.append("*")
                while True:
                    print (censoredcardsp1)
                    ncards = len(self.cardsp1)-1
                    try:
                        chosingcards1 = int(input("With the number 0 the first card of the list is selected, with 1 the second and so on, select the card to turn: "))
                    except ValueError:
                        print("You must write a number.")
                        continue
                    if chosingcards1 < 0:
                        print("You must write a positive number.")
                        continue
                    if chosingcards1 > ncards:
                        print("You must choose a card within the range")
                        continue
                    else:
                        break
                chosencard1 = self.cardsp1[chosingcards1] #this is the card that was turned over
                thecard = []
                thecard.append(str(chosencard1)) #add the card to a list to be able to show it on the board and to the other censored
                
                listh = [] #separate the list to censor (until this card)
                listd = [] #separate the list to censor (from this card on)
                liste = [] #separate the list to censor (between the cards)
                for i in self.cardsp1[:chosingcards1]:
                    listh.append("*")
                for i in self.cardsp1[chosingcards1+1:]:
                    listd.append("*")
                listrep = listh + thecard + listd  #list with everything censored except the card to show
                while True:
                    print (listrep)
                    ncards = len(self.cardsp1)-1
                    try:
                        chosingcards2 = int(input("Now select another card to flip and see if it is his pair: "))
                    except ValueError:
                        print("You must write a number.")
                        continue
                    if chosingcards2 < 0:
                        print("You must write a positive number.")
                        continue
                    if chosingcards2 > ncards:
                        print("You must choose a card within the range.")
                        continue
                    if chosingcards1 == chosingcards2:
                        print("You can't turn the same card over again.")
                        continue
                    else:
                        break

                chosencard2 = self.cardsp1[chosingcards2] # this is the second card that was turned over
                thecard2 = []
                thecard2.append(str(chosencard2)) #add the card to a list to be able to show it on the board and to the other censored
                
                listh = [] #separate the list to censor (until this card)
                listd = [] #separate the list to censor (from this card on)
                liste = [] #separate the list to censor (between the cards)
                if chosingcards1 < chosingcards2: 
                    for i in self.cardsp1[:chosingcards1]:
                        listh.append("*")
                    for i in self.cardsp1[chosingcards1+1:chosingcards2]:
                        liste.append("*")
                    for i in self.cardsp1[chosingcards2+1:]:
                        listd.append("*")
                    listrep = listh+thecard+liste+thecard2+listd
                    print (listrep)

                if chosingcards1 > chosingcards2:
                    for i in self.cardsp1[:chosingcards2]:
                        listh.append("*")
                    for i in self.cardsp1[chosingcards2+1:chosingcards1]:
                        liste.append("*")
                    for i in self.cardsp1[chosingcards1+1:]:
                        listd.append("*")
                    listrep = listh+thecard2+liste+thecard+listd
                    print (listrep)    

                if chosencard1 == chosencard2:
                    print("You have won a point, its your turn again")
                    self.pointsp1+=1
                    self.cardsp1.remove(chosencard1) #eliminating the chosen cards if they are the same
                    self.cardsp1.remove(chosencard2)
                    key = False
                    
                else:
                    print("You lose this turn")
                    key = True
                    break

            while len(self.cardsp1) > 0 and key == True :
                print ("Player 2 turn, here are the cards:")
                censoredcardsp1 = []
                for i in self.cardsp1:
                    censoredcardsp1.append("*")
                while True:
                    print (censoredcardsp1)
                    ncards = len(self.cardsp1)-1
                    try:
                        chosingcards1 = int(input("With the number 0 the first card of the list is selected, with 1 the second and so on, select the card to turn: "))
                    except ValueError:
                        print("You must write a number.")
                        continue
                    if chosingcards1 < 0:
                        print("You must write a positive number.")
                        continue
                    if chosingcards1 > ncards:
                        print("You must choose a card within the range.")
                        continue
                    else:
                        break
                chosencard1 = self.cardsp1[chosingcards1] #this is the card that was turned over
                thecard = []
                thecard.append(str(chosencard1)) #add the card to a list to be able to show it on the board and to the other censored
                
                listh = [] #separate the list to censor (until this card)
                listd = [] #separate the list to censor (from this card on)
                liste = [] #separate the list to censor (between the cards)
                for i in self.cardsp1[:chosingcards1]:
                    listh.append("*")
                for i in self.cardsp1[chosingcards1+1:]:
                    listd.append("*")
                listrep = listh + thecard + listd  #list with everything censored except the card to show

                while True:
                    print (listrep)
                    ncards = len(self.cardsp1)-1
                    try:
                        chosingcards2 = int(input("Now select another card to flip and see if it is his pair: "))
                    except ValueError:
                        print("You must write a number.")
                        continue
                    if chosingcards2 < 0:
                        print("You must write a positive number.")
                        continue
                    if chosingcards2 > ncards:
                        print("You must choose a card within the range.")
                        continue
                    if chosingcards1 == chosingcards2:
                        print("You can't turn the same card over again.")
                        continue
                    else:
                        break

                chosencard2 = self.cardsp1[chosingcards2] # this is the second card that was turned over
                thecard2 = []
                thecard2.append(str(chosencard2)) #add the card to a list to be able to show it on the board and to the other censored
                
                listh = [] #separate the list to censor (until this card)
                listd = [] #separate the list to censor (from this card on)
                liste = [] #separate the list to censor (between the cards)
                if chosingcards1 < chosingcards2: 
                    for i in self.cardsp1[:chosingcards1]:
                        listh.append("*")
                    for i in self.cardsp1[chosingcards1+1:chosingcards2]:
                        liste.append("*")
                    for i in self.cardsp1[chosingcards2+1:]:
                        listd.append("*")
                    listrep = listh+thecard+liste+thecard2+listd
                    print (listrep)

                if chosingcards1 > chosingcards2:
                    for i in self.cardsp1[:chosingcards2]:
                        listh.append("*")
                    for i in self.cardsp1[chosingcards2+1:chosingcards1]:
                        liste.append("*")
                    for i in self.cardsp1[chosingcards1+1:]:
                        listd.append("*")
                    listrep = listh+thecard2+liste+thecard+listd
                    print (listrep)    

                if chosencard1 == chosencard2:
                    print("You have won a point, its your turn again")
                    self.pointsp2+=1
                    self.cardsp1.remove(chosencard1) #eliminating the chosen cards if they are the same
                    self.cardsp1.remove(chosencard2)
                    continue
                else:
                    print("You lose this turn")
                    break
        if self.pointsp2 < self.pointsp1:
            print ("Player 1 Wins!!")
        if self.pointsp2 > self.pointsp1:
            print ("Player 2 Wins!!")
        if self.pointsp1 == self.pointsp2:
            print ("it´s a tie!")
