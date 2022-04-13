import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

curve=0
bounded = 0

Y=[]
X=[]
for N in range(100,10000):
    for i in range(N):
        x = 1*random.random()        
        y = 3*random.random()        

        if y <= 3*x**2:
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
