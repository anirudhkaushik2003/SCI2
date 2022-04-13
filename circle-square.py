import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

N = 10000
circle = 0
square = 0
X = []
Y = []
for j in range(0, 1000):
    for i in range(0, N):
        x = random.random()
        y = random.random()
        l = x * x + y * y
        l = l ** 0.5
        if l <= 1.0:
            circle += 1
        square += 1
    pi = circle/square
    pi = pi*4
    X.append(pi)
    Y.append(j)

plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(Y, X, color="red")
plt.show()
