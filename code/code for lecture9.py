# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:03:28 2017

@author: iris_
"""

# how to create an instance of object
# use a special method called __init__ to initialize some data attributes
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5        
# print representation of an object 
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    
c = Coordinate(3,4)
origin = Coordinate(0,0)

# how to use a method from the Coordinate class

# conventional way 
# if I'm using an instance to get the method, Python automatically uses that instance as first argument.
print(c.distance(origin))

# equivalent to 
# if I'm using the class to get the method, u need to provide both arguments,
# because Python doesn't know which is the instance that you want to use
print(Coordinate.distance(c,origin))

# use isinstance() to check if an object is an Coordinate
print(isinstance(c, Coordinate))



# Exercise
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
    
    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        #initialize
        commonValue = intSet()
        for var in self.vals:
            if other.member(var):
                commonValue.insert(var)
        return commonValue
    
    def __len__(self):
        return len(self.vals)


#s = intSet()
#print(s)
#s.insert(3)
#s.insert(4)
#s.insert(3)
#print(s)
#s.member(3)
#s.member(5)
#s.insert(6)
#print(s)
#s.remove(3)
#print(s)
##s.remove(3)