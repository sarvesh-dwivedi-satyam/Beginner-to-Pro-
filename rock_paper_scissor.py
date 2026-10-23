# Ask the user to make a choice
choices = ("r", "p", "s")
user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
if user_choice not in choices:
    print("Invalid Choice!")
# If choice is not valid
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not 
# Terminate