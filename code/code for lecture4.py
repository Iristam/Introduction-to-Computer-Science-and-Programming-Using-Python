# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:38:52 2017

@author: iris_
"""

def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("hi")
    return i%2 == 0

is_even(4)

def square(x):
    """
    x: int or float
    """
    return x**2

square(2)


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2 + b*x + c

# Another version
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    y = a*x**2 + b*x + c
    return y 

# Scope Example
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    x = x + 1
x = 5
h(x)
print(x)


# exercise 4
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)

# iteration vs recursion

def mult_iter(a,b):
    result = 0
    while b > 0:  #iteration
        result += a
        b -= 1
    return result

def mult(a,b):
    if b == 1:   #base case
        return a
    else:
        return a + mult(a, b-1)  #recursive step

#factorial   
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(4))

# exercise for iteration and recursion
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

def recurPower(base, exp):
    '''
    base: int or float.
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp > 0:
        return base * recurPower(base, exp-1)
    else:
        exp = abs(exp)
        return 1/(base * recurPower(base, exp-1))
    
###find the greatest common divisor of two integers 
'''
更相减损法:以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。
继续这个操作，直到所得的减数和差相等为止,即为最大公因数
'''
#iteration
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while a != b:
        if a > b:
            a -= b 
        else:
            b -= a
    return a 
    

'''
辗转相除法：
用较小数除较大数，再用出现的余数（第一余数）去除除数，再用出现的余数（第二余数）去除第一余数，
如此反复，直到最后余数是0为止。
如果是求两个数的最大公因数，那么最后的除数就是这两个数的最大公因数
'''
#iteration
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''  
    while a != b:
        if a > b:
            r = a % b 
            a = b 
            b = r
            if r == 0:
                return a
        else:
            a, b = b, a

#recursion
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        if a % b == 0:
            return b 
        else:
            return gcdRecur(b, a%b)
    else:
        return gcdRecur(b, a)
    
# Hanoi    
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)  #multiple recursive calls inside the body of a function
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

# exercise 
# 使用二分法判断某字符串是否含有某个字母
# 该字符串按照字母顺序排列
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '' or (len(aStr) == 1 and char != aStr):
        return False
    else:
        middle = len(aStr)//2
        if char == aStr[middle]:
            return True
        else:
            if char > aStr[middle]:
                return isIn(char, aStr[middle:])
            else:
                return isIn(char, aStr[:middle])
            
# 参考答案
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])
             


#########################################
     
        
# Grader of week2
# sum the area and square of the perimeter of the regular polygon
def polysum(n, s):
    '''
    n: number of sides
    s: length of each side 
    
    return: sum the area and square of the perimeter of the regular polygon
    面积与周长平方之和
    '''
    import math
    perimeter = n * s
    area = 0.25 * n * s**2 / math.tan(math.pi/n)
    result = area + perimeter**2
    return round(result,4) 