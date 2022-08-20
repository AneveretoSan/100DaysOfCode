from words import words
import random
import string

def valid_word(words): # se encarga de elejir de la lista una palabra válida, ignorando comas, espacios o guiones. Pra luego devolver la palabra válida.
    word  = random.choice(words)
    while '-' in word or ' ' in word:
        word  = random.choice(words)
    
    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word) # un set de todas la letras de la palabra
    alphabet = set(string.ascii_uppercase) # un set de todas la lestras del alfabeto
    used_letters = set() 

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left" "\n" "Yo have use this letters: ", ' '.join(used_letters)) # va añadiendo las letras que ha ido usando el usuario

        word_list = [letter if letter in used_letters else '_' for letter in word] # almacena las letras adivinadas de la palabra
        print("Current word: ", ' '.join(word_list)) # escribe las letras adivinadas de la palabra

        user_letter = input("Gues a letter: ").upper()
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                lives = lives -1
                print("This letter is not in the word")
        
        elif user_letter in used_letters:
            print("You have alredy use this letter")
        
        else:
            print("Invalid character")

    if lives == 0:
        print("You died, the word was", word)
    else:
        print("You guessed the word", word, "!!!")
    replay = str(input("Do you want to play againg? (yes/no): "))
    if replay == "yes":
        hangman()
    else:
        print("Bye bye!!, see you soon!")

hangman()


