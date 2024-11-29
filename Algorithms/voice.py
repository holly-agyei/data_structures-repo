secret_word = "elephant"

def get_guess():
    guess = input("Guess: ")
    if not guess.islower():
        print("Your guess must be a lowercase letter!")
    elif len(guess) != 1:
        print("Your guess must have exactly one character!")
    else:
        return guess
    return None

def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

dashes = "-" * len(secret_word)  # Create dashes equal to the length of the secret word
guesses_left = 10  # Number of incorrect guesses allowed

print(dashes)

while "-" in dashes and guesses_left > 0:  # Loop while user hasn't guessed the word and still has guesses
    print(f"{guesses_left} incorrect guesses left.")  # Print remaining guesses
    guess = None
    while guess is None:  # Ensure valid guess
        guess = get_guess()
    
    if guess in secret_word:
        print("That letter is in the word!")
        dashes = update_dashes(secret_word, dashes, guess)
    else:
        print("That letter is not in the word.")
        guesses_left -= 1  # Decrease guesses left for incorrect guess
    
    print(dashes)  # Display the updated dashes after each guess

# Check if the user won or lost
if "-" not in dashes:
    print(f"Congrats! You win. The word was: {secret_word}")
else:
    print(f"You lose. The word was: {secret_word}")
