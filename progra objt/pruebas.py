def cartas(chosingcards1):
    while True:
        try:
            chosingcards1 = int(input("With the number 0 the first card of the list is selected, with 1 the second and so on, select the card to turn: "))
        except ValueError:
            print("Debes escribir un número.")
            continue
        if chosingcards1 < 0:
            print("Debes escribir un número positivo.")
            continue
        if chosingcards1 > len(cardsp1)*2:
            print("Debes elegir una carta dentro del rango")
            continue
        else:
            break
    return chosingcards1
    print (chosingcards1, "posicion de carta a dar vuelta")
cartas(True)
