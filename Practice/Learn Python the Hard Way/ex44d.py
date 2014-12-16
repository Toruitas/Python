__author__ = 'Stuart'

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print('PARENT altered()')

class Child(Parent):
    def override(self):
        print("CHILD override()")


    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()  # calls the super class version of .altered()
        print("CHILD,AFTER PARENT altered()")

class Child2(Parent):
    def __init__(self,stuff):
        self.stuff = stuff
        super(Child,stuff).__init__()

dad = Parent()
son = Child()
print("--")
dad.implicit()
son.implicit()
print("--")
dad.override()
son.override()
print("--")
dad.altered()
son.altered()