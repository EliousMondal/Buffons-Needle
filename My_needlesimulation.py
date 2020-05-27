'''Author - MD. ELIOUS ALI MONDAL
   Created - 28/5/2017'''

#simulation of needle falling on a plane and estimating the value of pi
from math import *
import time
import random
start_time = time.process_time()
random.seed(5)
n = int(input('Enter the number of needles to be stimulated : '))
x1 = []
y1 = []
for i in range(n):
    x1.append(random.uniform(-10,10))
x1.sort()
for i in x1:
    y1.append(random.uniform(-10,10))
x2 = []
y2 = []
for i in range(len(x1)):
    g = random.uniform(0,2*pi)
    m = x1[i]+1/sqrt(1+tan(g)**2)

    l = x1[i]-1/sqrt(1+tan(g)**2)
    x2.append(random.choice([m,l]))
    p = y1[i]+tan(g)/sqrt(1+tan(g)**2)

    t = y1[i]-tan(g)/sqrt(1+tan(g)**2)
    y2.append(random.choice([p,t]))
#Let the number of needles falling in between space = s
s = 0

import pylab
pylab.figure(1)
for i in range(-10,11):
    pylab.plot([i,i],[-10,10],color = 'black')
for i in range(len(x1)):
    if int(max(x1[i],x2[i])) == 0 and int(min(x1[i],x2[i])) == 0:
        if (x1[i] > 0 and x2[i] > 0) or (x1[i] < 0 and x2[i] < 0):
            pylab.plot((x1[i],x2[i]),(y1[i],y2[i]),color = 'blue')
            s = s + 1
        else:
            pylab.plot((x1[i],x2[i]),(y1[i],y2[i]),color = 'red')
    else:        
        if  int(max(x1[i],x2[i]))-int(min(x1[i],x2[i])) == 0:
            pylab.plot((x1[i],x2[i]),(y1[i],y2[i]),color = 'blue')
            s = s + 1
        else:
            pylab.plot((x1[i],x2[i]),(y1[i],y2[i]),color = 'red')

end_time = time.process_time()
probability = s/n
pie = 2/(1-probability)
print('The probability of neddle falling in space between is ',probability)
print('The value of pi is ',pie)
pylab.title(('n = ',n,' Probability', probability,' Pi',pie))
print('Time taken is',end_time-start_time,'seconds')
pylab.show()    

