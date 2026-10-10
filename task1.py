
import random

# List of predefined words
words = ["python", "apple", "computer", "student", "network"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
else:
    print("\nGame Over! The word was:", word)

