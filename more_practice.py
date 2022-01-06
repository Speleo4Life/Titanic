# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
iris_data = pd.read_csv('~/Documents/Titanic/iris.csv')
my_sequence = np.arange(2,81,2)
my_new_sequence = np.reshape(my_sequence, [8,5], order = 'F')
mydf = pd.DataFrame(data = my_new_sequence, columns = ['V1', 'V2', 'V3', 'V4', 'V5'])
mydf['Groups'] = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']

# Basic summary statistics for a column
mydf.V1.describe()

# Basic summary statistics for specific multiple columns
mydf[['V1', 'V2']].describe()

# Basic summary statistics for a variable based on group membership
mydf.groupby('Groups')['V2'].describe()
