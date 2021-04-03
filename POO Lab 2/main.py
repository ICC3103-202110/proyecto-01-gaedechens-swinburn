#Laboratorio 2 poo main
from gameboard import Gameboard
from points import Points
from game import Game
def main():
    many = int(input("how many cards pairs: "))
    cardsp1 = []
    play = Gameboard(many,cardsp1)
    play.gameboard(many,cardsp1)
    Game(many,Points.pointsp1, Points.pointsp2, Gameboard.cardsp1).game()

if __name__ == "__main__":
    main()
