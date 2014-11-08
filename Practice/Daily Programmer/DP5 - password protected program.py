__author__ = 'Stuart'
"""
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)

http://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/
"""



def passchecker(user,password):
    passfile = open("password.txt.txt","r")
    for line in passfile:
        try:
            fileuser, passworde = line.split()
        except ValueError:
            continue
        if user != fileuser:
            continue
        if password == passworde:
            passfile.close()
            return True
    passfile.close()
    return False

def passhacker(program):
    """
    reads a .py program for a file IO and then parses that IO -- how?!
    :param program:
    :return:
    """


if __name__ == "__main__":
    import getpass
    user = input("Enter Username: ")
    #password = getpass.getpass()
    password = input("Password: ")
    if passchecker(user, password):
        print("You have access")
    else:
        print("Access denied")