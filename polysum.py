# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:03:17 2017

@author: Марианна
"""

import math

def polysum(n, s):
    '''
    Regular Polygons: polysum
    
    Take: 2 arguments, 'n' and 's'.

    A regular polygon has 'n' number of sides. Each side has length 's'.

    * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    * The perimeter of a polygon is: length of the boundary of the polygon

    Return: the sum, rounded to 4 decimal places.
    '''
    area = (0.25*n*s**2)/(math.tan(math.pi/n)) # calculate area
    perimeter = s * n #calculate perimeter
    
    return round(area + perimeter**2, 4) #return rounded sum