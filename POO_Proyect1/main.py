

from abc import ABC,abstractmethod

class Hero(ABC):
    def __init__(self,hero_name,description):
        self.hero_name = hero_name
        self.description = description
    
    @abstractmethod
    def action(self):
        pass
    
    @abstractmethod
    def counter_action(self):
        pass
    
class Duke(Hero):
    def action(self,Dealer,player):
        
class Assasin(Hero):
    def action(self,Dealer,target_player,player):
        
class Player:
    def __init__(self,name,hero1,hero2):
        self.name = name
        self.hero1 = hero1
        self.hero2 = hero2
        self.pocket_coins = draw_two()
        
class Dealer:
    def __init__(self,player_amount):
        buffer_token = Token("coin")
        self.bag_coins = [buffer_token for i in range(0,50)]
        
class Token:
    def __init__(self,name):
        self.name = name
        
def draw_two():
coins = []
for i in range(0,2):
    buffer_token = Token("coin")
    coins.append(buffer_token)
    return coins
