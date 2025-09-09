# hangman.py
import random

WORDS = ["python", "developer", "hangman", "challenge", "keyboard", "computer", "program"]

def display_state(secret, guesses):
    display = "".join(c if c in guesses else "_" for c in secret)
    print("Word: ", " ".join(display))
    print("Guessed:", " ".join(sorted(guesses)))

def main():
    secret = random.choice(WORDS)
    guesses = set()
    wrong = 0
    max_wrong = 6
    print("Welcome to Hangman!")
    while True:
        display_state(secret, guesses)
        if all(c in guesses for c in secret):
            print("You won! The word was:", secret)
            break
        if wrong >= max_wrong:
            print("You lost! The word was:", secret)
            break
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
            continue
        if guess in guesses:
            print("Already guessed.")
            continue
        guesses.add(guess)
        if guess not in secret:
            wrong += 1
            print(f"Wrong! {max_wrong - wrong} guesses left.")
        else:
            print("Good!")

if __name__ == "__main__":
    main()
