import random
from random import randint

print("Welcome to Rock Paper Scissors.")

#Randomization and Choice
turnList = ["rock", "paper", "scissors"]
computer = turnList[randint(0,2)]
player = str(input("Please select what do you want to play. Rock, paper, or scissors?"))

print("Your choice is", player)
print("Computer's choice is", computer)

#Tie
if player == computer:
    print("Tie! No one won, no one lost.")

#We Play Rock
elif player == "rock":
    if computer == "paper":
        print("You lost. Better luck next time!", computer, "defeats", player)
    elif computer == "scissors":
        print("You win! Congratulations.", player, "defeats", computer)

#We Play Paper
elif player == "paper":
    if computer == "scissor":
        print("You lost. Better luck next time!", computer, "defeats", player)
    elif computer == "rock":
        print("You win! Congratulations!", player, "defeats", computer)

#We Play Scissors
elif player == "scissor":
    if computer == "rock":
        print("You lost. Better luck next time!", computer, "defeats", player)
    elif computer == "paper":
        print ("You win! Congratulations!", computer, "defeats", player)

else:
    ("Invalid input. Try again and check your spelling.")

print("Thank you for playing Rock Paper Scissors")