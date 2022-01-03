#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 20:50:27 2021

@author: ray.macneil
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt


train = pd.read_csv('/Users/ray.macneil/Documents/Titanic/train.csv')

# Get summary of data frame, think str() in R
train.info()

# Get counts for a categorical variable
pd.value_counts(train.Embarked)


# Create a Bar Plot representing the 
x = ['Southampton', 'Cherbourg', 'Queenstown']
y_emb_pct = np.array((pd.value_counts(train.Embarked) / sum(pd.value_counts(train.Embarked))) * 100)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y_emb_pct)
ax.set_ylabel('Passengers (%)')
ax.set_xlabel('Embarkment Location')
ax.set_title('Titanic Passenger Composition by Location of Embarkment')
plt.show()

# Parse survival by passenger class
first_class = pd.value_counts(train[train['Pclass'] == 1]['Survived'] == 1)
second_class = pd.value_counts(train[train['Pclass'] == 2]['Survived'] == 1)
third_class = pd.value_counts(train[train['Pclass'] == 3]['Survived'] == 1)


# Organize in DataFrame
dat = {'class': ['First', 'Second', 'Third'],
       'died': [first_class[0], second_class[0], third_class[0]],
       'survived': [first_class[1], second_class[1], third_class[1]],
       'total': [sum(first_class), sum(second_class), sum(third_class)]}
dat = pd.DataFrame(dat)

# Get column marginal sums for 'died', 'survivev', and 'total'
sums = dat.sum()[1:]
# Compute expected values
exp_die = (sums.died * dat.total) / sums.total
exp_suv = (sums.survived * dat.total) / sums.total

# It might be more intutitve to look at the contingency table transcribed
# You can accomplish this with simple syntax built into pandas
tdat = dat.T

# Verify totals
sum(tdat[0][1:3]) == tdat.loc['total'][0]
sum(tdat[1][1:3]) == tdat.loc['total'][1]
sum(tdat[2][1:3]) == tdat.loc['total'][2]







