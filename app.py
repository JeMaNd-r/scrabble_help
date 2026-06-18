# App to provide the best-scoring word in Scrabble based on a user-given set of letters

## Load libraries


## Define constants
LETTER_SCORES = {
    "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}

WORD_DICT = [
    "Test",
    "festet",
    "festete",
    "Fester",
    "Festat"
]


## Function to take user input letters
def inp_letters() :
    print("# ABFRAGE DER BUCHSTABEN #")
    l_inp = input('''
    Bitte gib deine Buchstaben ohne Trennzeichen ein.
    Groß- oder Kleinbuchstaben spielen keine Rolle. Bsp.: AelLNZ
    Bestätige deine Eingabe mit ENTER.

    Deine Buchstaben: ''')
    print("")

    if len(l_inp) < 1 :
        l_inp = "EEFTSET"
        print(f"WARNUNG: Keine Buchstaben erhalten. Folgenden Buchstaben werden ausgewählt: { l_inp }")
        print("")

    l = sorted( list( l_inp.lower() ) )

    return l

LETTERS = inp_letters()


## Funtion to count letters
def count_letters(letters) :
    d = dict()

    for letter in letters :
        if letter not in d :
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
def check_words(letters_dict, word_dict, letter_scores):
    possible_words = {}
    for word in word_dict:
        score = 0
        for i in range(len(word)) :
            letter = word[i].lower()
            if letter not in letters_dict :
                break
            
            if letters_dict.get(letter) < word.count(letter) :
                break
            
            score += letter_scores.get(letter.upper())
            
            if i == (len(word)-1):
                possible_words[word] = score
    
    print("# MÖGLICHE WÖRTER #")
    print(f'''
    Folgende Wörter kannst du mit deinen Buchstaben bilden: 
    {list(possible_words.keys())}''')

    return possible_words

WORDS = check_words(L_COUNT, WORD_DICT, LETTER_SCORES)         

## Function to select highest-scoring word based on point(s) per letter

## Function to return top 5 words
