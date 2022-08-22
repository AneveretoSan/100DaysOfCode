import random

minimun = 0
limit = 0
limit = int(input("Choose the limit of the range: "))

user_number = 0
user_number = int(input("Choose your number: "))

computer_number = 0

while computer_number != user_number:
    computer_number = random.randint(minimun, limit)
    answer = str(input(str(computer_number) + " Is this number corret(c), too low(l) or to high(h)?: "))
    
    if answer == 'l':
        minimun = computer_number + 1
    elif answer == 'h':
            limit = computer_number - 1
    elif answer == 'c' and computer_number == user_number:
        print("Yes!!, I guess yur number")
    elif answer == 'c' and computer_number != user_number:
        print("You lie to me, don't do that >:(")
    else:
        pass