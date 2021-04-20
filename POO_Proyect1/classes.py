

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

class Empty_hero(Hero): #hero empty, because we need it or the program goes down when None type wants to interact with methods
    def action(self):
        nada = ()
    def counter_action(self):
        nada = ()

class Duke(Hero):
    def action(self,Dealer,player):
        did_player_shown_duke = Dealer.check_for_bluff(player)
        #did_player_shown_duke = False means no one doubt it
        #did_player_shown_duke = True means SOMEONE DOUBT IT and he lost one card or doubt it succsseessffuuyllyy one doubt it
        if did_player_shown_duke == False:
            if len(Dealer.bag_coins) > 2:
                for i in range(0,3):
                    insert_one(Dealer,player)
                return True
        else:
            #TO DO
            #replase the hero duke of the player
            print("!replacing duke hero!")
            pass
        return False
        
    def counter_action(self,action_name):
        if action_name == 'Foreign Aid':
            return True
        return False

def anounce_death(target_player):
    print("\n    --ANOUNCMENT-- \n ")
    print("Player "+target_player.get_name() + " is out of the game !")
    print("\n        --EOA--\n")

class Assasin(Hero):
    def action(self,Dealer,target_player,player): #something like this i think
        empty_hero = Empty_hero("empty","no hay nadie aca")
        for i in range(0,3):
            player.pocket_coins.pop(0)    
        insert_three(Dealer)
        print("--other player chat---")
        print("Hello player "+target_player.get_name()+ "\n the player "+ player.get_name() + "  has killed a influence of yours, \n do you think it is a bluff? \n [1] Yes its a bluff \n [2] No its not a bluff")
        target_player_option = input("Response : ")
        if target_player_option == "1":
            if player.hero1.hero_name == 'Assasin' or player.hero2.hero_name == 'Assasin':
                target_player.hero1 = empty_hero
                target_player.hero2 = empty_hero
            else:
                player.get_rid_of_a_card()
        else:
            target_player.get_rid_of_a_card()      
        return True
    def counter_action(self,action_name):#MOMENTARY NEED CAHNGE!!!!!!
        if action_name == 'Foreign Aid':
            return True
        return False
class Player:
    def __init__(self,name,hero1,hero2):#builder of players
        self.name = name
        self.hero1 = hero1
        self.hero2 = hero2
        self.pocket_coins = ["coin","coin"]
    
    def lose_influence(self,number):
        empty_hero = Empty_hero("empty","no hay nadie aca")
        if number == "1":
            
            self.hero1 = empty_hero
        elif number == "2":
            self.hero2 = empty_hero

    def get_name(self): #get name obviously
        return self.name

    def get_rid_of_a_card(self):
        print("Hello player "+self.get_name())
        empty_hero = Empty_hero("empty","no hay nadie aca")
        if self.hero1.hero_name and self.hero2.hero_name:#####PROBLEM HERE 'NoneType' object has no attribute 'hero_name', #####
            print("Chose what influence to lose \n [1] "+str(self.hero1.hero_name)+" \n [2] "+str(self.hero2.hero_name))
            lose = input("Enter your influence number : ")
            self.lose_influence(lose)
        elif self.hero1.hero_name:
            print("Chose what influence to lose \n [1] "+str(self.hero1.hero_name))
            lose = input("Enter your influence number : ")
            self.hero1 = empty_hero
        elif self.hero2.hero_name:
            print("Chose what influence to lose \n [2] "+str(self.hero2.hero_name))
            lose = input("Enter your influence number : ")
            self.hero2 = empty_hero

    def show_options(self):
        print("Showing current status for player " + self.get_name())
        if self.hero1:
            print("Hero 1  ["+self.hero1.hero_name+"]")
        if self.hero2:
            print("Hero 2  ["+self.hero2.hero_name+"]") 
        print("Total coins in the BAAAGGG "+ str(len(self.pocket_coins)))

class Dealer:
    def __init__(self,player_amount): #the dealer is like our bank
        buffer_token = Token("coin")
        self.bag_coins = [buffer_token for i in range(0,50)] #creating all the coins of the game
        duke = Duke(hero_name='Duke',
                     description='1 duke')
        assasin = Assasin(hero_name='Assasin',
                     description='1 assasin')
                     #creating some heroes to try the game
        self.players = []#the list of the players
        for i in range(0,player_amount): #creating players
            player_buffer = Player(str(i+1),duke,assasin)
            self.players.append(player_buffer)

    def show_players(self): #this is to show all players
        print("Showing players! ")
        for i in self.players:#BEFORE THIS WE NEED TO INCLUDE ONLY THE PLAYERS THAT STILL ALIVE
            print("Player "+i.get_name())

    def get_player_count(self): #counter of players
        return len(self.players)  

    def check_for_bluff(self,player):
        did_player_shown_duke = False
        for player_buffer in self.players:
            if player_buffer != player:
                print("\n ----- \n Hello player "+player_buffer.get_name() + " \n do you think the player "+ player.get_name()+" is bluffing on that duke moove? \n [1] Yes is bluffing \n [2] No he is not bluffing")
                player_buffer_option = input("Insert option : ")
                if player_buffer_option == "1":
                    if player.hero1.hero_name == 'Duke' or player.hero2.hero_name == 'Duke':
                        did_player_shown_duke = True
                        player_buffer.get_rid_of_a_card()       
                    break
        return did_player_shown_duke

class Token: #the coin of the game
    def __init__(self,name):
        self.name = name

def insert_one(Dealer,player):
        player.pocket_coins.append('coin')
        Dealer.bag_coins.pop(0)
        
"""def draw_two():#this is to give the players 2 coins at the start of the game
    coins = []
    for i in range(0,2):
        buffer_token = Token("coin")
        coins.append(buffer_token)
        return coins
    for i in range(0,2):
        insert_one(Dealer,Player)
    return"""
def insert_three(Dealer): #paying the dealer 3 coins
    for i in range(0,3):
        buffer_token = Token("coin")
        Dealer.bag_coins.append(buffer_token)

