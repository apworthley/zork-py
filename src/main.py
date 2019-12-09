# Main game file

import zork
def main():
        alive=1
        print("---------------------------------------------------------")
        print("Welcome to Zork - The Unofficial Python Version.")
        loop = 4
        while alive == 1:
            zork.intro(loop)
            choice = input("What do you do?\n")
            if choice.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive=2
            elif loop == 4:
                loop=zork.four(choice)
            elif loop == 1:
                loop=zork.one(choice)
            elif loop == 8:
                loop=zork.eight(choice)
            elif loop == 9:
                loop=zork.nine(choice)
            elif loop == 10:
                loop=zork.ten(choice)
            elif loop == 11:
                loop=zork.eleven(choice)
                if loop == 1101:
                    alive = 2

        dead_inp = input("Do you want to play again? Y/N ")
        if dead_inp.lower() == ("n"):
                print("Thanks for playing!")
                print("---------------------------------------------------------")
        if dead_inp.lower() == ("y"):
                main()

main()

def PrintOutput(s):
        print("OUTPUT", s)




