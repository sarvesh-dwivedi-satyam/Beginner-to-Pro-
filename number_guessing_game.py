# Generate a random number
import random
number_to_guess = random.randint(1,100)
# Loop
while True:
    # Ask the user to make a guess
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        # If number < guess
        if guess < number_to_guess:
        # Print too low
            print("Too low!")
        # If number > guess
        elif guess > number_to_guess:
        # Print too high
            print("Too high!")
        # Else
        else:
        # Print well done
            print("Congratulations! You guessed the number.")
            break
        # if not a valid number
    except ValueError:
        # print an error
        print("Please enter a valid number")