# Define functions used in app.py

## Function to take user input letters
def inp_letters() :
    print("# ABFRAGE DER BUCHSTABEN #")
    l_inp = input('''
    Bitte gib deine Buchstaben ohne Trennzeichen ein.
    Groß- oder Kleinbuchstaben spielen keine Rolle. Bsp.: AelLNZ
    Bestätige deine Eingabe mit ENTER.

    HINWEIS: Du kannst das Programm jederzeit beenden mit STRG + C

    Deine Buchstaben: ''')
    print("")

    if len(l_inp) < 1 :
        l_inp = "EEFTSET"
        print(f"WARNUNG: Keine Buchstaben erhalten. Folgenden Buchstaben werden ausgewählt: { l_inp }")
        print("")

    l = sorted( list( l_inp.lower() ) )

    return l


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


## Function to match letters to dictonary words
def check_words(letters_dict, word_dict, letter_scores):
    print("Suche nach möglichen Wörtern...")
    print("")

    possible_words = {}
    for word in word_dict:
        score = 0
        if len(word) > sum(letters_dict.values()):
            continue

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
    {list(possible_words.keys())}
    ''')

    return possible_words


## Function to select highest-scoring word based on point(s) per letter
def best_words(possible_words):
    print("Suche die Wörter mit den meisten Punkten...")
    print("")

    word_dict = [ (s,w) for w,s in possible_words.items() ]
    word_dict = sorted( word_dict, reverse=True )
    word_best = dict( [ (w,s) for s,w in word_dict[0:5] ] )
    
    # OPTIONAL: if there are multiplication fields at certain letter positions
    # ... increase scores...

    print("# WÖRTER MIT DEN MEISTEN PUNKTEN #")
    print(f'''
    Folgende Wörter bringen dir die meisten Punkte:
    {word_best}
    ''')
    
    return word_best