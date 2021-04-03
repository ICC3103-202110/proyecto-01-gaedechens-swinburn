#Laboratorio 2 poo main
from gameboard import Gameboard
from points import Points
def main():
    many = int(input("how many cards pairs: "))
    play = Gameboard(many)
    print(play.gameboard(many))
    





if __name__ == "__main__":
    main()
