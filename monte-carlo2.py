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
        x = random.random()        
        y = random.random()
        z = random.random()        

        if z <= (x**2)*y:
            curve +=1
        bounded += 1
        
    integral = curve/bounded
    X.append(N)
    Y.append(integral) 
    
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(X, Y, color="red")
plt.show()
