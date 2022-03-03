import numpy as np
import scipy.stats as sps
import powerlaw
from numpy import random
# from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy
import sys


# graph vertexes size
# number_of_nodes =[0,3,5,10,25,50,100,250,400,500]
# for i in range(len(number_of_nodes)):
#     print (number_of_nodes[i])

# Code from here: https://stats.stackexchange.com/questions/173242/random-sample-from-power-law-distribution
# Power law distribution
from random import random
x_min = 5
alpha = 2.5
x_discrete = []
for i in range(100):
    r = random()
    x_smp = x_min * (1 - r) ** (-1 / (alpha - 1))
    x_discrete.append(round(x_smp))
# print("\nPower law dist")
# print (x_discrete)

# binomial distribution
# Syntax = np.random.binomial(n,p, size=None)
# Parameters: n = trails, p = probability of success, size=output shape
binomial_dist_list =[]
# print("\nBinomial dist")
bin = np.random.binomial(120,0.45,size=50)
for i in range(len(bin)):
    binomial_dist_list.append(round(bin[i]))
# print (binomial_dist_list)

# normal distribution
# Syntax = np.random.normal(loc=0.0, scale=1.0, size=None)
# loc = mean of distribution, scale = standard deviation, size = output size
normal_dist_list =[]
print("\nNormal dist")
x = np.random.normal(40,10,50)
for i in range(len(x)):
    normal_dist_list.append(round(x[i]))
print (sorted(set(normal_dist_list)))
