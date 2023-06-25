"""
This is a gussnumber game by me Abdulrahmn69
"""
from random import randint

again = 'y'
while again == 'y':
    number = randint(1, 10)
    tries = 5
    number_of_tries = 0
    print("U have {} chances" .format(tries))
    print("Enter number between 1:10")
    while 1: 
        if tries == 0:
            break
        guss = int(input())
        if guss == number:
            number_of_tries += 1
            print("you get it with {} tries" .format(number_of_tries))
            break
        else:
            if guss > number:
                print("Less than")
                tries -= 1
                number_of_tries += 1
                print("{} chances left".format(tries)) if tries != 1 else print("Last chance")
            else:
                print("Greater than")
                tries -= 1
                number_of_tries += 1
                print("{} chances left".format(tries)) if tries != 1 else print("Last chance")
    again = input("Again ? y / n:  ").strip().lower()
