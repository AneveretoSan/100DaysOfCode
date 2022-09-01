import random

computer_number = 0
user_number = 0

min = int(input("Please choose a minimun number: "))
max = int(input("Please choose a maximun number: "))

computer_number = random.randint(min, max)

while user_number != computer_number:
    user_number = int(input("chosse a number: "))
    
    if user_number > computer_number:
            print("Your number is to high ")
    elif user_number < computer_number:
            print("Your number is to low ")
    elif user_number == computer_number:
        print("Your guess the number ")

