from abc import ABC,abstractmethod
import random
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
        pass
    def counter_action(self):
        pass

class Contessa(Hero):
    def action(self,Dealer,player):
        pass
       
    def counter_action(self,action_name):
        pass

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
           
            #replase the hero duke of the player
            if player.hero1.hero_name == "Duke":
                Dealer.change_first_card(player)
            elif player.hero2.hero_name == "Duke":
                Dealer.change_second_card(player)
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

class Ambassador(Hero):
    def action(self,dealer,player):
        if player.hero1.hero_name != "empty" and player.hero2.hero_name != "empty":
            if player.hero1.hero_name == 'Ambassador' or player.hero2.hero_name == 'Ambassador':
                print ("Changing your both cards")
                Dealer.change_both_cards(dealer,player)

            else:
                print("You dont have the Ambassador hero")
        elif player.hero1.hero_name != "empty" and player.hero2.hero_name == "empty":
            if player.hero1.hero_name == 'Ambassador':
                print("Changing hero 1" )
                Dealer.change_first_card(dealer,player)
            else:
                print("You dont have the Ambassador hero")
                

        elif player.hero2.hero_name != "empty" and player.hero1.hero_name == "empty":
            if player.hero2.hero_name == 'Ambassador':
                print("Changing hero 2" )
                Dealer.change_second_card(dealer,player)
            
            else:
                print("You dont have the Ambassador hero")
                
            
        


    def counter_action(self,action_name):
        pass

class Captain(Hero):
    def action(self,dealer,player):
        print("Pick a Target player")
        for i in dealer.players:
            if i.get_name() != player.get_name():
                print(i.get_name())
        while True:
            opt = input("insert player option : ")
            if len(dealer.players) < int(opt):
                print("invalid returning...")
            else:
                print("Starting steal move!")
                self.doubt_captain(dealer,player,dealer.players[int(opt)-1])
                break        
    def counter_action(self,action_name):
        pass
   
    def doubt_captain(self,dealer,player,target_player):
        didnt_got_blocked = True
        for i in dealer.players: #COUNTERACTION 
            if i.get_name() != player.get_name():
                if i.get_name() != target_player.get_name():
                    while True:
                        print("\n Hello player "+i.get_name()+ " would you block the player " + player.get_name() + " of his Captain moove ? \n [1] Yes block it \n [2] No , let it pass \n ")
                        option = input("Insert option : ")
                        if option == "1":
                            print("\n Hello player "+ player.get_name()+ " the player  " + i.get_name()+ " has blocked your moove, do you thinks he is bluffing ? \n [1] Yes he is bluffing \n [2] No he is not bluffing ")
                            player_option = input("Insert option : ")
                            if player_option == "1" :
                                if i.hero1.hero_name == 'Captain' or i.hero2.hero_name == 'Captain':
                                    print("Ooops you didnt guess it correctly and you got blocked ...")
                                    player.get_rid_of_a_card()
                                    didnt_got_blocked = False
                                    if i.hero1.hero_name == "Captain":
                                        dealer.change_first_card(i)
                                    elif i.hero2.hero_name == "Captain":
                                        dealer.change_second_card(i)
                                    print("!replacing captain hero!")
                                    break
                                else:
                                    print("You doubted correctly, that player didnt had a captain!")
                                    i.get_rid_of_a_card()
                                    break
                            if player_option == "2" :
                                didnt_got_blocked = False#he got blocked and didnt doubt it
                                break
                        elif option == "2":
                            break
                        else:
                            print("Invalid option returning...")
                                           
        for i in dealer.players: #DOUBT OPTION FOR TARGET PLAYER
            if i.get_name() != player.get_name():
                if i.get_name() == target_player.get_name():
                    while True:
                        print("\n Hello player "+i.get_name()+ " would you doubt the player " + player.get_name() + " of his Captain moove against YOU ? \n [1] Yes its a bluff \n [2] No its not a bluff \n")
                        option = input("Insert option : ")
                        if option == "1":
                            if player.hero1.hero_name == "Captain" or player.hero2.hero_name == "Captain":
                                print("\n OOps Your bluff went wrong")
                                if player.hero1.hero_name == "Captain":
                                    dealer.change_first_card(player)
                                elif player.hero2.hero_name == "Captain":
                                    dealer.change_second_card(player)
                                print("!replacing captain hero!")
                                i.get_rid_of_a_card()
                                break  
                            else:
                                print("Doubted correctly the player didnt had the captain! ")
                                player.get_rid_of_a_card()
                                break
                        elif option == "2":
                            if didnt_got_blocked:    
                                try:
                                    i.pocket_coins.pop(0)
                                    player.pocket_coins.append("coin")
                                    i.pocket_coins.pop(0)
                                    player.pocket_coins.append("coin")
                                    print("steal completed!")
                                    break
                                except Exception:
                                    print("Target player didnt had enough coins for the whole steal !")
                                    print("steal completed!")
                                    break
                            else:
                                print("you got blocked from your steal move! better luck next time ")
                                break
                        else:
                            print("Invalid option returning...")


