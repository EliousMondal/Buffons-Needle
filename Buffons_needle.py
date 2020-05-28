'''Author - MD. ELIOUS ALI MONDAL
   Creadted - 28/5/2020'''

import numpy as np
from numpy import random as random
random.seed(5)

def initiate():
    '''Finding a random orientation of the needle'''
    dx = random.uniform(0,1)
    dy = random.uniform(0,1)
    R = np.sqrt(dx**2 + dy**2)
    if R<1:
        return (dx,dy,R)
    else:
        return initiate()

a = float(input('Enter the length of needle : '))
b = float(input('Enter the gap between lines : '))
ntrials = int(input('Enter the number of trials : '))

nhit = 0
for i in range(ntrials):
    x_cen = random.uniform(0,b/2)
    d = initiate()
    x_tip = x_cen - (a/2)*(d[0]/d[2])
    if (x_tip < 0):
        nhit += 1

hit_avg = nhit/ntrials
pi = (2*a)/(hit_avg*b)

print('\u03C0 = ',pi)



