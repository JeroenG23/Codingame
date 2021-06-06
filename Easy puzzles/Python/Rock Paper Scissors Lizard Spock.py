import sys
import math

n = int(input())
Competitor_list=[]
for i in range(n):
    numplayer, signplayer = input().split()
    #Competitor_list = int(inputs[0])
    #signplayer = inputs[1]
    Help_list=[int(numplayer), signplayer]
    Competitor_list.append(Help_list)

Tournament_rounds=1
Competitors=n
while Competitors !=2:
    Tournament_rounds+=1
    Competitors=Competitors/2
    
Winner=0
Loser=0
def Match_winner(Sign_player_1, Sign_player_2,Num_player_1,Num_player_2,Winner,Loser):
    if Sign_player_1==Sign_player_2 and Num_player_1<Num_player_2:
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='C'and Sign_player_2=="P":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='P'and Sign_player_2=="R":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='R'and Sign_player_2=="L":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='L'and Sign_player_2=="S":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='S'and Sign_player_2=="C":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='C'and Sign_player_2=="L":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='L'and Sign_player_2=="P":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='P'and Sign_player_2=="S":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='S'and Sign_player_2=="R":
        Winner = Num_player_1
        Loser = Num_player_2  
    elif Sign_player_1=='R'and Sign_player_2=="C":
        Winner = Num_player_1
        Loser = Num_player_2  
    else:
        Winner = Num_player_2
        Loser = Num_player_1
    return Winner, Loser

i=0
Tournament_list = Competitor_list
Loser_list=[]
for j in range(Tournament_rounds):
    while i<(len(Tournament_list)-1):
        Winner, Loser = Match_winner(Tournament_list[i][1],Tournament_list[i+1][1],Tournament_list[i][0],Tournament_list[i+1][0],Winner, Loser)
        if Winner == Tournament_list[i][0]:
            Help_list=[]
            Help_list = Tournament_list[i]
            Help_list.append(Loser)
            Loser_list.append(Tournament_list[i+1])
        elif Winner == Tournament_list[i+1][0]:
            Help_list=[]
            Help_list = Tournament_list[i+1]
            Help_list.append(Loser)
            Loser_list.append(Tournament_list[i])
        i+=2
    for i in range( len(Loser_list)):
        Tournament_list.remove(Loser_list[i])
    Loser_list.clear()
    i=0
    
print(Tournament_list[0][0])
Losers=""
for i in range(len(Tournament_list[0][2:])):
    Losers = Losers + " "+ str(Tournament_list[0][2+i])
print(Losers.lstrip())
