__author__ = 'stu'

"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock"""

def getHand():
    hand = (raw_input("Rock, paper, scissors? Or 'quit' to quit the game. ")).lower()
    if (hand != "rock") and (hand != "paper") and (hand != "scissors") and (hand != 'quit'):
        print("Sorry, that isn't a valid play, throw another one!")
        getHand()
    else:
        return hand

def compareHands(userA,userB):
    if userA == "rock" and userB == "scissors" or userA == "scissors" and userB == "paper"or userA == "paper" and userB == "rock":
        return "UserA wins with " + userA
    elif userA == 'quit' or userB == 'quit':
        return "Surrender!"
    elif userA == userB:
        return playGame()
    else: 
        return "User B wins with " + userB

def playGame():
    userA = getHand()
    userB = getHand()
    print compareHands(userA,userB)
    
print "Let's play a game..."
playGame()