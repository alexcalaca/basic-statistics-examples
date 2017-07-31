# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
Reach me at alexcalaca@gmail.com
"""

"""
From a python dictionary to a Pandas Data Frame with pandas series values
"""

import pandas as pd

#Create a python dictionary with pandas series values
dictionary = {
        'name': pd.Series(['Mark', 'Allen', 'Josh'], index=['a', 'b', 'c']),
        'city': pd.Series(['NYC', 'RJ', 'LA'], index=['a', 'b', 'c']),
        'age': pd.Series([29, 39, 51], index=['a', 'b', 'c']),
        'ticket': pd.Series([30.25, 60.50, 60.50], index=['a', 'b', 'c']),
        'bought?': pd.Series([True, False, True], index=['a', 'b', 'c'])
        }


#Assign the pandas data frame to a variable
df = pd.DataFrame(dictionary)

print(df)