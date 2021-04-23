

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
            if len(Dealer.bag_of_coins) > 2:
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
        if self.hero1.hero_name and self.hero2.hero_name:
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
        duke = Duke(hero_name='Duke',
                     description='1 duke')
        assasin = Assasin(hero_name='Assasin',
                     description='1 assasin')
                     #creating some heroes to try the game
        self.players = []#the list of the players
        for i in range(0,player_amount): #creating players
            player_buffer = Player(str(i+1),duke,assasin)
            self.players.append(player_buffer)

    #buffer_token = Token("coin")
    bag_of_coins = ["coin" for i in range(0,50)] #this is going to be the bank of coins of the game

    def show_players(self): #this is to show all players
        print("Showing players! ")
        for i in self.players:#BEFORE THIS WE NEED TO INCLUDE ONLY THE PLAYERS THAT STILL ALIVE
            print("Player "+i.get_name())

    def get_player_count(self): #counter of players
        return len(self.players)  

    def check_for_bluff(self,player):#checking the bluff for the duke hero.... WE NEED TO CHANGE THE NAME OF THE FUNCION PLZ......
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

    def check_for_counteraction_option_foreign_aid(self,player):
        did_player_shown_duke = False
        someone_dooubt_it = True
        someone_counter_it_successfully = False
        for player_buffer in self.players:
            if player_buffer.get_name != player.get_name:
                print("\n ----- \n Hello player "+player_buffer.get_name() + " \n would you like to counter attack "+ player.get_name()+" on that Foreign Aid move? \n [1] Yes block it \n [2] No dont block it")
                player_buffer_option = str(input("Insert option : "))
                if player_buffer_option == "1":
                    someone_dooubt_it = True
                    someone_counter_it_successfully = self.foreign_aid_counteraction(player,player_buffer)
                    break
                else:
                    pass
        if someone_counter_it_successfully:
            pass
        else:
            player.pocket_coins.append("coin")
            player.pocket_coins.append("coin")
            print("-----\n Foreign Aid Successfully retrived! \n \n ")
           
        return did_player_shown_duke
            
        
    def foreign_aid_counteraction(self,player,player_buffer):
        # player ----> traying to do a foreing aid
        # player_buffer -----> traying to stop that player
        print("\n ----- \n Hello player "+player.get_name()+ ', the Player '+player_buffer.get_name()+ 'has counter your foreign Aid , Do oyou belive he is bluffing the Duke?' +' \n [1] Yes is bluffing \n [2] No he is not bluffing"' )
        player_option = str(input("Insert option : "))
        did_player_show_duke = False
        if player_option == "1":
            if player_buffer.hero1.hero_name == 'Duke' or player_buffer.hero2.hero_name == 'Duke':
                did_player_show_duke = True
                print("\n OOps you doubted wrong, the player "+ player_buffer.get_name() + " had the Duke, now get rid of a card ! \n")
                player.get_rid_of_a_card()      
                #draw one hero
            elif player_buffer.hero1.hero_name != 'Duke' and player_buffer.hero2.hero_name != 'Duke':
                did_player_show_duke = False
                player_buffer.get_rid_of_a_card()
                #draw one hero
            # analize the results of the past interaciton
            if did_player_show_duke:
                return True
            else:
                return False    
        else:
            print("Someone blocked your action, so you dont get the 2 coins of Foreign Aid")
            return True
            player.pocket_coins.pop(0)
            player.pocket_coins.pop(0)
"""
    def insert_one(self,player):#this function is to give a player one coin and at the same time subtract one coin from the dealers bag
        player.pocket_coins.append('coin')
        Dealer.bag_of_coins.pop(0)"""

"""def foreign_aid_counteraction(player):
    
    for player_buffer in self.players:
            if player_buffer == player:
                print("\n ----- \n Hello player "+player.get_name()+ ','+player_buffer.get_name()+ 'has counter attacked you, how would you like to respond' +' \n [1] Yes is bluffing \n [2] No he is not bluffing"' )
                player_buffer_option = str(input("Insert option : "))
                if player_buffer_option == "1":
                    if player_buffer.hero1.hero_name == 'Duke' or player_buffer.hero2.hero_name == 'Duke':
                        
                        player.get_rid_of_a_card()      
                        break
                   
                    if player_buffer.hero1.hero_name != 'Duke' and player_buffer.hero2.hero_name != 'Duke':
                        
                        player_buffer.get_rid_of_a_card()
                        break
                else:
                    print("Someone blocked your action, so you dont get the 2 coins of Foreign Aid")
                    player.pocket_coins.pop(0)
                    player.pocket_coins.pop(0)"""



class Token: #the coin of the game
    def __init__(self,name):
        self.name = name

def insert_one(Dealer,player):#this function is to give a player one coin and at the same time subtract one coin from the dealers bag
        player.pocket_coins.append('coin')
        Dealer.bag_of_coins.pop(0)
        

def insert_three(Dealer): #paying the dealer 3 coins
    for i in range(0,3):
        Dealer.bag_of_coins.append('coin')

