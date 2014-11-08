__author__ = 'Stuart'
"""
Random password generator
default 8 characters, but user can define what length of password they want

"""

def password_assembler(length=8):
    """
    Takes user-defined length (default 8) and generates a random password
    :param length: default 8, otherwise user-defined
    :return: password of length length
    """
    password = ""
    for i in range(length+1):
        password += random_character()
    return password

def random_character():
    """
    random character generator
    :return: random character
    """
    characters = string.printable
    return random.choice(characters)




if __name__ == "__main__":
    import random
    import string
    length = input("What length password would you like? Default is 8")
    print(password_assembler(int(length)))