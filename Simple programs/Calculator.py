'''Calculator v1.0'''

'''Future adds: GUI, factorial, sen, con, tg, arcsen, arccon, arctg, 
    de radianes a grados y viseversa, de celsius a farenheit y a kelvin y viseversa, ecuaciones cuadradas, derivadas'''

import math

def sum(a, b):
    print((a + b))

def rest(a, b):
    print((a - b))

def mult(a, b):
    print((a * b))

def div(a, b):
    print((a / b))

def sqrt(a, b):
    print(a**(1/float(b)))

def pow(a, b):
    print(math.pow(a, b))

def MCD(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return(a)

def mcm(a, b):
    c = MCD(a, b)
    print((a * b) / c)

def welcome():
    print("Welcome to the calculator, what do you want to do? \n \n * equal, \n * substract, \n * multiply, \n * divide, \n * root, \n * power, \n * mcm(lowest common multiple), \n * MCD(highest common factor): \n ")

options = ("equal", "substract", "multiply", "divide", "root", "power", "mcm", "MCD")

while True: # para que todo siga repitiendose una vez acaba
    welcome()
    choice = input("Enter your choice: ")

    if choice in ("equal", "substract", "multiply", "divide", "root", "power", "mcm", "MCD"):
        num1 = float(input("Select the first numer: "))
        num2 = float(input("Select the second numer: "))
# este if se encarga de ejecutar la función correspondiente a cada elección del usuario
        if choice == "equal":
            sum(num1, num2)
        elif choice == "substract":
            rest(num1, num2)
        elif choice == "multiply":
            mult(num1, num2)
        elif choice == "divide":
            div(num1, num2)
        elif choice == "root":
            sqrt(num1, num2)
        elif choice == "power":
            pow(num1, num2)
        elif choice == "mcm":
            mcm(num1, num2)
        elif choice == "MCD":
            MCD(num1, num2)
            print(MCD(num1, num2))

    dessicion = input("Do you want to leave or to continue? (yes/no): ") # guardamos la desición del usuario de querer o no continuar
    if dessicion != "yes": # con este if paramos o no el while true
        print("Byee, see yo soon")
        break

