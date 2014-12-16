__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/rhrmx/3282012_challenge_32_easy/
lets simulate a roulette wheel!
a program that takes as input your bet, and gives as output how much you won, with the appropriate probability
write a program that will take a players bet and output the resulting spin and payout. try using an american roulette
wheel (which has the 00 slot) to add a slight twist. and try to incorporate as many complex bets as you can to. a
comprehensive list can be found here[1]
http://en.wikipedia.org/wiki/Roulette#Bet_odds_table

Use OOP!!!
"""

def payout(n,bet):
    return (36/n-1)*bet

def play_game(number):
    print('{} \n {}'.format(reds,blacks))
    try:
        if int(number) == rolled:
            return("You won {}".format(payout(1,bet)),payout(1,bet))
        else:
            return("You lost! HAHAHAHA!",-bet)
    except ValueError:
        if number in reds[0] and rolled in reds[1]:
            return("You won {}".format(payout(18,bet)),payout(18,bet))
        elif number in blacks[0] and rolled in blacks[1]:
            return("You won {}".format(payout(18,bet)),payout(18,bet))
        elif number == "even" or number == "evens" and (rolled % 2 == 0):
            return("You won {}".format(payout(18,bet)),payout(18,bet))
        elif number == "odd" or number == "odds" and (rolled % 2 != 0):
            return("You won {}".format(payout(18,bet)),payout(18,bet))
        else:
            return("You lost! HAHAHAHA!",-bet)

def play_validity_test(number):
    """
    gets the player's move, then returns True if valid, False if not
    :param number: user input
    :return: True or False. True if good, False if exit or bad bed.
    """
    try:
        number = int(number)
        if not 0 < number <= 36:
            return (False, number)
        else:
            return (True, number)
    except ValueError:
        if number not in ["reds","red","black","blacks","even","evens","odd","odds","exit"]:
            return False
        else:
            return (True,number)




if __name__ == "__main__":
    import random
    reds = ("reds",[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36])
    blacks = ("blacks", [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35])
    greens = [0]
    money = 100
    keep_playing = True

    while money > 0 and keep_playing:
        number = (input("Pick a number from 1-36, or enter reds, blacks, evens, or odds."))
        bet = int(input("How much do you want to bet?"))
        rolled = random.randint(0,36)

        if play_validity_test(number)[0]:
            print(number,rolled)
            results = play_game(number)
            print(results)
            money += results[1]
        elif not play_validity_test(number)[0]:
            print("That number isn't a valid bet, fool")
        else:
            money -= bet

        continuous = input("Do you want to play again? y/n")
        if continuous == "yes" or continuous == "y":
            print("Great! You currently have {} gold pieces".format(money))
        else:
            print("Thanks for playing, you cashed out {} gold pieces".format(money))
            keep_playing = False
            break

