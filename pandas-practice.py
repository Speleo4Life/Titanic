# -*- coding: utf-8 -*-
"""
Pandas Practice
"""
import numpy as np
from numpy.random import default_rng
import pandas as pd
from pandas import Series, DataFrame
obj = pd.Series([4,7,-5,])

# Series with index names
obj2 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])

# Read in data
traindf = pd.read_csv('~/Documents/Titanic/train.csv')
traindf.head()
traindf.columns

# Timing: NumPy Arrays vs. Python Lists
my_array = np.arange(1000000)
my_list = list(range(1000000))
%time for _ in range(10): my_array2 = my_array * 2
%time for _ in range(10): my_list2 = my_list * 2

mat = np.arange(10)
# Reshape by ROWs (MATLAB default)
mat.reshape(3,3, order='F') # Think R: 'by rows'
mat.reshape(3,3, order='C') # Think R: 'by columns'

# Constructing a DataFrame
np.tile(np.arange(2019,2021+1,1), 2)
["Milton"] * 3
