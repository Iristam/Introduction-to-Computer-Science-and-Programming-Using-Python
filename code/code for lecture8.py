# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:45:05 2017

@author: iris_
"""

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")

'''
exceptions raised by any statement in body of try are handled by the except statement 
and excutions continues after the body of the except statement.
'''
        
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")

'''
else:
    body of this is executed when execution of associated try body completes with no exceptions
finally:
    body of this is always executed after try, else and except clauses, even if they raised another
    error or executed a break, continue or return
'''    

while True:
    try: 
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")

# Exercise: simple divide
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
    print("okay")
    
# assertion
def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)
'''
if given an empty list, the length of the grades is 0, the "not" statement is false.
since that is false, assert, then, will stop the execution, 
and throw an assert error -- throw an assert exception with that message printed out.

functions ends immediately if assertion not met.
'''

