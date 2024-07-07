# The game()function in a program lets a user play a game and returns the score as an integer. You need to write a program to update the Hi-score whenever the game( ) functin break the Hi-score.
def game():
    
    return int(input("Enter your score: "))

def read_high_score(file_path):
    try:
        with open(file_path, "r") as file:
            high_score = int(file.read())
            return high_score
    except FileNotFoundError:
        return 0

def write_high_score(file_path, high_score):
    with open(file_path, "w") as file:
        file.write(str(high_score))

def main():
    file_path = "high_score.txt"
    
    # Read the current high score
    high_score = read_high_score(file_path)
    print(f"Current High Score: {high_score}")
    
    # Get the new score from the game function
    new_score = game()
    print(f"Your Score: {new_score}")
    
    # Update the high score if the new score is higher
    if new_score > high_score:
        print("Congratulations! You have a new high score.")
        write_high_score(file_path, new_score)
    else:
        print("Try again to beat the high score.")

if __name__ == "__main__":
    main()
