import random

def get_user_choice():
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        try:
            user_input = int(input("                           CHOOSE \n         1.Rock          2.Paper         3.Scissors \n\n         Enter the number to make a choice: "))
            if user_input in choices:
                return choices[user_input]
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"\nFinal scores:\nUser: {user_score}\nComputer: {computer_score}")

if __name__ == "__main__":
    main()