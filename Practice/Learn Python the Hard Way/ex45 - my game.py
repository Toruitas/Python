__author__ = 'Stuart'


"""
black jack OOP version
need: players, hands, game, dealer
"""

import random
from sys import exit

class Game(object):
    def __init__(self):
        self.list_of_players = []
        players = int(input("How many players will be joining us?"))
        for i in range(players+1):  # +1 for dealer, which will be player [-1]
            self.list_of_players.append(Player())

    def play_game(self):
        print("Ok, first round. Dealer deals.")

        for j in range(len(self.list_of_players[:-1])):  # since dealer is last in list, have to disinclude
            self.list_of_players[j].back_in_it()
            print("Player {} has been dealt {}".format(j+1, self.list_of_players[j].show_cards()))
        print("The dealer has been dealt {}".format(self.list_of_players[-1].show_cards()))
        print("Remember, hit CTRL-Z to exit at any time.")
        at_least_one_still_playing = True  # since we have at least one playing, we set this to true to get the ball rolling

        while at_least_one_still_playing:
            for j in range(len(self.list_of_players[:-1])):
                print("It's player {}'s turn".format(j+1))
                if self.list_of_players[j].get_still_playing():  # player is still playing
                    print(self.list_of_players[j].show_cards())
                    # to avoid getting asked about your ace twice in the if > 21:
                    points = (self.list_of_players[j].points())
                    print(points)
                    if points > 21:
                        print("Player {} busts!".format(j+1))
                        self.list_of_players[j].stop_playing()
                    else:
                        choice = input("Hit or stand?")
                        if "h" in choice:
                            print("Player {} hits and".format(j+1))
                            self.list_of_players[j].hit()
                        else:
                            print("Player {} stands.".format(j+1))
                            self.list_of_players[j].stop_playing()
                else:
                    pass  # player isn't playing anymore

            # We need to break the loop somehow when everybody stands or loses.
            # this part does a check of all the players to see if any are still playing
            # at the end of each movement through the player list above.
            # if all have still_playing set to False, then at_least_... won't reset to True, and while loop stops
            at_least_one_still_playing = False
            for player in self.list_of_players[:-1]:
                if player.get_still_playing():
                    at_least_one_still_playing = True
                else:
                    pass

        # after all the players have stopped playing, says who won and who lost.
        # since it is player vs house, just goes through all and compares to dealer.
        for player in self.list_of_players:
            if self.list_of_players[-1].points() > 21:
                print("Player wins!")
            elif player.points() == 21:
                print("Player wins!")
            elif player.points() > self.list_of_players[-1].points():
                print("Player wins!")
            else:
                print("Player loses")

        answer = input("Play again? y/n")
        if "y" in answer:
            self.play_game()
        else:
            print("Thanks for playing")
            exit(1)


class Player(object):
    def __init__(self):
        self.starting_cash = 100
        self.starting_hand = Hand()
        # self.starting_hand.build_initial_hand()
        self.still_playing = True  # player initialized as playing. No observers here!

    def show_cards(self):
        return self.starting_hand.get_hand()

    def hit(self):
        """
        adds card using the Player's hand object's add_card method, then prints results.
        probably should return instead, but... it is what it is
        """
        self.starting_hand.add_card()
        print("draws a {} card".format(self.starting_hand.get_hand()[-1]))

    def points(self):
        return self.starting_hand.get_points()

    def adjust_bet(self, qty):  # unused for now. May add in betting functionality later.
        self.starting_cash += qty

    def get_still_playing(self):  # returns Player's playing status. If he stands or busts, will be False.
        return self.still_playing

    def stop_playing(self):
        #  works for both standing and busting.
        self.still_playing = False

    def back_in_it(self):
        # used to bring the player back into the game on the next round.
        self.still_playing = True


class Hand(object):
    """
    Has a deck, and builds a hand from a random selection of cards. Assuming multiple deck game, so can have repeats.
    self.hand is a list of card names.
    self.points is recalculated every time, since we add cards to the hand
    """
    def __init__(self):
        self.deck = {
            "Ace": (1,11),
            "King":10,
            "Queen":10,
            "Jack": 10,
            "10":10,
            "9":9,
            "8":8,
            "7":7,
            "6":6,
            "5":5,
            "4":4,
            "3":3,
            "2":2
        }
        self.hand = []
        self.points = 0
        self.add_card()  # deals 2 cards for initial hand instead of using build_initial_hand method
        self.add_card()

    def add_card(self):
        self.hand += (random.sample(self.deck.keys(), 1))

    # def build_initial_hand(self):
    #     self.add_card()
    #     self.add_card()

    def get_hand(self):
        return self.hand

    def get_points(self):
        """
        Should make cards all individual objects with points and suits, to get around repeated asking for each ace's value.
        Pretty sure you can't actually just change that after drawing a second one.
        Could be wrong... but let's be lazy and forget that anyway!
        :return:
        """
        self.points = 0
        for card in self.hand:
            if card != "Ace":
                self.points += self.deck[card]
            else:
                value = input("Do you want your Ace to be worth 11, or 1?")
                if value == "11":
                    self.points += self.deck["Ace"][1]
                else:
                    self.points += self.deck["Ace"][0]
        return self.points


if __name__ == "__main__":
    play_game = Game()
    play_game.play_game()