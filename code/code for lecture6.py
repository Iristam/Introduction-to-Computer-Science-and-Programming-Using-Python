# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:26:15 2017

@author: iris_
"""

# create an empty dictionary
my_dict = {}

grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

# must base on the key when indexing 
# it will return the value associated with that key
grades['Ana']

# add an entry to the dictionary 
grades['Sylvan'] = 'A'

# test to see if the key is in the dictionary
'Jonh' in grades
'''
output: True
'''
 
# remove an entry
del(grades['Ana'])

# get an iterable that acts like a tuple of all keys
grades.keys()
'''
output: dict_keys(['Ana', 'John', 'Denise', 'Katy'])
'''

# get an iterable that acts like a tuple of all values
grades.values()
'''
output: dict_values(['B', 'A+', 'A', 'A'])
'''


### Exercise

# returns the sum of the number of values associated with a dictionary
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for value in aDict.values():
        result += len(value)
    return result


#  returns the key corresponding to the entry with the largest number of values
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_len = len(max(aDict.values()))
    for key in aDict.keys():
        result = len(aDict[key])
        if result == max_len:
            output = key
            break
    return output

def biggest(aDict):

'''
aDict: A dictionary, where all the values are lists.

returns: The key with the largest number of values associated with it
'''
larg_item = ['',0]
if len(aDict) ==0:
    return None 
for (k,v) in aDict.items():
    if len(v)>larg_item[1]:
       larg_item[0]=k
       larg_item[1]=len(v)

return larg_item[0]

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = sorted(aDict.items(),key=lambda x:len(x[1]))[-1][0]
    return result