#RPS V5 - counting the score 

#importing the radint from random module
from random import randint
player_wins = 0
computer_wins = 0

#while lop will help us count he score and let the game run till the time someones wins
while player_wins<2 and computer_wins<2:
    print(f"Player_score = {player_wins}, Computer_score = {computer_wins}")
    print()
    
    #taking input from he player
    #storing the random number generated in variable r_num and defiening the move
    player = input("Enter your choice: ").lower()
    r_num = randint(0,2)
    if r_num == 0:
        computer = "rock"
    elif r_num == 1:
        computer = "paper"
    else:
        computer = "scissor"
        
    print(f"Computer plays: {computer}")  
    
    #nested if-else  to compare 
    if player == computer:
        print("it's a Tie")
    elif player == "rock":
        if computer == "scissor":
            player_wins +=1
            print("Player wins")
        else:
            computer_wins += 1
            print("Computer wins")
            
    elif player == "paper":
        if computer == "rock":
            player_wins +=1
            print("Player wins")
        else:
            computer_wins += 1
            print("Computer wins")
            
    elif player == "scissor":
        if computer == "paper":
            player_wins +=1
            print("Player wins")
        else:
            computer_wins += 1
            print("Computer wins") 
    else:
        print("please enter a valid choice")
#declaring the final score        
print(f"FINAL SCORE... Player: = {player_wins}, Computer: = {computer_wins}")        