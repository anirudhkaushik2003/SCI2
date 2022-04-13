

import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np
import sys

curve=0
bounded = 0
e = 2.718281828459045

Y=[]
X=[]
for N in range(100,1000):
    for i in range(N):
        x = random.uniform(-1*sys.maxsize,sys.maxsize)        
        y = random.uniform(-1*sys.maxsize,sys.maxsize)        

        if y <= e**(-1*x**2):
            curve +=1
        bounded += 1
        
    integral = curve/bounded*3
    X.append(N)
    Y.append(integral) 
    
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(X, Y, color="red")
plt.show()