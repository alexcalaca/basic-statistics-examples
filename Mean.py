# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
Reach me at alexcalaca@gmail.com
"""

""""
The mean is the average of the numbers.
It is easy to calculate: add up all the numbers, then divide by how many numbers there are.
"""

import numpy as np

#Create an array of numbers
numbers = [0, 2, 4, 6, 8, 10]

value = np.mean(numbers)

print ("The mean is %s" %value)