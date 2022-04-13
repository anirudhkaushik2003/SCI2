
import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np
from math import pi

#let amplitude = 5
#let angular freq = 2
#let mass = 3
A = 5
w = 2
m = 3
# H = p^2/2m + 1/2kx^2
#diff eq => md^2x/dt + w^2x = 0 where w = (k/m^)0.5
# x = Acoswt
# p = mdx/dt = -Awsinwt

t = np.linspace(0,pi,200)

#q3- time series of x and p
#plt.plot(t,A*np.cos(w*t),color='red')
#plt.plot(t,-1*A*m*w*np.sin(w*t),color='green')
#plt.xlabel('t')
#plt.ylabel('p')

#q4- trajectory in phase space
plt.plot(A*np.cos(w*t),-m*1*A*w*np.sin(w*t),color='blue')
plt.xlabel('x')
plt.ylabel('p')

#q5- kinetic energy = 0, system starts at a given initial x, show how system evolves on the energy surface
# dU = -Fdx = kxdx integrating from 0 to x we get U(x) = 1/2kx^2 = 1/2 A^2 cos^2(wt+phi)
# if we start at x0, i.e an extreme position we get A=x0, at t=0 x = x0, so phase difference will be 0
# p = -mAwsinwt = 0 at t= 0
# we plot U(x) vs x and kinetic energy T(x) = p^2/2m vs x
# plt.plot(t, ((A*np.cos(w*t)**2)*(w**2)*m/2),color='blue') #potential energy vs time
# plt.plot(t,((1*A*w*np.sin(w*t))**2)*m/2,color='red') #kinetic energy vs time

# x=(A*np.cos(w*t))
# KE = ((1*A*w*np.sin(w*t))**2)*m/2
# plt.plot(x,1/2*(w**2)*m*(x**2),color="red") #potential energy vs x
# plt.plot(x,KE,color="blue") #kinetic energy vs x
# plt.xlabel('x')
# plt.ylabel('U(x) T(x)')

plt.show()