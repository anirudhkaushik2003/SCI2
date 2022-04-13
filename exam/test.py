import autograd.numpy as np
from autograd import hessian
import exam4

g = lambda w:  4* epsilon* (((sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 6)+((sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 6))


exam4.solve_fw()
ddf = hessian(g)
    
print(ddf(xx).diagonal(axis1=1, axis2=2))