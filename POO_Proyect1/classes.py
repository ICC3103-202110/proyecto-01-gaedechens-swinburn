

from abc import ABC,abstractmethod

class Hero(ABC):
    def __init__(self,hero_name,description):
        self.hero_name = hero_name
        self.description = description
    
    @abstractmethod
    def action(self):#abstract method because each character is going to have a different method
        pass
    
    @abstractmethod
    def counter_action(self):#abstract method because each character is going to have a different method
        pass
"""    
class Duke(Hero):
    def action(self,Dealer,player):
        
class Assasin(Hero):
    def action(self,Dealer,target_player,player):""" #something like this i think
        
class Player:
    def __init__(self,name,hero1,hero2):#builder of players
        self.name = name
        self.hero1 = hero1
        self.hero2 = hero2
        self.pocket_coins = draw_two()
    
    def get_name(self): #get name obviously
        return self.name

class Dealer:
    def __init__(self,player_amount): #the dealer is like our bank
        buffer_token = Token("coin")
        self.bag_coins = [buffer_token for i in range(0,50)] #creating all the coins of the game
        self.players = []#the list of the players
        for i in range(0,player_amount): #creating players
            player_buffer = Player(str(i+1),"hero1","hero2")
            self.players.append(player_buffer)

    def show_players(self): #this is to show all players
        print("Showing players! ")
        for i in self.players:
            print("Player "+i.get_name())

    def get_player_count(self): #counter of players
        return len(self.players)    

class Token: #the coin of the game
    def __init__(self,name):
        self.name = name
        
def draw_two():#this is to give the players 2 coins at the start of the game
    coins = []
    for i in range(0,2):
        buffer_token = Token("coin")
        coins.append(buffer_token)
        return coins
