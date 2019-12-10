import items




def starting_spot(second):
	
        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                return [4,1]
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                return [4,1]
        elif second.lower() == ("go north"):
                return [1,1]
        elif second.lower() == ("go east"):
                return [3,1]
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                return [4,1]
        elif second.lower() == ("go southwest"):
                return [8,1]
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                return [4,1]
        else:
                print("---------------------------------------------------------")
                return [4,1]

def the_lake(north_house_inp):
	# North of House

        if north_house_inp.lower() == ("go south"):
                return [4,1]
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                return [1,1]
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                return [1,1]
        else:
                print("---------------------------------------------------------")
                return [1,1]

def the_forest(forest_inp):

	# Southwest Loop

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                return [8,1]
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                return [8,1]
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                return [8,1]
        elif forest_inp.lower() == ("go east"):
                return [9,1]
        else:
                print("---------------------------------------------------------")
                return [8,1]
def the_grate(grating_inp):
	# East Loop and Grating Input
		

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                return [9,1]
        elif grating_inp.lower() == ("descend grating"):
                return [10,1]
        else:
                print("---------------------------------------------------------")
                return [9,1]

def the_cave(cave_inp):
	

        if cave_inp.lower() == ("descend staircase"):
                return [11,1]
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                return [10,1]
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                return [10,1]
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                return [10,1]
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                return [10,1]
        elif cave_inp.lower() == ("go down staircase"):
                return [11,1]
        elif cave_inp.lower() == ("scale staircase"):
                return [11,1]

        else:
                print("---------------------------------------------------------")
                return [10,1]
def back_of_house(room):
        if room.lower() == ("go west"):
                return[2,1]
        elif room.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("There was a high fence that you were unable to climb")
                return[3,1]
        elif room.lower() == ("go back"):
                return[4,1]
        else:
                print("---------------------------------------------------------")
                return [3,1]
def kitchen(options):
        if options.lower() == ("go up stairs"):
                return [5,1]
        elif options.lower() == ("pick up lantern"):
                print("The lamp is super glued to the table.")
                return [2,1]
        elif options.lower() == ("look for food"):
                print("there is no food, sorry!")
                return [2,1]
        elif options.lower() == ("go back outside"):
                return [3,1]
        else:
                print("---------------------------------------------------------")
                return [2,1]
def attic(portal):
        if portal.lower() == "go in portal":
                return [8,1]
        elif portal.lower() == "go back down":
                return[2,1]
        else:
                print("---------------------------------------------------------")
                return [5,1]
		# End of game
def the_end(last_inp):
			
        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
                print("---------------------------------------------------------")
                return [1101,1]

       
        else:
                print("---------------------------------------------------------")
                return [11,1]
			
		
