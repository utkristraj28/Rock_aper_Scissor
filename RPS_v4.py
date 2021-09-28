#RPS V4 - Computer vs Player ;Playing 3 times

#Randint will generate random number between 0-2(inculsive)
from random import randint
#for loop will let the game run three times
#takin input from the user
#strong random number 0-3 in r_num
for times in range(3):
    player = input("Player make your move: ")
    rand_num = randint(0,2)
    
    #defineing computer moves based on the random number generated
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissor"
    
    print(f"Computer plays {computer}")
    
    #nested if-else to compare
    if player==computer:
        print("Its a tie")
    
    elif player == "rock":
        if computer == "paper":
            print("computer wins")
        else:
            print("player wins")
        
    elif player == "paper":
        if computer == "scissor":
            print("computer wins")
        else:
            print("player wins")  
        
    elif player == "scissor":
        if computer == "rock":
            print("computer wins")
        else:
            print("player wins") 
        
    else:
        print(f"{player} enter a valid entry")
    