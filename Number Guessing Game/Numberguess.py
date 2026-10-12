# Number Guessing Game Project

# Import Random Module
import random 

# Display Welcome Message
print("Welcome to Number Guessing Game!")

# Tell the player the nukber range
print("I'm thinking of a number between 1 and 100")

# Generate a random secret number
secret_number = random.randint(1, 100)

# Start attempt counter at 0
attempts = 0

# Set maximum number of attempts 
max_attempts = 8

# Keep the game running while attempts remain
while attempts < max_attempts :

    # Get the player's guess
    guess = int(input("Enter a number:"))

    # Increase the attempt counter 
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    
    # Checking if guess is too high 
    elif guess > secret_number:
        print("Too high!")

    # Checking if guess is too low
    else:
        print("Too low!")

    # Giving the player a rating
    if attempts <= 3:
        print("Excellent! You're a great guesser!")
    
    elif attempts <= 5:
        print("Good job!")
    
    else:
        print("You made it")

    # Give a hint if the guess is very close
    difference = abs(secret_number - guess)

    if difference <= 5:
        print("You're very close!")

# Show remaining attempts
remaining = max_attempts - attempts
print(f"Attempts remaining: {remaining}")
print()

# Display Game Over Message
if attempts == max_attempts and guess != secret_number:
    print("\nGame Over!")
    print(f"The number was {secret_number}.")

