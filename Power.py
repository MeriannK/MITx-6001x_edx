# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:41:13 2017

@author: Марианна
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    res = 1
    for n in range (1, exp + 1):
        res *= base
    return res


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)
    
print(iterPower(0.9, 0))
print(iterPower(-6.04, 1))
print(iterPower(3.56, 10))
print('---------------------')
print(recurPower(3.41, 2))
print(recurPower(3.56, 10))
print(recurPower(-7.55, 5))