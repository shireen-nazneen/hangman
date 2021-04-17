import string
from image import IMAGES
from words import choose_word
def is_word_guessed(secret_word, letters_guessed):
    return False
def get_guessed_word(secret_word, letters_guessed):
    index=0
    guessed_word=""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+= "_"
        index+=1
    return guessed_word
import string
def if_valid(user):
    if user.isalpha():
        return True
        if len(user)==1:
            return True
        else:
            return "invalid"
    else:
        return "invalid"
def get_available_letters(letters_guessed):
    import string
    letters_left=list(string.ascii_lowercase)
    shireen=""
    for j in letters_left:
        if j not in letters_guessed:
            shireen+=j
    return shireen
def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)
def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    j=0
    while j<1:
        user=input("enter game level for Easy (1) ,medeum (2) , hard(3) ")
        if user=="1":
            remaining_lives=8
            count_wrong_input=0
            j+=1
        elif user=="2":
            remaining_lives=6
            count_wrong_input=2
            j+=1
        elif user=="3":
            count_wrong_input=4
            remaining_lives=4
            j+=1
        else:
            continue
    letters_guessed=[]
    count=0
    while remaining_lives>0:
        available_letters=get_available_letters(letters_guessed)
        print("Available letters: " + available_letters)
        guess=input("Please guess a letter: ")
        letter=guess.lower()
        if letter=="hint":
            if count==0:
                print("your hint for this secret word is this --"+ get_hint(secret_word,letters_guessed))
                count+=1
            else:
                print("hint alrady used")
        if letter not in get_available_letters(letters_guessed):
            continue
        if not if_valid(letter):
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print( "Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("")
            if is_word_guessed(secret_word, letters_guessed)==True:
                print( " * * Congratulations, you won! * * ")
                break
        else:
            available_letters=get_available_letters(letters_guessed)
            letters_guessed.append(letter)
            print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, letters_guessed))

            print(IMAGES[count_wrong_input])
            remaining_lives-=1
            print("remaining lives ",remaining_lives)
            count_wrong_input+=1
    if is_word_guessed(secret_word, letters_guessed)==False:
        print("sorry your lives is over")
        print("*** game over please try again***")
secret_word = choose_word()
hangman(secret_word)
                                            
