
import random

words = ["python", "computer", "coding", "program", "developer"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("_ " * len(word))

while incorrect_guesses < max_attempts:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Attempts left:", max_attempts - incorrect_guesses)

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break
else:
    print("Game over! The word was:", word)
