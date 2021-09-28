#RPS v1 
#Player 1 vs Player 2
        
print("..Rock..")
print("..Paper..")
print("..Scissor..")
#taking input form both the players
p1 = input("Player 1 Chose: ").lower()
p2 = input("Player 2 Chose: ").lower()

#multiple elif to check who wins between the two players
if p1 == p2:
    print("Its a Tie!")
elif p1 == "rock" and p2 == "paper":
    print("Player 2 wins")
elif p1 == "rock" and p2 == "scissor":
    print("player 1 wins")
elif p1 == "paper" and p2 == "scissor":
    print("Player 2 wins")
elif p1 == "paper" and p2 == "rock":
    print("player 1 wins")
elif p1 == "scissor" and p2 == "rock":
    print("Player 2 wins")
elif p1 == "scissor" and p2 == "paper":
    print("player 1 wins")   
else:
    print("Somthing went wrong")
            