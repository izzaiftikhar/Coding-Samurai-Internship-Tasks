# HANGMAN GAME PROJECT

# Welcome message
print("========================")
print("     HANGMAN GAME")
print("========================")

# Importing random
import random

# List of words
word_list = ['python', 'programming', 'variables', 'strings', 'range']

# Choose a random word
secret_word = random.choice(word_list)

# Store guessed letters
guessed_letters = []

# Count wrong guesses
wrong_guesses = 0
max_wrong = 6
print("Welcome to Hangman!")
print("The word has", len(secret_word), "letters.")

# Game loop
while wrong_guesses < max_wrong:

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter 
        else:
            display_word += "_"
    print("\nWord:", display_word)
    print("Remaining guesses:", max_wrong - wrong_guesses)

    # Check if player won
    if display_word == secret_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Take user's guess
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    # Save the guess
    guessed_letters.append(guess)

    # Check answer
    if guess in secret_word:
        print("Nice! This letter is in the word.")
    else:
        print("Oops! Try another letter.")
        wrong_guesses += 1

# Runs if player reaches 6 wrong guesses
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The word was:", secret_word)



