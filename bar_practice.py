#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 01:35:50 2022

@author: ray.macneil
"""

import numpy as np
import matplotlib.pyplot as plt

dat = {2015:{'CS':30, 'IT':40, 'E&TC':35}, 2016:{'CS':25, 'IT':23, 'E&TC':22}, 
       2017:{'CS':50, 'IT':51, 'E&TC':45}, 2018:{'CS':20, 'IT':16, 'E&CT':19}}
# dat = [[30, 25, 50, 20],
# [40, 23, 51, 17],
# [35, 22, 45, 19]]
X = np.arange(4)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.bar(X + 0.00, dat[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, dat[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, dat[2], color = 'r', width = 0.25)
