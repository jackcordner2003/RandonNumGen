# Random Number Generator

import random

def randomNumber():
    print("Random Number Genertor\n")

    num1 = int(input("Please Enter the First Number\n"))

    num2 = int(input("Please Enter the Second Number\n"))

    if(num2 <= num1):
        print("\n Number 2 must be higher than Number 1  \n\n")
        randomNumber()
    else:
        print("\n Random Number: ", random.randint(num1, num2) + "\n\n")


running = True

while(running == True):
    randomNumber()
    
    choice = input("\nDo you want to generate another random number? (yes/no): \n\n\n")
    if choice.lower() != "yes":
        running = False
