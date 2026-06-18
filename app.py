# App to provide the best-scoring word in Scrabble based on a user-given set of letters

## Load libraries


## Define constants
LETTER_SCORES = {
    "AEILNORSTU": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10 }

## Function to take user input letters
def inp_letters():
    LETTERS = input('''# ABFRAGE DER BUCHSTABEN #

    Bitte gib deine Buchstaben ohne Trennzeichen ein.
    Groß- oder Kleinbuchstaben spielen keine Rolle. Bsp.: AelLNZ
    Bestätige deine Eingabe mit ENTER.

    Deine Buchstaben: ''')

    letters = LETTERS.lower()

    return letters

l = inp_letters()
print(l)

## Function to match letters to dictonary words

## Function to select highest-scoring word based on point(s) per letter

## Function to return top 5 words
