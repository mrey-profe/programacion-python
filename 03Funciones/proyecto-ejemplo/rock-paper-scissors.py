import random

# Functions for the view

def user_play() -> str:
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input

def show_choices(user: str, computer: str) -> None:
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    
def show_winner(result: str) -> None:
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

def print_round_result(user_score: int, computer_score: int) -> None:
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
        
def print_final_winner(user_score: int, computer_score: int) -> None:
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner! Better luck next time.")
    else:
        print("The game ends in a tie!")
        
# Functions for the game logic        
        
def computer_play() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user: str, computer: str) -> str:
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
        (user == 'paper' and computer == 'rock') or \
        (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def update_score(result: str, user_score: int, computer_score: int) -> tuple[int, int]:
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1
    # Nothing to do for tie
    return user_score, computer_score

def play_round(user_score: int, computer_score: int) -> tuple[int, int]:
    user_choice = user_play()
    computer_choice = computer_play()
    show_choices(user_choice, computer_choice)
    
    while computer_choice == user_choice: # While there is a tie, replay
        print("It's a tie! Replay the round.")
        user_choice = user_play()
        computer_choice = computer_play()
        show_choices(user_choice, computer_choice)
    
    result = determine_winner(user_choice, computer_choice)
    show_winner(result)

    user_score, computer_score = update_score(result, user_score, computer_score)

    print_round_result(user_score, computer_score)
    
    return user_score, computer_score


# Main program

user_score = 0
computer_score = 0
rounds = 3

for round in range(rounds):
    print(f"Round {round + 1}:")
    user_score, computer_score = play_round(user_score, computer_score)

print_final_winner(user_score, computer_score)