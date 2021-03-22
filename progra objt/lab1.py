#LAB1 "memorice"
import random

print("Welcome to Memorize, with how many cards pairs do you want to play?")
pairs = int(input())
####CREANDO LOS MASOS####
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

pointsp1= 0 #puntaje player 1
pointsp2= 0 #puntaje player 2

#####PRIMERA JUGADA#####
print ("Player 1 turn, here are your cards:")
censoredcardsp1 = []
for i in cardsp1:
    censoredcardsp1.append("*")
print (censoredcardsp1)
print("With the number 0 the first card is selected, with 1 the second and so on, select the card to turn: ")
chosingcards1= int(input()) #elige la posicion de la carta a dar vuelta
#print (cardsp1[chosingcards1]) #imprime la carta a dar vuelta
thecard = list(str(cardsp1[chosingcards1])) #convierte la carta que se dio vuelta en una lista para despues sumar listas y censurar las demas

listh = [] #separa la lista para censurar
listd = [] #separa la lista para censurar
for i in cardsp1[:chosingcards1]:
    listh.append("*")
for i in cardsp1[chosingcards1+1:]:
    listd.append("*")
listrep = listh + thecard + listd  #lista con todo censurado excepto la carta a mostrar
print (listrep)

