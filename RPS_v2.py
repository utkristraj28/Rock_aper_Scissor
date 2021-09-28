#RPS V2
#PLayer1 vs Player2

print("..Rock..")
print("..Paper..")
print("..Scissor..")
#Taking input ftom both the players
p1 = input("Player 1 Chose: ").lower()
p2 = input("Player 2 Chose: ").lower()

#nested if-else for better understandability
if p1 == p2:
    print("Draw")
elif p1 == "rock":
    if p2 == "paper":
        print("Player 2 wins")
    elif p2 == "scissor":
        print("Player 1 wins")
elif p1 == "paper":
    if p2 == "scissor":
        print("Player 2 wins")
    elif p2 == "rock":
        print("Player 1 wins") 
elif p1 == "scissor":
    if p2 == "rock":
        print("Player 2 wins")
    elif p2 == "paper":
        print("Player 1 wins")        