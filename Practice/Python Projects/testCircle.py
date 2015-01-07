__author__ = 'Stuart'

"""
keep in mind, packages need to have one-word names

self.__radius -- the two underscores make things private
"""

class Circle1:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else:
            raise ValueError("Value must be positive")

    def area(self):
        return 3.14159 * (self.__radius ** 2)

class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    def __setRadius(self,newValue):
        if newValue >=0:
            self.__radius = newValue
        else:
            raise ValueError("Value must be positive")
    radius = property(None, __setRadius)
# = property(read=None, write=none, delete =none)
# This code takes as arguments a set of functions for read, write, and delete (as well as a documentation
# string). The default value of each is None . In this case you created the radius property with a None read
# function but with the (now private) __setRadius() method as a write function. The other values were
# left at their default of None . The result was that radius could be accessed by the user as if it were a public
# data attribute when assigning a value but, under the covers, Python called the _ setRadius() method.
# Any attempt to read (or delete) the attribute would be ignored because the action gets routed to None .
# Makes it so that the user can write to the radius but not read it

    @property  # doing it like this is a shortcut to make something read only
    def area(self):
        return 3.14159 * (self.__radius**2)
