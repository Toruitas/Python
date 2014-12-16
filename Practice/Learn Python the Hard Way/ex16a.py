__author__ = 'Stuart'

from sys import argv

script, file = argv

print("Remember that file you rewrote earlier?")
remember = input("> ")
if remember == "Y":
    print("Ok good.")
else:
    print("Well, let's remind you.")
    target = open(file)
    print(target.read())
    target.close()
    print("Add something to it Ba!")
    target = open(file,"a")
    target.write(input("What do you want to say?"))
    target.close()
    print("Sweet.")