# -*- coding: utf-8 -*-
'''
Created on Mon Oct 23 21:15:34 2017

@author: iris_
'''

###Exercise Two of lecture three
#Sample
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
#Script enters an infinite loop and never terminates
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

#Add 'break' to avoid an infinite loop    
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
    else:
        break
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
#Another code whose effect is same as the sample
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    

#Exercise: guess my number
print('Please think of a number between 0 and 100!')

low = 0
high = 100
guessed = False
ans = (low + high)//2

while not guessed:
    print('Is your secret number ' + str(ans) + '?')
    flag = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if flag == 'l':
        low = ans
    elif flag == 'h':
        high = ans
    elif flag == 'c':
        guessed = True
    else:
        print('Sorry, I did not understand your input.')
    ans = (low + high)//2
    
print('Game over. Your secret number was: ' + str(ans))
