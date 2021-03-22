#LAB1 "memorice"
import random

print("Welcome to Memorize, with how many cards pairs do you want to play?")
pairs = int(input())

cardsp1 = [] #cards player1
cardsp2 = [] #cards player2
cardsp1= list(range(1,pairs+1))
cardsp1 = cardsp1*2
cardsp2= list(range(1,pairs+1))
cardsp2 = cardsp2*2
random.shuffle(cardsp1)
random.shuffle(cardsp2)
print ("shuffling the cards...")
print("You only can see your cards once so memorize it!")
print ("player 1 cards:",cardsp1)
print ("player 2 cards:",cardsp2)

pointsp1= 0
pointsp2= 0
print (cardsp1[0])

