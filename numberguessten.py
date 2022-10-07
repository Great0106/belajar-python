import random
from random import randint

print("Welcome to Guess the Number. Your objectivve is to guess the computer's number.")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
guess = numbers[randint(0, 10)]
player = str(input("Insert the number you would like to guess. Ranging from 1 to 10."))

# print(guess) -- to test

if player == guess:
    print("Congratulations! The number both you and the computer guessed was "+guess+". Thank you for playing this game!")
elif player >= guess:
    print("Wrong answer, your guess is too high.")
elif player < guess:
    print("Wrong answer, your guess is too low.")
else:
    print("Invalid input.")
