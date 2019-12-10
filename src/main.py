# Main game file

import zork
def intro(num):
        if num == 4:
                print("---------------------------------------------------------")
                print("You are standing in an open field west of a white house.")
                print("You can see a small lake to the north.")
                print("(A secret path leads southwest into the forest.)")
                print("There is a Small Mailbox.")
        elif num == 1:
                print("---------------------------------------------------------")
                print("You find yourself at the edge of a beautiful lake aside rolling hills.")
                print("A small pier juts out into the lake.")
                print("A fishing rod rests on the pier.")
                print("(You can see a white house in the distance to the south.)")
        elif num == 8:
                print("---------------------------------------------------------")
                print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        elif num == 9:
                print("---------------------------------------------------------")
                print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
                print("There is an open grating, descending into darkness.")
        elif num == 10:
                print("---------------------------------------------------------")
                print("You are in a tiny cave with a dark, forbidding staircase leading down.")
                print("There is a skeleton of a human male in one corner.")
        elif num == 11:
                print("---------------------------------------------------------")
                print("You have entered a mud-floored room.")
                print("Lying half buried in the mud is an old trunk, bulging with jewels.")
        elif num == 3:
                print("---------------------------------------------------------")
                print("You are behind the massive house. There seems to be a gap big enough to fit through to the west.")
                print("There might be a door though if you walk around to the south")
        elif num == 2:
                print("---------------------------------------------------------")
                print("You find yourself in a dimly lit kitchen with dust covering the floor.")
                print("A lantern rests on the kitchen island.")
                print("A set of stairs leads up to another room.")
        elif num == 5:
                print("---------------------------------------------------------")
                print("You find yourself in a dimly lit attic with dust covering the floor.")
                print("There is a magical portal in the far back corner")
                print("A set of stairs leads back to the kitchen")
def main():
        print("---------------------------------------------------------")
        print("Welcome to Zork - The Unofficial Python Version.")
        print("\nStatus Alive")
        loop = [4,1]
        while loop[1] == 1:
            intro(loop[0])
            choice = input("What do you do?\n")
            
            if choice.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("Status: Dead")
                print("---------------------------------------------------------")
                loop=[0,2]
            elif loop[1]==1:
                print("\n---------------------------------------------------------")
                print ("Status: Alive")
            if loop[0] == 4:
                loop=zork.starting_spot(choice)
            elif loop[0] == 1:
                loop=zork.the_lake(choice)
            elif loop[0] == 8:
                loop=zork.the_forest(choice)
            elif loop[0] == 9:
                loop=zork.the_grate(choice)
            elif loop[0] == 10:
                loop=zork.the_cave(choice)
            elif loop[0] == 3:
                loop=zork.back_of_house(choice)
            elif loop[0] == 5:
                loop=zork.attic(choice)
            elif loop[0] == 2:
                loop=zork.kitchen(choice)
            elif loop[0] == 11:
                loop=zork.the_end(choice)
                if loop[0] == 1101:
                    loop[1] = 2

        dead_inp = input("Do you want to play again? Y/N ")
        if dead_inp.lower() == ("n"):
                print("Thanks for playing!")
                print("---------------------------------------------------------")
        if dead_inp.lower() == ("y"):
                main()

main()





