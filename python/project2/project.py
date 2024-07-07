''' we are going to write a program that generates a random number and asks the user to guess it. if the player's guess is higher than actual number. the program display "lower number please" similarly, if the user's guess is too low, the program displays the number of guess the player used to arrive at the number.
hint: use the random module'''
import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)
a = -1
guess = 0

while a != n:
    guess += 1
    a = int(input("Guess the number: "))
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"Congratulations! You've guessed the number {n} correctly in {guess} attempts.")
