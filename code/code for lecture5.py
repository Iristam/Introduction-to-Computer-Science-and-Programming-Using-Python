# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:15:28 2017

@author: iris_
"""

# tuples can be used to return more than one value from a function 
def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q, r)
(quot, rem) = quotient_and_remainder(4,5)



# Exercise: odd tuples
'''
Write a procedure called oddTuples, which takes a tuple as input, 
and returns a new tuple as output, where every other element of the input tuple is copied, 
starting with the first one.
'''
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oddTuples = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            oddTuples += (aTup[i],)
    return oddTuples

oddTuples = oddTuples(aTup)

# 参考答案
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]

def applytoEach(L, f):
    '''
    assume L is a list, 
    f a function mutates L by replacing each element, e, of L by L(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
        
# lists of functions
def applyFuns(L, x):
    for f in L:
        print(f(x))
 

L1 = [1, 28, 36]
L2 = [2, 57, 9]
list(map(min, L1, L2))
'''
output: [1, 28, 9]       
'''



# exercise: apply to each
## the first one
def abs_x(x):
    return abs(x)

applyToEach(testList, abs_x)

## the second
def plus_x(x):
    return x + 1

applyToEach(testList, plus_x)

## the third
def square(x):
    return x**2

applyToEach(testList, square)

