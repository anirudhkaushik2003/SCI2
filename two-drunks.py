import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

X = []
Y = []
a = []
b = []
MeanDisp = []
Disp = 0
N = 50
l = 0
a.append(0)
b.append(0)
for N in range(0,100):
    for j in range(1000):
        for i in range(0,N):
            a.append(random.choice([1,-1]))
            b.append(random.choice([1,-1]))
        a = np.array(a)
        b = np.array(b)
        x = a.sum()
        Disp += x
        y = b.sum()
        if x == y:
            l += 1
        a = []
        b = []
    X.append(l/1000)
    MeanDisp.append(x/N)
    Y.append(N)
    l = 0

A=[]
B =[]

A.append(1.0)
B.append(0)


for N in range(1,100):
    prob = factorial(2*N,exact=True)
    prob2 = 2**N
    prob2 = prob2*factorial(N,exact=True)
    prob2 = prob2*prob2
    A.append(prob/prob2)
    B.append(N)
    if N == 1:
        print(prob/prob2)
            
    
plt.title("Line graph")
plt.xlabel("N")
plt.ylabel("Probability")
plt.plot(Y, X, color ="red")
plt.plot(B,A,color="blue")
plt.plot(Y,MeanDisp,color="green")
plt.legend(["random walk simulated","actual probability","Mean displacement"])
plt.show()

