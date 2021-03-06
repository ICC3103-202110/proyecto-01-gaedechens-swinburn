from classes import * 

def showturn(player_phase):
    print("--------")
    print("Turn of player "+ str(player_phase+1))

def show_and_get_option(dealer):
    posibles = [str(i) for i in range(1,8)]
    while(True):
        print("Options \n [1] Income \n [2] Foreign Aid \n [3] Coup \n [4] Tax (Duke required) \n [5] Assassinate *3 coins* (assasin required)\n [6] Exchange (Ambassador required) \n [7] Steal (captain required)")
        opcion = input("Option : ")
        if opcion in posibles:
            return opcion
        else:
            print("Invalid option...")



if __name__=='__main__':
    print("Welcome to Coup! ")
    amount_of_players = int(input("Enter player amount :")) 
    dealer = Dealer(amount_of_players) #creating instance for Dealer 
    dealer.show_players()
    phase_counter = 0
    log= []
    while True:
        #current player
        player_phase = phase_counter%amount_of_players
        
        if dealer.players[player_phase].hero1.hero_name != "empty" or dealer.players[player_phase].hero2.hero_name != "empty": 
            showturn(player_phase)
            for i in log:
                print(i)
            #actual turn
            print(dealer.players[player_phase].get_name())
            dealer.players[player_phase].show_options()
            
            #Current player ----> dealer.players[player_phase]
            current_player = dealer.players[player_phase]
            if dealer.players[player_phase].get_name() == "1": #"reseting" the log when the round its over
                log = []

            #option choosing part
            opcion = show_and_get_option(dealer)
            
            #CREATING THE LOG
            if opcion =="1":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Income")
                    log.append(text)
            elif opcion =="2":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Foreign Aid")
                    log.append(text)
            elif opcion =="3":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Coup")
                    log.append(text)
            elif opcion =="4":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Tax")
                    log.append(text)
            elif opcion =="5":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Assassinate")
                    log.append(text)
            elif opcion =="6":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Exchange")
                    log.append(text)
            elif opcion =="7":
                    text = ("Player"+str(dealer.players[player_phase].get_name()) + " did the action Steal")
                    log.append(text)
            #END OF CREATING THE LOG

            if opcion == "1":
                insert_one(Dealer,dealer.players[player_phase])
           
                print("1 coin has been added to the bag")

            elif opcion == "2":
                dealer.check_for_counteraction_option_foreign_aid(dealer.players[player_phase])

            elif opcion == "3":
                if dealer.coup(dealer.players[player_phase]):
                    for i in range(0,7):
                        dealer.players[player_phase].pocket_coins.pop(0)
            
            elif opcion == "4":
                duke_buffer = Duke("duke","1 duke")
                duke_buffer.action(dealer,dealer.players[player_phase])
           
            elif opcion == "5":
                
                #assasination menu
                while True:
                    print("Posible targets bellow")
                    dealer.show_players()
                    target_option = input("Select player ")
                    if int(target_option) <= (dealer.get_player_count()):
                        assasin_buffer = Assasin("assasin","1 assasin")
                        assasin_buffer.action(dealer,dealer.players[int(target_option)-1],dealer.players[player_phase])
                        break
                    else:
                        print("Incorect player election... returning")

            elif opcion == "6":
                ambassador_buffer = Ambassador("Ambassador","1 ambassador")
                ambassador_buffer.action(dealer,dealer.players[player_phase])

            elif opcion == "7":
                captain_buffer = Captain("captain","1 captain")
                captain_buffer.action(dealer,dealer.players[player_phase])

        #EndOfTurn
        still = []
        for i in dealer.players:
            if i.hero1.hero_name != "empty" or i.hero2.hero_name != "empty":
                still.append(i)
        if len(still) == 1:
            print("Se acabo y gano el jugador "+ str(player_phase+1))
            break
        phase_counter +=1
    
print("Thanks for playing")
