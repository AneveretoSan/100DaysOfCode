import random
from Player import Player
from Computer import Computer
from Choice import Choice


class Main:
    player_name = ""
    player1 = Player(0, player_name, None)
    computer = Computer(0, None)

    while True: # para que todo siga repitiendose una vez acaba
        computer.option = random.choice(Choice.choices) #el ordenador seleciona su elección de manera aleatoria dentro de la lista
        player1.option = None

        while player1.option not in Choice.choices: # si el jugador no ha seleccionado una opción correcta volverá a mandarle el input hasta que envie una correcta
            player1.option = input("Select your choice: ").lower()

        print("\nYour choice is: " + player1.option + "\nPython choice is: " + computer.option + "\n")
    # este if es donde determinamos que se imprimirá en pantalla según que elecciones hayan salido y a quién se le suma un punto
        if  player1.option == computer.option:
            print("Tie\n")
        elif player1.option == "rock":
            if computer.option == "paper":
                print("You lose")
                computer.option += 1
            elif computer.option == "scissors":
                print("You win")
                player1.points += 1

        elif player1.option == "paper":
            if computer.option == "scissors":
                print("You lose")
                computer.option += 1
            elif computer.option == "rock":
                print("You win")
                player1.points += 1

        elif player1.option == "scissors":
            if computer.option == "rock":
                print("You lose")
                player1.points += 1
            elif computer.option == "paper":
                print("You win")
                player1.points += 1
            
        print("The scores are: \n" + "\tPython score: " + str(computer.points) + "\n" + "\tYour score: " + str(player1.points))

        replay = str(input("Do you want to play againg? (yes/no): ")) # guardamos la desición del usuario de querer o no continuar jugando
    # con este if paramos o no el while true
        if replay != "yes": 
            break
    print("Bye bye!!, see you soon!")
