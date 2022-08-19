#from words import words
import random
import string

words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing"]

def valid_word(words):
    word  = random.choice(words)
    while '-' in word and ' ':
        word  = random.choice(words)
    
    return word

def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("Yo have use this letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list), word)

        user_letter = input("Gues a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have alredy use this letter")
        
        else:
            print("Invalid character")

hangman()


