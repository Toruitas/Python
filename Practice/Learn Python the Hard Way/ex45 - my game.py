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
        players = int("How many players will be joining us?")
        for i in range(players+1): #+1 for dealer, which will be player [-1]
            self.list_of_players.append(Player)

    def play_game(self):
        print("Ok, first round. Dealer deals.")
        for j in range(len(self.list_of_players)):
            self.list_of_players[j].back_in_it()
            print("Player {} has been dealt {}".format(j+1, self.list_of_players[j].show_cards()))
        print("The dealer has been dealt {}".format(self.list_of_players[-1].show_cards()))
        print("Remember, hit CTRL-Z to exit at any time.")

        while True:
            for player in self.list_of_players:
                if player.get_still_playing():
                    player.show_cards()
                    print("Player has {} points.".format(player.points()))
                    if player.points() > 21:
                        print("Player busts!")
                        player.stop_playing()
                    else:
                        choice = input("Hit or stand?")
                        if choice == "Hit":
                            player.hit()
                        else:
                            print("Player stands.")
                            player.stop_playing()

        for player in self.list_of_players:
            if player.points == 21:
                print("Player wins!")
                



class Player(object):
    def __init__(self):
        self.starting_cash = 100
        self.starting_hand = Hand()
        self.starting_hand.build_initial_hand()
        self.still_playing = True

    def show_cards(self):
        print(self.starting_hand.get_hand())

    def hit(self):
        self.starting_hand.add_card()
        print("Player draws a {} card".format(self.starting_hand.get_hand()[-1]))

    def stand(self):
        pass

    def points(self):
        return self.starting_hand.get_points()

    def adjust_bet(self, qty):
        self.starting_cash += qty

    def get_still_playing(self):
        return self.still_playing

    def stop_playing(self):
        self.still_playing = False

    def back_in_it(self):
        self.still_playing = True


class Hand(object):
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

    def add_card(self):
        self.hand += (random.sample(self.deck.keys(),1))

    def build_initial_hand(self):
        self.add_card()
        self.add_card()

    def get_hand(self):
        return self.hand

    def get_points(self):
        self.points = 0
        for card in self.hand:
            if card != "Ace":
                self.points += self.deck[card]
            else:
                value = input("Do you want your Ace to be worth 11, or 1?")
                if value == "11":
                    self.points += self.deck["Ace"[1]]
                else:
                    self.points += self.deck["Ace"[0]]
        return self.get_points()