#RPS V3 - Computer vs Player

#random module to get randomly generated number between 0-2(inculsive)
#storing it in a variable r_num 
# and taking input formt he user
from random import randint
player = input("Player make your move: ")
rand_num = randint(0,2)

#defineing computer moves based on the randim number generated
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
    