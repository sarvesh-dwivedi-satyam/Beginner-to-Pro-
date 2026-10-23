import random

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
# Ask the user to make a choice
choices = ("r", "p", "s")
while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(choices)

    # Print choices (emojis)
    print(f"You Chose {emojis[user_choice]}")
    print(f"Computer Chose {emojis[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else:
        print("You lose")

    # Ask the user if they want to continue
    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break
# If not 
# Terminate
