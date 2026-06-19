# App to provide the best-scoring word in Scrabble based on a user-given set of letters

## Load libraries
import json
import time

## Import functions saved in other py file
from functions import inp_letters
from functions import count_letters
from functions import check_words
from functions import best_words


## Define constants
LETTER_SCORES = {
    "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "Ä": 6, "Ü": 6,
    "J": 8, "X": 8, "Ö": 8,
    "Q": 10, "Z": 10
}

# WORD_DICT = [
#     "Test",
#     "festet",
#     "festete",
#     "Fester",
#     "Festat"
# ]

with open("wordlist.json", 'r') as f:
    WORD_DICT = json.load(f)


# Perform app

while True:
    LETTERS = inp_letters()
    time.sleep(3)

    L_COUNT = count_letters(LETTERS)

    WORDS = check_words(L_COUNT, WORD_DICT, LETTER_SCORES)         
    time.sleep(3)

    WORDS_TOP5 = best_words(WORDS)

    print("Na, welches nimmst du?")
    time.sleep(3)

    print("")
    input("Hast du neue Buchstaben? Drücke ENTER zum Fortfahren...")
    print("")