class Assasin(Hero):
    def action(self,Dealer,target_player,player):
        empty_hero = Empty_hero("empty","no hay nadie aca")
        for i in range(0,3):
            player.pocket_coins.pop(0)    
        insert_three(Dealer)
        print("--other player chat---")
        print("Hello player "+target_player.get_name()+ "\n the player "+ player.get_name() + "  has killed a influence of yours, \n do you think it is a bluff? \n [1] Yes its a bluff \n [2] No its not a bluff \n [3] Bloc with Contessa")
        target_player_option = input("Response : ")
        if target_player_option == "1":
            if player.hero1.hero_name == 'Assasin' or player.hero2.hero_name == 'Assasin':
                if player.hero1.hero_name == "Assasin":
                    Dealer.change_first_card(player)
                elif player.hero2.hero_name == "Assasin":
                    Dealer.change_second_card(player)
                print("!replacing assasin hero!")
                target_player.hero1 = empty_hero
                target_player.hero2 = empty_hero
            else:
                player.get_rid_of_a_card()

        elif target_player_option == "3": #blocked with contessa
                while True:
                    print("Hello player "+player.get_name()+ "\n the player "+ target_player.get_name() + "  Blocked your assasinationn with a Contessa, \n Do you think its a bluff ? \n [1] Yes, its a bluff \n [2] No, He is not bluffing")
                    player_input_against_contessmove = input("Insert option : ")
                    if player_input_against_contessmove == "1":
                        if player.hero1.hero_name == 'Contessa' or player.hero2.hero_name == 'Contessa':
                            player.get_rid_of_a_card()
                        else:
                            try:
                                target_player.get_rid_of_a_card()
                                target_player.get_rid_of_a_card()
                                print("You bluffed wrong, you got assasinated and you loose one cuz of your BLUFFING skills")
                                return False
                                break
                            except Exception:
                                print("You bluffed wrong, you got assasinated and you loose one cuz of your BLUFFING skills")
                                break
                
                    else:
                        print("Assesintaion retrieved unsuccessfully")
                        return False
                     
                    break
        else:
            target_player.get_rid_of_a_card()      
        return True
    def counter_action(self,action_name):#MOMENTARY NEED CHANGE!!!!!!
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
        contess = Contessa(hero_name='Contessa', description='1 contessa')
        captain = Captain(hero_name='Captain', description= '1 captain')
        ambassador = Ambassador(hero_name= "Ambassador", description="1 ambassador")
        capp = [captain for i in range(0,3)]
        cont = [contess for i in range(0,3)]
        assa = [assasin for i in range(0,3)]
        duk = [duke for i in range(0,3)]
        amb = [ambassador for i in range(0,3)]
        self.deck = cont+ assa + duk + capp + amb #deck of cards
        random.shuffle(self.deck)
    
        self.players = []#the list of the players
        for i in range(0,player_amount): #creating players
            first_hero_buffer = self.deck.pop(0)
            random.shuffle(self.deck)
            second_hero_buffer = self.deck.pop(0)
            random.shuffle(self.deck)
            player_buffer = Player(str(i+1),first_hero_buffer,second_hero_buffer)
            self.players.append(player_buffer)

    bag_of_coins = ["coin" for i in range(0,50)] #this is going to be the bank of coins of the game

    def change_both_cards(self,player): #this changes both cards of a player
        self.deck.append(player.hero1)
        self.deck.append(player.hero2)
        random.shuffle(self.deck)
        player.hero1 = self.deck.pop(0)
        player.hero2 = self.deck.pop(0)

    def change_first_card(self,player): #this change hero1 of the player
        self.deck.append(player.hero1)
        random.shuffle(self.deck)
        player.hero1 = self.deck.pop(0)

    def change_second_card(self,player): #this change hero2 of the player
        self.deck.append(player.hero2)
        random.shuffle(self.deck)
        player.hero2 = self.deck.pop(0)



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

    def coup(self,player):
        if len(player.pocket_coins) >= 7:
            print("What player should loose an influence? \n ")
            for i in self.players:
                if i.get_name() != player.get_name():
                    print("Player "+i.get_name())
            while True:
                coup_option  = input("Insert player : ")
                for i in self.players:
                    if i.get_name() != player.get_name():
                        if coup_option == i.get_name():
                            #selected valid target
                            i.get_rid_of_a_card()
                            print("Coup retrieved successfully")
                            return True
                print("Incorret player option try again ... \n ")
            return False

def insert_one(Dealer,player):#this function is to give a player one coin and at the same time subtract one coin from the dealers bag
        player.pocket_coins.append('coin')
        Dealer.bag_of_coins.pop(0)
        

def insert_three(Dealer): #paying the dealer 3 coins
    for i in range(0,3):
        Dealer.bag_of_coins.append('coin')

