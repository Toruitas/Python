__author__ = 'Stuart'

from sys import argv

script, user_name, sex = argv
prompt = '> '

print("Hi {}, I'm the {} script.".format(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Hey, {}, what do you like to bang?".format(sex))
target = input(prompt)

print("""
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
Oh, and you like to bang {}.
""".format(likes, lives, computer,target)
)