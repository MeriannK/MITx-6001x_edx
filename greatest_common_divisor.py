# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:52:27 2017

@author: Марианна
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a <= b:
        i = a
        while a % i != 0 or b % i != 0:
            i -= 1
    else:
        i = b
        while a % i != 0 or b % i != 0:
            i -= 1
    return i

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
       a, b = b, a
    if b == 0:
        return a   
    elif a > b:
        return gcdRecur(b, a%b)


print(gcdIter(216, 198))
print(gcdIter(60, 54))
print(gcdIter(27, 54))
print("----------")
print(gcdRecur(156, 216))
print(gcdRecur(40, 56))
print(gcdRecur(27, 30))