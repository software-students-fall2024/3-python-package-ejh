import time
from pyAnimals_ejh.pyAnimals_ejh import *

def main():
    while (1):
        try:
            animal = input("Enter an animal (cat, bunny, elephant, rabbit): ").strip().lower()

            try:
                function = int(input("Available functions: \n1. Move\n2. Race\n3. Random Message\n4. Random Fact\nChoose a function (enter a number between 1-4): "))
                while (function < 1 or function > 4):
                    function = int(input("Not a valid function. Please choose a number between 1-4: "))
                
                if (function == 1):
                    move(animal)
                    exit()
                elif (function == 2):
                    race(animal)
                    exit()
                elif (function == 3):
                    randMessage(animal)
                    exit()
                elif (function == 4):
                    print_fact(animal)
                    exit()
                else:
                    print("Error executing program")
                    exit()
            except ValueError as e:
                    print(e)

        except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()