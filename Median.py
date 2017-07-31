# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
Reach me at alexcalaca@gmail.com
"""

""""
The "median" is the "middle" value in the list of numbers.
Your numbers have to be listed in numerical order from smallest to largest.
Python does that for you.
"""

import numpy as np

#Create an array of numbers
numbers = [10, 4, 8, 6, 0, 2]

value = np.median(numbers)

print ("The median is %s" %value)