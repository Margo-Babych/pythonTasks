"""The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement."""

import random

print("Which number I guessed? ")
user = int(input("Choose a number from 1 to 10 and print here:"))
computer = random.randint(1, 10)
if user == computer:
    print("Yes, it is right answer.")
else:
    print("Try again")