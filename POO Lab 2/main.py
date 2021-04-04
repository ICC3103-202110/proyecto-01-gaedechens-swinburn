#Laboratorio 2 poo main
from gameboard import Gameboard
from points import Points
from game import Game
def main():
    many = int(input("Welcome to Memorize, how many pairs of cards do you want to play with?"))
    cardsp1 = []
    play = Gameboard(many,cardsp1)
    play.gameboard(many,cardsp1) #calling the gameboard function 
    Game(many,Points.pointsp1, Points.pointsp2, Gameboard.cardsp1).game() #calling the game function 

if __name__ == "__main__":
    main()
