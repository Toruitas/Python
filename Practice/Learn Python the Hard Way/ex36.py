__author__ = 'Stuart'

def the_woods():
    print("You find yourself in the dark dark woods.\n"
          "What could be lurking around the corner?\n"
          "You hear something crashing through the bushes behind you, and see a clearing ahead.\n"
          "Do you 'look back' or do you 'run away' to the clearing?\n")
    decision = input("> ")
    if "look" in decision or "back" in decision:
        print("You look back just in time to see an 8-eyed monstrosity rush at you.")
        die("Congats, you are now the proud mother of 10,000 baby spider eggs.")
    elif "run" in decision or "clearing" in decision:
        clearing()
    else:
        die("You dawdle around and get eaten by a monster spider.")

def clearing():
    print("As you break through the underbrush out into the sunny clearing, the branches cease cracking behind you.")
    print("You look back just in time to see a giant spindly thing melt back into the darkness")
    print("Oh shit, you left your wallet back in the woods. Do you 'get your wallet' or 'head to high ground")
    decision = input("> ")
    if "wallet" in decision or "get" in decision:
        print("You sneak back into the forest and look for your wallet.")
        print("You don't find it, but what you do find is...")
        die("The giant spider you just ran away from. He's still hungry... X_X")
    elif "high" in decision or "head" in decision:
        print("You decide to keep moving. You're broke anyway.")
        high_ground()
    else:
        print("You decide to lay down and watch clouds for a while...")
        print("Oh shit, a UFO! You've been abducted!")
        print("The aliens are a bunch of sexy ladies who have heard of how amazing human sex is. You live happily ever "
              "after")
        exit(0)
        #ufo()

def high_ground():
    print("You can see pretty far from here. Some sort of weird flying saucer just floated by the clearing you just "
          "left...")
    print("You know, what would be useful is a 'stick', or some 'water' or something...")
    print("What do you want to try to find?")
    decision = input("> ")
    if 'stick' in decision:
        print("Oh look, here's a nice stick.")
        die("You wave it around a little bit, and the sap of the stick gets on your hands and starts to burn. You melt.")
    elif 'water' in decision:
        print("You hear water bubbling over there.")
        print("Yeah the water is vinegar. You kill yourself because this world has vinegar as water and who wants "
              "to live in that kind of place?")
        exit(0)
    else:
        print("Fuck it all.")
        exit(0)

def die(reason):
    print(reason)
    exit(0)

def start():
    print("You wake up in a daze, with your pants around your ankles and a weird knotting in your hair...")
    print("Also your ass hurts.")
    print("Do you pull up your pants?")
    decision = input("> ")
    if "y" in decision:
        print("Pants are probably a good idea.")
        print("You look around...")
        the_woods()
    else:# "n" in decision:
        print("Well, really, who needs pants anyway?")
        the_woods()

start()
#BORING