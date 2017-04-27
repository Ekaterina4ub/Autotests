#coding: utf-8
import random

message = raw_input("Hi! Do you want to play the game? ")

if message == "yes":
    print("Let's start! Enter number from 1 to 10: ")
    a = input("")
    b = random.randint(1, 10)
    print(b)
    i = 1
while i < 10:
     if a == b:
         print("You win!")
         exit()
     else:
         print("Oops! Try again.")
         a = input("")
         b = random.randint(1, 10)
         print(b)
         i += 1
else:
    print("Goodbye!")
    exit()
