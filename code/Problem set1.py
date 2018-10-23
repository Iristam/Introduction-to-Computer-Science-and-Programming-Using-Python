# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:28:35 2017

@author: iris_
"""
#Problem 1
s = 'azcbobobegghakl'
numVowel = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowel += 1
print("Number of vowels: " + str(numVowel))

#Problem 2
num = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        num += 1   
print("Number of times bob occurs is: " + str(num))

#Problem 3 
s = 'azcbobobegghakl'
for i in range(len(s)):
    j = i 
    while j < len(s) and s[j] <= s[j + 1]:
        j += 1 
    if j - i > 1:
        break
print("Longest substring in alphabetical order is: ", s[i:j+1])

##判断1：后一个字符比前一个字符大
##判断2：字符串的长度
# initialization
s = 'azcbobobegghakl'
s = s + '0'
tmp = ''
longest = ''

for i in range(1,len(s)):
    tmp += s[i-1]
    if s[i-1] > s[i]:
        if len(tmp) > len(longest):
            longest = tmp
        tmp = ''

# Termination: the for loop reaches the last char of s 
        
print(longest)


s = 'azcbobobegghakl'
tmp = ''
longest = ''
flag = ''
for letter in s:
    if letter >= flag:
        tmp += letter
    else:
        tmp = letter
    if len(tmp) > len(longest):
        longest = tmp
    flag = letter
    print("letter: ", letter, "flag: ", flag, "tmp: ", tmp, "longest: ", longest)
print(longest)

s = 'azcbobobegghakl'
tmp = s[0]
longest = s[0]
for i in range(1,len(s)):
    if s[i-1] <= s[i]:
        tmp += s[i]
    else:
        tmp = s[i]
    if len(tmp) > len(longest):
        longest = tmp
    print(i, "tmp: ", tmp, "longest: ", longest)
print(longest)


