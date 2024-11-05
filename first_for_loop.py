numbers =[1,2,3,4,5,6,7]
for number in numbers:
    print(number)
    
# create a question and answer game, where you try to guess a number between 1 to 10

import random

def guess_number_game():
    # Randomly choose a number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 10. You have 3 guesses.")

    # Loop through the number of attempts
    for attempt in range(1, attempts + 1):
        # Prompt the user for their guess
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        # Check if the guess is correct
        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")

        # If this is the last attempt and they haven't guessed correctly
        if attempt == attempts:
            print(f"Sorry, you've run out of guesses. The correct number was {number_to_guess}.")

# Run the game
guess_number_game()
