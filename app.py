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
    print("# ABFRAGE DER BUCHSTABEN #")
    l_inp = input('''
    Bitte gib deine Buchstaben ohne Trennzeichen ein.
    Groß- oder Kleinbuchstaben spielen keine Rolle. Bsp.: AelLNZ
    Bestätige deine Eingabe mit ENTER.

    Deine Buchstaben: ''')
    print("")

    if len(l_inp) < 1:
        l_inp = "ETTAEST"
        print(f"WARNUNG: Keine Buchstaben erhalten. Folgenden Buchstaben werden ausgewählt: { l_inp }")
        print("")

    l = sorted( list( l_inp.lower() ) )

    return l

LETTERS = inp_letters()


## Funtion to count letters
def count_letters(letters):
    d = dict()

    for letter in letters:
        if letter not in d:
            d[letter] = 1
        else :
            d[letter] += 1
    
    print("# ANZAHL DER BUCHSTABEN #")
    print(f'''
    Du hast folgende {sum(d.values())} Buchstaben: 
    {[str(n) + "x " + a.upper() for a,n in d.items()]}
    ''')

    return d

L_COUNT = count_letters(LETTERS)


## Function to match letters to dictonary words

## Function to select highest-scoring word based on point(s) per letter

## Function to return top 5 words
