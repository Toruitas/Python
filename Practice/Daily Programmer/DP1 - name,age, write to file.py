"""
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later..
https://gist.github.com/layingincouch/2762092
http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
"""

class Person(object):
    name = ""
    age = 0
    redditName = ""

    def __init__(self, name, age, redditName):
        self.name = name
        self.age = age
        self.redditName = redditName

    def __str__(self):
        return self.name

def make_person(name, age, redditName):
    person = Person(name, age, redditName)
    return person

def report(file):
    with open(file, 'r') as fil:
        for line in fil:
            print(line)
    #file = open(file, 'r') #r read only, w write only, a append (any data added directly to end), r+ for r&w. r assumed
    #file.readlines(-1)
    #file.close()

def log(person,file):
    file = open(file, 'a') #r read only, w write only, a append (any data added directly to end), r+ for r&w. r assumed
    file.write("This user's name is " + person.name + ", age is " + person.age + " years old, and username is " + person.redditName+".\n")
    file.close()

if __name__ == '__main__':
    people = {}
    stillLogging = True
    file = "DP1.txt"
    while stillLogging == True:
        keepGoing = input("Do you have someone to log? Y/N").lower()
        if keepGoing == "n":
            stillLogging = False
            break
        elif keepGoing == "y":
            name = input("What is the person's name?")
            age = input("What about age?")
            username = input("What is this person's username?")
            people[name] = make_person(name, age, username)
        else:
            print("Say again?")

    for key in people:
        log(people[key], file)

    report(file)