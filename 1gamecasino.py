# coding: utf-8
# игра типа казино - игроку предлагается угадать число от 1 до 10, которое случайно генерируется; всего дается 10 попыток

import random

attempt = 1

welcome_message = input("Hi! Do you want to play the game? ")

if welcome_message == "yes":
    print("Let's start! Enter number from 1 to 10: ")

    while attempt < 10:
        number = int(input())
        reference_number = random.randint(1, 10)
        print(reference_number)
        if number == reference_number:
            print("You win!")
            exit()
        else:
            print("Oops! Try again.")
            attempt += 1
else:
    print("Goodbye!")
    exit()
