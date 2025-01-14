"""
Input: User choices guide them through a simple story.
Output: Consequences of the choices.
Key Concepts: Functions, conditionals, and loops.
"""

import os
import time

os.system('clear')
name = input("Enter your name?")

def main():
    os.system('clear')
    print("\t\t\t***Snake Jungle***\t\t\t")

    print("""
                 ___         ____       __
                / __|       /  _ \     /  /
                _          /  / \ \   /  /
                  \       /  /   \ \_/  /
                _ _/     /__/     \___ /
                
        """)
    print("""
    Welcome to Snake Island.\n
    The Island is filled with deadliest snakes\n
    One wrong move and you're on their menu.
    Will you reach the end, or will you be devoured???
    """)

    choice = input("Press 0 to begin the match.")
    choice = int(choice)


def start():
    while True:
        os.system('clear')
        print("welcome...")
        print("You have to choose a jungle. \n 1.Amazon or\n 2.Africa \n 3.Australian Jungle 1 or\n 4.Snake island\n 5.exit")
        choice = int(choice)
        if choice == 1:
            amazon()
        elif choice == 2:
            africa()
        elif choice == 3:
            australia()
        elif choice == 4:
            snakeIsland()
        else:
            print("This jungle will come soon.")
            print("Pick from the remaining")
        continue


def amazon():
    print("Amazon? are you sure?...")
    time.sleep(2)
    print("Not afraid of the constrictor snakes I see?")
    time.sleep(2)
    print("Travelling....")
    time.sleep(2)
    print("Arrived...")
    time.sleep(2)
    os.system("clear")

    print(f"Hae {name}, you've arrived at amazon. I'm Lisa!")
    print("Your personal guardian for this journey")
    print("we have two roads ahead of us one is murram the other is tarmac\n which one should we follow")
    print("\n1.murram \n2.tarmac")
    choice = int(choice)
    if(choice == 1):
        print("walking...")
        time.sleep(1)
        print("30 minutes later.")
        time.sleep(2)
        print(f"Lisa: {name},what a dusty road.")
        time.sleep(1)
        print(f"{name}: Yeah.")
        print("Lisa: There is a borehole ahead, we can drink there")
        print("Can't wait")
        time.sleep(1)
        print("Tchk.")
        time.sleep(1)
        print("{name}: Did you hear that?")
        print("Lisa: No")
        print("{name}:I swear i heard something")
        time.sleep(2)
        print("Lisa: Didn't know i was walking with a scaredy cat!")
        print("*Behind lisa's back a snake raised its ahead, a BOA!*")
        print("*Ready to pounce on young Lisa*")
        print("1. Protect Lisa or 2.Run away")
        choice = int(choice)
        if choice == 1:
            print("Lisa: Did i mention i am a virtual")
            print("Animals, can't see me or touch me, only you can")
            print("The Boa jumped and curled around {name}")
            print("{name}: why didn't you say sooner?")
            time.sleep(1)
            print("Lisa: You didn't ask?")
            print("*Life is squeezed out, you are dead!!!")
            print("Lisa:They never learn. What a big dish for the boa.")

        elif(choice == 2):
            print("10 minutes later...")
            time.sleep(2)
            print("Lisa: How could you leave a 10 year old like that.")
            print("{name}: I put myself above everyone")
            time.sleep(1)
            print("{name}:There is this saying. Once life is precious.")
            print("#Lisa thinking: *such a vile man, to kill the courageous ia easy, \n but the cowardly it's hard. How will i feed my baby snakes.")
        
        else:
            print("You die, No escape to the matrix")

def africa():
    os.system('clear')
    print('Welcome to Africa')    




main()