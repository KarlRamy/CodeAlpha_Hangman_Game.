import random

def hangman():
    words = ["BMW", "Mercedes", "Audi", "Porsche", "Lotus"]
    word = random.choice(words).upper()
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6

    print(" Welcome to the Hangman Game!")
    print(" Guess the car brand - You have 6 attempts.\n")

    while attempts > 0 and len(word_letters) > 0:
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_display))

        guess = input("Guess a letter: ").strip().upper()

        if not guess or not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter one letter only.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!\n")
        else:
            attempts -= 1
            print("Wrong guess!\n")

    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The correct word was: {word}")

if __name__ == "__main__":
    hangman()