__author__ = 'stu'

"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

while loop version"""

def playGame():
    winsA = 0
    winsB = 0
    while winsA <3 and winsB <3:
        userA = raw_input("Rock, paper, scissors, user A? ").lower()
        userB = raw_input("Rock, paper, scissors, user B? ").lower()
        if compareHands(userA, userB) =='a':
            winsA +=1
        elif compareHands(userA, userB) =='b':
            winsB +=1
        elif compareHands(userA, userB) =='tie':
            print("Tie, go again!")
        else:
            print("That doesn't make sense, try again!")
        print("A has "+ str(winsA) +" wins")
        print("B has "+ str(winsB) +" wins")
    if winsA > winsB:
        return "Player A wins!"
    else:
        return "Player B wins!"
        
def compareHands(userA,userB):
    if userA == "rock" and userB == "scissors" or userA == "scissors" and userB == "paper"or userA == "paper" and userB == "rock":
        return "a"
    elif userA == userB:
        return "tie"
    else: 
        return "b"

print playGame()