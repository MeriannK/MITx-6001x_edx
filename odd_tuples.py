# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:14:38 2017

@author: Марианна
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new_tup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            new_tup = new_tup + (aTup[i],)
    return new_tup

aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))