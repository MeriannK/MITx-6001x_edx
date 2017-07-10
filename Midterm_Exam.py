# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:32:34 2017

@author: Марианна
"""



def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    trig_num = 0
    for i in range(1, k+1):
        trig_num += i
        if trig_num == k:
            return True
        if trig_num > k:
            return False
print(is_triangular(1))

'''
Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. If s = "a" then print_without_vowels will print the empty string .
'''
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    s_without_vowels = s
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in s:
        if letter in vowels:
            s_without_vowels = s_without_vowels.replace(letter, '')
    print(s_without_vowels)
s = "This Is great!"
print_without_vowels(s)

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    odd_ls = []
    for num in L:
        count = L.count(num)
        if count % 2 != 0:
            odd_ls.append(num)
    if len(odd_ls) > 0:
        return max(odd_ls)

print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,9,3]))

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    d_invert = {}
    new_items = []
    items = d.items()
    for tup in items:
        new_items.append(tuple((tup[1], tup[0])))
    for i in new_items:
        d_invert.setdefault(i[0],list()).append(i[1])
    for key in d_invert:
        d_invert[key].sort()           
    return d_invert
d = {1:10, 2:20, 3:30, 4:30}
dict_invert(d)
print(dict_invert(d))
print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
        
    def mult(x):
        k = len(L) - 1
        polysum = 0
        for number in L:
            polysum += number * x ** k   
            k -= 1
        return polysum
    return mult
    
    
print(general_poly([1, 2, 3, 4])(10))


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    max_item = None
    max_count = 0
    if len(L1) != len(L2):
        return False
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    for i in range(len(L1)):
        if L1.count(L1[i]) != L2.count(L1[i]):
            return False
    for j in L1:
        count = L1.count(j)
        if count > max_count:
            max_count = count
            max_item = j
    return (max_item, max_count, type(max_item))
    
    

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
print(is_list_permutation(L1, L2))
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))