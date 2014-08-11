_author_ = 'stu'

"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (_Hint: remember to use the user input lessons from the very first exercise
Extras:
Keep the game going until the user types "exit"
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

number = str(random.randint(1,10))
guessed = False
numGuesses = 0

while guessed == False:
    userGuess = raw_input("What's your guess, 1-10?").lower()
    if userGuess == "exit":
        break
    elif userGuess == number:
        guessed = True
        numGuesses +=1
        print("You got it after " + str(numGuesses) + " guesses! The number was "+ number+".")
    else:
        numGuesses +=1
        if int(number)>int(userGuess):
            print("Your guess is too low, try again.")
        else: #if int(number)<int(userGuess):
            print("Your guess is too high, try again.")