import random

# Define the choices and rules of the game
choices = ['rock', 'paper', 'scissors']
rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# Play the game
while True:
    # Get user input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Check if the user input is valid
    if user_choice not in choices:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue

    # Generate computer choice
    computer_choice = random.choice(choices)

    # Determine the winner (or if it's a tie)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif rules[user_choice] == computer_choice:
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display the result
    print(f"You chose {user_choice}, computer chose {computer_choice}. {result}")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        continue
    else:
        break
