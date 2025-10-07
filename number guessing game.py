import random

def number_guessing_game():
    # Generate random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 1# You can change the number of attempts allowed

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number_to_guess:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    else:
        print(f"❌ Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()
