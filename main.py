"""
Input: User choices guide them through a simple story.
Output: Consequences of the choices.
Key Concepts: Functions, conditionals, and loops.
"""

import os
import time
import sys

os.system('clear')
name = input("Enter your name?")

def main():
    os.system('clear')
    print("\t\t\t***Snake Jungle***\t\t\t")


    #snake adventures figlet
    print("""
            _____ _   _   ___   _   __ _____  ___ ______ _   _ _____ _   _ _____ _   _______ _____ _____ 
            /  ___| \ | | / _ \ | | / /|  ___|/ _ \|  _  \ | | |  ___| \ | |_   _| | | | ___ \  ___/  ___|
            \ `--.|  \| |/ /_\ \| |/ / | |__ / /_\ \ | | | | | | |__ |  \| | | | | | | | |_/ / |__ \ `--. 
            `--. \ . ` ||  _  ||    \ |  __||  _  | | | | | | |  __|| . ` | | | | | | |    /|  __| `--. \
            /\__/ / |\  || | | || |\  \| |___| | | | |/ /\ \_/ / |___| |\  | | | | |_| | |\ \| |___/\__/ /
            \____/\_| \_/\_| |_/\_| \_/\____/\_| |_/___/  \___/\____/\_| \_/ \_/  \___/\_| \_\____/\____/     
        """)
    print("""\t\t
    Welcome to Snake Island.\n
    The Island is filled with deadliest snakes\n
    One wrong move and you're on their menu.
    Will you reach the end, or will you be devoured???
    """)

    choice = input("Press 0 to begin the match and 1 to close")
    choice = int(choice)

    if choice == 0:
        start()
    else:
        sys.exit()


def start():
    while True:
        os.system('clear')
        print("welcome...")
        print("You have to choose a jungle. \n 1.Amazon \n 2.Africa \n 3.Australian Jungle \n 4.Snake island\n 5.exit")
        choice = input()
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
            sys.exit()

#amazon function
def amazon():
    os.system('clear')
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
    choice = input()
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
        print(f"{name}: Can't wait")
        time.sleep(1)
        print("Tchk.")
        time.sleep(1)
        print(f"{name}: Did you hear that?")
        print("Lisa: No")
        print(f"{name}:I swear i heard something")
        time.sleep(2)
        print("Lisa: Didn't know i was walking with a scaredy cat!")
        print("*Behind lisa's back a snake raised its ahead, a BOA!*")
        print("*Ready to pounce on young Lisa*")
        print("1. Protect Lisa or 2.Run away")
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("Lisa: Did i mention i am a virtual.")
            print("Animals, can't see me or touch me, only you can.")
            print(f"The Boa jumped and curled around {name}.")
            print(f"{name}: why didn't you say sooner?")
            time.sleep(1)
            print("Lisa: You didn't ask?")
            print("*Life is squeezed out, you are dead!!!")
            print("Lisa:They never learn. What a big dish for the boa.")
            goToMain()

    elif(choice == 2):
        print("10 minutes later...")
        time.sleep(2)
        print("Lisa: How could you leave a 10 year old like that.")
        print(f"{name}: I put myself above everyone")
        time.sleep(1)
        print(f"{name}:There is this saying. Once life is precious.")
        print("#Lisa thinking: *such a vile man, to kill the courageous is easy, \n but the cowardly it's hard. How will i feed my baby snakes.")
        goToMain()
    
    else:
        print("You die, No escape to the matrix")
        goToMain()

#africa function
def africa():
    import random
    os.system('clear')
    print('Welcome to Africa')
    print('The Home Land of the Black Mamba')
    print("Lisa: Hi, I'm Lisa your guide.")
    time.sleep(2)
    print("Lisa: Do you want to know a fun fact about black mambas(yes/no)")
    ans = input().lower()
    if ans == 'yes':
        print("Lisa: Black Mambas are the fastest snakes in Africa")
        print("Lisa: Non-poisnous, would you like to see one(yes/no)")
        ans = input().lower()
        if(ans == 'yes'):
            os.system('clear')
            print("\t\t**Welcome To Mamba City**")
            ans = input("Lisa: I have three snakes one must bite you.\n which snake number do you want a bite from\n pick carefully.(press 0 if you want pc to pick for you)(choose between (1 to 3))")

            ans  = int(ans)

            luck = ans

            if ans == 0:
                luck = random.randint(1,3)
            
            match luck:
                case 1: 
                    print("Lisa: You've been bitten by Puff Adder, \n Lisa: Goodbye mate, till next time" )
                    print("You diE")
                    sys.exit()
                case 2:
                    print("Lisa: Black Mamba is your good night friend")
                    print("You die")
                case 3:
                    print("Lisa: You've been bitten by boomslang, highly venomous")
                    time.sleep(3)
                    print("Lisa: But I have the antidote")
                    ans = input("Lisa: 1. Gravel for the antidote or 2. Die with honour (1/2)")
                    ans = int(ans)
                    if ans == 1:
                        print("Lisa: You survive.")
                        print("Lisa: You win.")
                        print("Congratulations for completing africa")

                    ans = input('Restart game:(yes/no)')
                    if ans.lower == 'yes':
                        main()
                    else:
                        goToMain()
        
        else:
            print("You die")
            print("Can't escape the matrix, you must accept")

#australia function
def australia():
    os.system('clear')
    print("It's australia, Where people eat snake for breakFast")
    print("You meet a 8 year old child")

    ans = input('child1: Here take the snake. (yes/no)')
    if(ans.lower == 'yes'):
        print(f"{name}: such a young nice snake")
        time.sleep(2)
        print("child1: yeah, it's a taipan.")
        print("Lisa: chuckle")
    else:
        print("Child1: Why??? It's just a taipan, you scaredy cat.")
        print(f"{name}: I'm not a scared cat")
        ans = input(f"{name}: furious,(1.push the girl away or 2. walk away)(1 or 2)")

        ans = int(ans)

        if ans == 1:
            print("Lisa: You are so heartless")
            print("You die")
            print("Lisa and child1 stare at your carcass, \n Lisa: We all love children, never be harsh on them.")
            print("child1: mmmh")
            goToMain()

        else:
            print(f"Lisa: where should we go now {name}")
            time.sleep(2)
            print(f"{name}: far from him")
            print("Lisa: Australian reptile park it is")
            time.sleep(2)

            print(f"{name}: what???")
            print("swoosh! you appear in the reptile park")
            time.sleep(2)
            print(f"{name}: I hate this")
            time.sleep(2)
            print("Lisa: Let's play a game.")
            print(f"{name}:Which one?")
            time.sleep(2)
            print("Lisa: snake eating game.")
            time.sleep(2)

            print(f"{name}: Okay, let us view first then play later")
            print("Lisa: okay")
            time.sleep(2)
            print("Lisa: You know your death comes first")
            print(f"{name}: hahaha")
            goToMain()

#snake island function
def snakeIsland():
    print("You die😊")
    goToMain()

#goes back to main or exit the program in every jungle
def goToMain():
    print("\nGo back to main(yes/no), no to close the program")
    choice = input()
    if choice.lower() == 'yes':
        main()
    else:
        sys.exit()    
    

main()