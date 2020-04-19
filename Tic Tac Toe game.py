import random
player_names=['Mac','Jones','Roman','Marcus','Luther','Stephen','kevin','Alisha','Bobby','Natasha']
flag=True  #anonymous variable for main function's conditional loop.


print("""
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ |
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
                                                     
 """)



###########  Asking the players name and introduction to opponent.   ############
user_name=str(input('Please type out your name -->'))
opponent=random.choice(player_names)
print('Welcome '+user_name+' to the new version of the wounderful game. Let\'s start this......')
print('Introducing to you your opponent --> '+opponent)




############   Select your marker (X / O)?      ##############
player_marker=''
opponent_marker=['X','O']
while (player_marker!='X' and player_marker!='O'):
    player_marker=input("Please enter your marker (X/O)--> ")

opponent_marker.remove(player_marker)
print('Your marker is '+player_marker+' and '+opponent+'\'s marker is '+opponent_marker[0])




#############   The checkboard view of the tic tac toe game is built.    ###############
def check_board(board):
    print(f"""
            _        _  
           |/|      |/|
       {board[1]}   |/|  {board[2]}   |/|  {board[3]}  
     ______|/|______|/|______ 
    |______|/|______|/|______|
           |/|      |/|       
       {board[4]}   |/|  {board[5]}   |/|  {board[6]}    
     ______|/|______|/|______ 
    |______|/|______|/|______|
           |/|      |/|       
       {board[7]}   |/|  {board[8]}   |/|  {board[9]}   
           |/|      |/|      
    """)


print("Here is your Check Board")
values=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
check_board(values)




############  This function is gonna define which player is the winner.        ###############
def winner_check(sign,score,name,choi):
    winning_list=[[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    temp=winning_list
    global flag
    for ele in temp:
        a=0
        for element in ele:
            if(element in score):
                a+=1
            else:
                a=0
        if(a==3):
            print("GAME OVER\nThe winnner is "+name)
            flag=False
            break
        else:
            flag=True
            



        
#############  In this function the playing view of the player are defined.    ###############
def play_mode(picks,player,computer,mark,comp_mark):
    choices=[1,2,3,4,5,6,7,8,9]
    global flag
    player_turn=0
    player_score,computer_score=[],[]

    while(flag):
        ############   manual player turn    ############
        player_turn=int(input(player+' please enter your Choice Number -->'))    #Normal statement.
        while(int(player_turn)<1 or int(player_turn)>9):   #condition if the user enters number >9 or <1 and continues asking until value input is in between these two parameters.
            player_turn=int(input('Dear '+player+' you\'r out of range, please make another choice -->'))
        while(player_turn not in choices and player_turn in range(1,10)): #condition check whether the opted block is previously not chosen. 
            player_turn=int(input('Dear '+player+' the choice is previously chosen, please make another choice-->'))

        picks.pop(player_turn)             #Pops/Delets the index place holder ' ' to insert new element at that place. 
        picks.insert(player_turn,mark)        #Insert marker to the index position of picks list which the player has chosen.
        player_score.append(player_turn)      #justifies which blocks are filled by player marker.
        #print(picks)
        check_board(picks)
        winner_check(mark,player_score,player,choices)  #Checks whether the player is winner or not.
        
        if(flag==False):             #End of control
            break
        choices.remove(player_turn)          #Options that are chosen by the player will be removed from choices list
        



        ###############Random player or computers turn with random picks.  ##############
        if not choices:
            print("GAME OVER\nIts Draw")
            flag=False
            break
        opponent_turn=int(random.choice(choices))
        print(computer+" has chosen -->",opponent_turn)

        picks.pop(opponent_turn)                  #Pops/Delets the index place holder ' ' to insert new element at that place.
        picks.insert(opponent_turn,comp_mark)     #Insert marker to the index position of picks list which the player has chosen.
        computer_score.append(opponent_turn)       #Justifies which blocks are filled by computer marker.
        #print(picks)
        check_board(picks)
        winner_check(comp_mark,computer_score,computer,choices)  #Checks whether the computer is winner or not.
        if(flag==False):       #End of control
            break
        choices.remove(opponent_turn)             #Options that are chosen by the computer will be removed from choices list
        



#Main function call
play_mode(values,user_name,opponent,player_marker,opponent_marker[0])
