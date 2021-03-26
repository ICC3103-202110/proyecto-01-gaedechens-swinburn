#LAB1 "memorice"
import random

print("Welcome to Memorize, how many pairs of cards do you want to play with?")
pairs = int(input())
####CREANDO EL MASO####
cardsp1 = [] #cards
cardsp1= list(range(1,pairs+1))
cardsp1 = cardsp1*2
random.shuffle(cardsp1)
print ("shuffling the cards...")

pointsp1= 0 #puntaje player 1
pointsp2= 0 #puntaje player 2

while pointsp1 + pointsp2 < pairs:

    
    while len(cardsp1) > 0 :
        print ("Player 1 turn, here are the cards:")
        censoredcardsp1 = []
        for i in cardsp1:
            censoredcardsp1.append("*")
        while True:
            print (censoredcardsp1)
            ncards = len(cardsp1)-1
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
        chosencard1 = cardsp1[chosingcards1] #esta es la carta que se dio vuelta
        thecard = []
        thecard.append(str(chosencard1)) #añade la carta a una lista para poder mostrarla en el tablero ya  las demas censuradas
        
        listh = [] #separa la lista para censurar (hasta esa carta)
        listd = [] #separa la lista para censurar (desde esa carta en adelante)
        liste = [] #separa la lista para censurar (entremedio de las cartas)
        for i in cardsp1[:chosingcards1]:
            listh.append("*")
        for i in cardsp1[chosingcards1+1:]:
            listd.append("*")
        listrep = listh + thecard + listd  #lista con todo censurado excepto la carta a mostrar
        while True:
            print (listrep)
            ncards = len(cardsp1)-1
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

        chosencard2 = cardsp1[chosingcards2] # esta es la segunda carta que se dio vuelta
        thecard2 = []
        thecard2.append(str(chosencard2)) #añade la carta a una lista para poder mostrarla en el tablero ya  las demas censuradas
        
        listh = [] #separa la lista para censurar (hasta esa carta)
        listd = [] #separa la lista para censurar (desde esa carta en adelante)
        liste = [] #separa la lista para censurar (entremedio de las cartas)
        if chosingcards1 < chosingcards2: 
            for i in cardsp1[:chosingcards1]:
                listh.append("*")
            for i in cardsp1[chosingcards1+1:chosingcards2]:
                liste.append("*")
            for i in cardsp1[chosingcards2+1:]:
                listd.append("*")
            listrep = listh+thecard+liste+thecard2+listd
            print (listrep)

        if chosingcards1 > chosingcards2:
            for i in cardsp1[:chosingcards2]:
                listh.append("*")
            for i in cardsp1[chosingcards2+1:chosingcards1]:
                liste.append("*")
            for i in cardsp1[chosingcards1+1:]:
                listd.append("*")
            listrep = listh+thecard2+liste+thecard+listd
            print (listrep)    

        if chosencard1 == chosencard2:
            print("You have won a point, its your turn again")
            pointsp1+=1
            cardsp1.remove(chosencard1) #eliminando las cartas elegidas si esque son iguales
            cardsp1.remove(chosencard2)
            key = False
            
        else:
            print("You lose this turn")
            key = True
            break

    while len(cardsp1) > 0 and key == True :
        print ("Player 2 turn, here are the cards:")
        censoredcardsp1 = []
        for i in cardsp1:
            censoredcardsp1.append("*")
        while True:
            print (censoredcardsp1)
            ncards = len(cardsp1)-1
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
        chosencard1 = cardsp1[chosingcards1] #esta es la carta que se dio vuelta
        thecard = []
        thecard.append(str(chosencard1)) #añade la carta a una lista para poder mostrarla en el tablero ya  las demas censuradas
        
        listh = [] #separa la lista para censurar (hasta esa carta)
        listd = [] #separa la lista para censurar (desde esa carta en adelante)
        liste = [] #separa la lista para censurar (entremedio de las cartas)
        for i in cardsp1[:chosingcards1]:
            listh.append("*")
        for i in cardsp1[chosingcards1+1:]:
            listd.append("*")
        listrep = listh + thecard + listd  #lista con todo censurado excepto la carta a mostrar

        while True:
            print (listrep)
            ncards = len(cardsp1)-1
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

        chosencard2 = cardsp1[chosingcards2] # esta es la segunda carta que se dio vuelta
        thecard2 = []
        thecard2.append(str(chosencard2)) #añade la carta a una lista para poder mostrarla en el tablero ya  las demas censuradas
        
        listh = [] #separa la lista para censurar (hasta esa carta)
        listd = [] #separa la lista para censurar (desde esa carta en adelante)
        liste = [] #separa la lista para censurar (entremedio de las cartas)
        if chosingcards1 < chosingcards2: 
            for i in cardsp1[:chosingcards1]:
                listh.append("*")
            for i in cardsp1[chosingcards1+1:chosingcards2]:
                liste.append("*")
            for i in cardsp1[chosingcards2+1:]:
                listd.append("*")
            listrep = listh+thecard+liste+thecard2+listd
            print (listrep)

        if chosingcards1 > chosingcards2:
            for i in cardsp1[:chosingcards2]:
                listh.append("*")
            for i in cardsp1[chosingcards2+1:chosingcards1]:
                liste.append("*")
            for i in cardsp1[chosingcards1+1:]:
                listd.append("*")
            listrep = listh+thecard2+liste+thecard+listd
            print (listrep)    

        if chosencard1 == chosencard2:
            print("You have won a point, its your turn again")
            pointsp2+=1
            cardsp1.remove(chosencard1) #eliminando las cartas elegidas si esque son iguales
            cardsp1.remove(chosencard2)
            continue
        else:
            print("You lose this turn")
            break
if pointsp2 < pointsp1:
    print ("Player 1 Wins!!")
if pointsp2 > pointsp1:
    print ("Player 2 Wins!!")


