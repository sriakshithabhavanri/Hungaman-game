import random

# List of words with corresponding hints (riddles)
words_with_hints = [
    ("bicycle", "I have two wheels and you can pedal me to move fast."),
    ("pyramid", "I am an ancient structure with a square base and triangular sides."),
    ("kangaroo", "I am an Australian animal that jumps and has a pouch."),
    ("volcano", "I can erupt with lava and ash, and I am a type of mountain."),
    ("octopus", "I live in the sea and have eight arms."),
    ("balloon", "I am filled with air and often used in parties for decoration."),
    ("guitar", "I have strings and you can play music with me."),
    ("puzzle", "I can be a game or a problem that requires ingenuity to solve."),
    ("library", "A place where you can borrow books."),
    ("astronaut", "I travel to space and explore beyond Earth."),
    ("chocolate", "I am a sweet treat made from cocoa beans."),
    ("ballet", "I am a form of dance that requires grace and technique."),
    ("umbrella", "I protect you from the rain."),
    ("whisper", "I am a way of speaking very softly."),
    ("notebook", "You use me to write notes and keep track of things.")
]

# Choose a random word and its hint from the list
word, hint = random.choice(words_with_hints)

# Create a list to store the guessed letters
guessed_letters = []

# Create a list to store the word with underscores
word_with_underscores = ["_"] * len(word)

# Set the number of attempts
attempts = 6

print("Welcome to Hangman!")
print("You have", attempts, "attempts to guess the word.")

while attempts > 0:
    # Print the word with underscores
    print(" ".join(word_with_underscores))

    # Ask the user to guess a letter or request a hint
    user_input = input("Guess a letter or type 'hint' for a hint: ").lower()

    if user_input == 'hint':
        print("Hint:", hint)
        continue

    # Check if the letter has already been guessed
    if user_input in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(user_input)

    # Check if the letter is in the word
    if user_input in word:
        # Fill in the corresponding underscores
        for i in range(len(word)):
            if word[i] == user_input:
                word_with_underscores[i] = user_input
    else:
        # Draw a part of the gallows
        attempts -= 1
        print("Incorrect! You have", attempts, "attempts left.")

    # Check if the word has been fully guessed
    if "_" not in word_with_underscores:
        print("Congratulations! You guessed the word:", word)
        break

if attempts == 0:
    print("Sorry, you didn't guess the word. The word was:", word)