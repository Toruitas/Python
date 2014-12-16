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

# bet
# player
# table & spin/ round

class Player(object):
    """
    Player with name, money, game playing
    """

    def __init__(self, name, starting_cash, starting_game):
        self.name = name
        self.money = starting_cash
        self.game = starting_game

    def get_name(self):
        return self.name
    def get_money(self):
        return self.money
    def get_game(self):
        return self.game

    def start_game(self,game):
        playing = Play_a_game(game)


class Table(object):
    """
    A roulette table and all the numbers including 0 (no 00)
    Additional:
    Inside: Straight, Split, Street, Corner, 6-line, trio, basket, top line
    Outside: with reds/blacks, even/odd,1-18/19-36 slots, snake bet, 1-12,13-24,25-36,columns,

    Attributes:
    Table number

    Methods:
    Calculate payout
    Random wheel
    Get available plays
    """

    rules = "Make a bet on a pocket, or a range of pockets. Can currently make only single pocket bets."
    table = #print image of table

    def valid_moves(self):

    def spin_wheel(self):
        import random
        return random.randint(1,36)




class Play_a_game(object):
    """
    Play a game of each game. May include multiple rounds?
    multiple inheritance from the games?
    """

    def __init__(self,game):
        self.game = game

    def get_rules(self,game):
        return game.get_rules

    def make_move(self,game):