from classes import * 

if __name__=='__main__':
    print("Welcome to Coup! ")
    amount_of_players = int(input("Enter player amount :")) 
    dealer = Dealer(amount_of_players) #creating instance for Dealer 
    dealer.show_players()
    