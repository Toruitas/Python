__author__ = 'Stuart'

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print('OTHER altered()')

class Child(object):

    def __init__(self):
        #Child has an assistant object
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()  # similar to our other Super calls
        print("CHILD, AFTER OTHER ALTERED()")

son = Child()
son.implicit()
son.override()
son.altered()