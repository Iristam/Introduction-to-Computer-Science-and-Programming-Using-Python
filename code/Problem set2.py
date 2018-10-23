# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:22:14 2017

@author: iris_
"""

# Problem1
'''
若每月仅还信用卡最低还款额，计算一年后该信用卡的未偿还余额

变量解释：
1.balance - the outstanding balance on the credit card

2.annualInterestRate - annual interest rate as a decimal

3.monthlyPaymentRate - minimum monthly payment rate as a decimal

'''

'''
    inputs: 
        balance: 一开始的未偿还余额
        annualInterestRate：利息的年化率
        monthlyPaymentRate: 最低还款比例
    
    returns:balance = (balance - balance * monthlyPaymentRate) * (1+annualInterestRate/12)
        remaining balance
    '''
for i in range(1,13):
    result = (balance - balance * monthlyPaymentRate) * (1+annualInterestRate/12)
    balance = round(result, 2)
print("Remaining balance: ", balance)




'''
Problem 2:
    
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.
The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.
'''

# initialize
month = 0
monthlyInterestRate = annualInterestRate / 12
minPayment = 10
initialBalance = balance

# balance of each month within a year
def pay(month, balance, minPayment, monthlyInterestRate):
    while month < 12:
        unpaidBalance = balance - minPayment
        balance = unpaidBalance + unpaidBalance * monthlyInterestRate
        month += 1
    return balance
        
# if we cannot pay off a credit card balance within 12 months, increase minPayment
while pay(month, balance, minPayment, monthlyInterestRate) > 0:
    balance = initialBalance
    minPayment += 10
    month = 0
    pay(month, balance, minPayment, monthlyInterestRate)
print("Lowest Payment: ", str(minPayment))
    

'''
Problem 3:
use the bisection method to calculate the lowest payment
'''
# initialize
balance = 320000
annualInterestRate = 0.2
initialBalance = balance
month = 0
monthlyInterestRate = annualInterestRate / 12
low = balance / 12
high = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
minPayment = (low + high) / 2
epsilon = 0.01

# balance of each month within a year
def pay(month, balance, minPayment, monthlyInterestRate):
    while month < 12:
        unpaidBalance = balance - minPayment
        balance = unpaidBalance + unpaidBalance * monthlyInterestRate
        month += 1
    return balance

while abs(balance) >= epsilon:
    balance = initialBalance
    month = 0 
    balance = pay(month, balance, minPayment, monthlyInterestRate)
    if balance > 0:
        low = minPayment
    else:
        high = minPayment
    minPayment = (low + high) / 2
minPayment = round(minPayment, 2)
print("Lowest Payment: ", str(minPayment))

        
    
    
    