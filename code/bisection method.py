# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:31:39 2017

@author: iris_
"""
##find the square root of x by using bisection method

#when x > 1
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))

# when 0 < x < 1
x = 0.01
epsilon = 0.01
numGuesses = 0
low = 0.0
high = 1/x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))

#final version: find the square root of x which is real number 
x = 0.01
epsilon = 0.01
numGuesses = 0
if x > 0:
    if abs(x) >= 1:
        low = 0.0
        high = x
    else:
        low = 0.0
        high = 1/x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))
else:
    print("Negative numbers have no square root")


##find the cube root of x by using bisection method
x = -54
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (low + high)/2

while abs(ans**3 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if abs(ans**3) < abs(x):
        low = ans
    else:
        high = ans 
    ans = (high + low)/2
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to cube root of " + str(x))

    