import items


def intro(num):
        if num == 4:
                print("---------------------------------------------------------")
                print("You are standing in an open field west of a white house, with a boarded front door.")
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

def four(second):
	
        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                return 4
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                return 4
        elif second.lower() == ("go north"):
                return 1
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
                return 4
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                return 4
        elif second.lower() == ("go southwest"):
                return 8
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                return 4
        else:
                print("---------------------------------------------------------")
                return 4

def one(north_house_inp):
	# North of House

        if north_house_inp.lower() == ("go south"):
                return 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                return 1
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                return 1
        else:
                print("---------------------------------------------------------")
                return 4

def eight(forest_inp):

	# Southwest Loop

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                return 8
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                return 8
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                return 8
        elif forest_inp.lower() == ("go east"):
                return 9
        else:
                print("---------------------------------------------------------")
                return 8
def nine(grating_inp):
	# East Loop and Grating Input
		

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                return 9
        elif grating_inp.lower() == ("descend grating"):
                return 10
        else:
                print("---------------------------------------------------------")
                return 9

def ten(cave_inp):
	

        if cave_inp.lower() == ("descend staircase"):
                return 11
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                return 10
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                return 10
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                return 10
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                return 10
        elif cave_inp.lower() == ("go down staircase"):
                return 11
        elif cave_inp.lower() == ("scale staircase"):
                return 11
        else:
                print("---------------------------------------------------------")
                return 10


		# End of game
def eleven(last_inp):
			
        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
                return 1101
       
        else:
                print("---------------------------------------------------------")
                return 11
			
		
