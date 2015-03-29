__author__ = 'Stuart'

"""
oxox_data is the data module for a tic-tac-toe game.
It saves and restores a game board. The functions are:
    saveGame(game) -> None
    restoreGame() ->game
Note that no limits are placed on the size of the data.
The game implementation is responsible for validating
all data in and out.
"""

import os.path
GAME_FILE = ".oxogame.dat"

def _getPath():
    """
    Helper function.
    Return valid path for data file.
    Tries to use user's home folder. defaults to cwd.

    funcs not intended to be called by module users have leading underscore.
    :return: str
    """
    try:
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    return game_path

def saveGame(game):
    """
    Saves game obj in data file in user's home folder.
    No checking is done on the input, which is expected
    to be a list of characters
    :param game: game object to save
    :return: none
    """

    path = os.path.join(_getPath(), GAME_FILE) #game_file
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)

def restoreGame():
    """
    Restores game from data file.
    The game obj is list of chars
    :return: game object
    """

    path = os.path.join(_getPath(), GAME_FILE)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)

def test():
    print("Path = ", _getPath())
    saveGame(list("XO  XO OX"))
    print(restoreGame())

if __name__ == "__main__":
    test()