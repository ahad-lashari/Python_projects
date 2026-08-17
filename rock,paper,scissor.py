import random
def play_game():
    choices = ["rock", "paper", "scissors"]

    score_player = 0
    score_computer = 0

    print("==========================================")
    print("      ROCK, PAPER, SCISSORS GAME          ")
    print("==========================================")

    while True:
        user_choice = (
            input("\nEnter rock, paper, or scissors (or 'quit' to stop): ")
            .strip()
            .lower()
        )
        if user_choice == "quit":
            print("\nThanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid entry! Please type 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("Outcome: It's a tie!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("Outcome: You win this round!")
            score_player += 1
        else:
            print("Outcome: Computer wins this round!")
            score_computer += 1
        print(f"Score -> You: {score_player} | Computer: {score_computer}")

if __name__ == "__main__":
    play_game()