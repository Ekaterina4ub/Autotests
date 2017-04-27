#coding: utf-8
import random

attempt = 1

welcome_message = raw_input("Hi! Do you want to play the game? ")

if welcome_message == "yes":
    print("Let's start! Enter number from 1 to 10: ")
    number = input("")
    reference_number = random.randint(1, 10)
    print(reference_number)

    while attempt < 10:

        if number == reference_number:
            print("You win!")
            exit()
        else:
            print("Oops! Try again.")
            number = input("")
            reference_number = random.randint(1, 10)
            print(reference_number)
            attempt += 1
else:
    print("Goodbye!")
    exit()
