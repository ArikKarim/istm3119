# sufficiently bored to do a Wellesley CS111 assignment just for funzies

import random # will be used to play a game with a random word

INTRO = """\
Welcome to guess-that-word!
You will guess what the word could be and we will reveal which letters
of your guess are correct. If a letter is in the word but in a different
location, we'll let you know.

'@' means this letter is correct.
'*' means this letter is present in a different spot.
'-' means this letter is not present.

Use the hints to guess the word!
"""

def letterHints(secret, guess): # indicates correct and incorrect letter placement/usage
    hint = ''
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            hint += '@'
        elif guess[i] in secret:
            hint += '*'
        else:
            hint += '-'
    return hint

def getGuess(word_length): # indicates length of secret word
    while True:
        guess = input(f"Guess a word ({word_length} letters): ")
        if len(guess) == word_length:
            return guess
        else:
            print(f"You must guess a word with {word_length} letters.")

def playGame(word):
    # Print introduction
    print(INTRO)

    # Print the word length before starting guesses
    print(f"The word has {len(word)} letters.")

    # Initialize guess counter
    guesses = 0

    # Main game loop
    while True:
        # Get a valid guess using getGuess
        guess = getGuess(len(word))
        guesses += 1

        # Get hints using letterHints
        hint = letterHints(word, guess)

        # Only print hint if the guess is incorrect
        if hint != "@" * len(word):
            print(hint)

        # Check if the guess is correct
        if hint == "@" * len(word):
            print(f"Congratulations! You guessed it, the word was: {word}")

            # Print appropriate message based on number of guesses
            if guesses == 1:
                print("Wow, you guessed it in one try!")
            elif guesses < 7:
                print(f"Great job! You guessed the word in just {guesses} tries.")
            else:
                print(f"You guessed the word in {guesses} tries.")
            break

WORDS = [
    "assign", "alias", "append", "branch", "binary", "boolean",
    "catch", "comment", "copy", "data", "debug", "declare",
    "element", "error", "empty", "file", "float", "format",
    "global", "game", "grid", "hash", "header", "heap",
    "input", "integer", "iterate", "join", "joule", "jump",
    "keyword", "kernel", "keys", "loop", "list", "local",
    "mutable", "method", "module", "none", "newline", "nested",
    "object", "open", "order", "python", "print", "pattern",
    "quote", "queue", "quine", "range", "return", "recurse",
    "syntax", "string", "shell", "test", "tuple", "turtle",
    "update", "unique", "user", "value", "void", "virtual",
    "while", "wave", "word", "xerox", "yield", "zero", "zombie"
]

def playRandomGame():
    """
    Works like playGame, except the word is chosen randomly from the
    WORDS list. Use this to play a game where you don't know the answer
    ahead of time.
    """
    playGame(random.choice(WORDS))
