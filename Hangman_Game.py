import random

# Predefined list of words
words = ["python", "hangman", "coding", "program", "random"]

# Randomly choose a word
word_to_guess = random.choice(words)

# Create a list to display guessed letters and underscores
hidden_word = ["_" for _ in word_to_guess]

# Track guessed letters and attempts
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("\nWelcome to Hangman!")

# Main game loop
while incorrect_guesses < max_incorrect and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                hidden_word[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses += 1

# End of game results
if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game Over! The word was:", word_to_guess)
