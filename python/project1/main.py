import random

# Mapping choices to numbers
choices = {"rock": 1, "paper": -1, "scissors": 0}

# Getting user input
youstr = input("Enter your choice (rock, paper, or scissors): ").lower()
if youstr not in choices:
    print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")
else:
    you = choices[youstr]

    # Randomly generate computer's choice
    computer = random.choice(list(choices.values()))

    # Determining and displaying the choices
    computer_choice = [k for k, v in choices.items() if v == computer][0]
    print(f"Computer chose {computer_choice}.")

    # Determine the winner
    if computer == you:
        print("It's a tie!")
    elif (computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
        print("You lose!")
    else:
        print("You won!")
