from words import words
import random
import string

def valid_word(words):
    word  = random.choice(words)
    while '-' in word and ' ':
        word  = random.choice(words)
    
    return word

def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii.uppercase)
    used_words = set()
    for i in word_letters:
        print('_')

valid_word()
hangman()