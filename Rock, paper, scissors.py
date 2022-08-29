'''Rock paper and scissors v1.0'''
'''Future adds: GUI, icons, skins, lizar and spoke update'''

import random

python_points = 0
user_points = 0

choices = ["scissors","paper","rock"]

while True: # para que todo siga repitiendose una vez acaba
    python_choice = random.choice(choices) #el ordenador seleciona su elección de manera aleatoria dentro de la lista
    user_choice = None 

    while user_choice not in choices: # si el jugador no ha seleccionado una opción correcta volverá a mandarle el input hasta que envie una correcta
        user_choice = input("Select your choice: ").lower()

    print("\nYour choice is: " + user_choice + "\nPython choice is: " + python_choice + "\n")
# este if es donde determinamos que se imprimirá en pantalla según que elecciones hayan salido y a quién se le suma un punto
    if  user_choice == python_choice:
        print("Tie\n")
    elif user_choice == "rock":
        if python_choice == "paper":
            print("You lose")
            python_points += 1
        elif python_choice == "scissors":
            print("You win")
            user_points += 1

    elif user_choice == "paper":
        if python_choice == "scissors":
            print("You lose")
            python_points += 1
        elif python_choice == "rock":
            print("You win")
            user_points += 1

    elif user_choice == "scissors":
        if python_choice == "rock":
            print("You lose")
            python_points += 1
        elif python_choice == "paper":
            print("You win")
            user_points += 1
        
    print("The scores are: \n" + "\tPython score: " + str(python_points) + "\n" + "\tYour score: " + str(user_points))

    replay = str(input("Do you want to play againg? (yes/no): ")) # guardamos la desición del usuario de querer o no continuar jugando
# con este if paramos o no el while true
    if replay != "yes": 
        break
print("Bye bye!!, see you soon!")