#RPS V6 - counting the score 

#importing the radint from random module
from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

#the winning_score vairable make this code more flexible
while player_wins<winning_score and computer_wins<winning_score:
    print(f"Player_score = {player_wins}, Computer_score = {computer_wins}")
    print()
    
    #taking input from he player
    #if the player enter quit, the code will end
    #storing the random number generated in variable r_num and defiening the move
    player = input("Enter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    r_num = randint(0,2)
    if r_num == 0:
        computer = "rock"
    elif r_num == 1:
        computer = "paper"
    else:
        computer = "scissor"
        
    print(f"Computer plays: {computer}")  
    
    #nested if-else to compare
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

#declaring the winner
if player_wins > computer_wins:
    print("CONGRATS,You Win!!")
if player_wins == computer_wins:
    print("Its a Tie")
else:
    print("OH NO, The Computer won :( ")