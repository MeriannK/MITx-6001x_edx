# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:58:22 2017

@author: Марианна
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr)
    mid = int((low + high)/2)
    if len(aStr) <= 1:
        if aStr == char:
            return True
        else:
            return False
        return False
    elif aStr[mid] == char:
        return True
    else:
        if aStr[mid] < char:
            low = mid
            return isIn(char, aStr[low:high])
        else:
            high = mid
            return isIn(char, aStr[low:high])
        
print(isIn('a', ''))
print(isIn('b', 'bijlprtuuuvwwwz'))