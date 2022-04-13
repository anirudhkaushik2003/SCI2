import exam
import exam2
import autograd.numpy as np
from autograd import hessian





import numpy as np
import numdifftools as nd
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as dt
from sklearn.model_selection import train_test_split
from autograd import grad

epsilon = 0.238
sigma = 3.4



def gradient_descent(
    max_iterations,
    threshold,
    w_init,
    obj_func,
    grad_func,
    index,
    extra_param=[],
    learning_rate=0.05,
    momentum=0.8,
):

    w = w_init
    w_history = []   
    w_history.append(w)
    f_history = obj_func(w)
    delta_w = np.zeros(w.shape)
    i = 0
    diff = 1.0e10

    while i < max_iterations and diff > threshold:
        delta_w = -learning_rate * grad_func(w) + momentum * delta_w
        w = w + delta_w
        # store the history of w and f
        w_history.append(w)
        f_history = np.vstack((f_history, obj_func(w)))

        # update iteration number and diff between successive values
        # of objective function
        i += 1
        diff = np.absolute(f_history[-1] - f_history[-2])
        plt.subplot(3, 4, index)
            
        plt.plot(i,obj_func(w), 'bo')
        
    return np.array(w_history), f_history





# Pts are 2D points and f_val is the corresponding function value


# Objective function
def f(w):
    return 4* epsilon* (((sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 6)+((sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 6))
    
g = lambda w:  4* epsilon* (((sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[0])))**0.5 ) ** 6)+((sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[3],w[0])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[2])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[1],w[3])))**0.5 ) ** 6)+ ((sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 12 - (sigma / np.sum(np.square(np.subtract(w[2],w[3])))**0.5 ) ** 6))

# Function to compute the gradient
def gradient(w):
    dgdw = grad(g)
    return dgdw(w)
    


# Function to plot the objective function
# and learning history annotated by arrows
# to show how learning proceeded
def visualize_learning(w_history):

    # Make the function plot
    # function_plot(pts,f_vals)

    # Plot the history
    print("minimum potential energy found = ",f(np.array(w_history[-1])))
    # Annotate the point found at last iteration
    # for w, i in zip(w_history, range(iter - 1)):
    #     # Annotate with arrows to show history
    #     
def mhessian(f):
        ddf = hessian(f)
        def hess(x):
            return ddf(x).diagonal(axis1=1, axis2=2)
        return hess

    

def solve_fw():
    # Setting up
    (point1,point2,point3,point4) = exam.make_point()
    rand = np.random.RandomState(19)
    w_init = np.array((point1,point2,point3,point4))
    fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(18, 12))

    
    learning_rates = [0.05, 0.2, 0.5, 0.8]
    momentum = [0, 0.5, 0.9]
    
    index = 1
    # Iteration through all possible parameter combinations
    print()
    for alpha in momentum:
        for eta, col in zip(learning_rates, [0, 1, 2, 3]):
            
            w_history, f_history = gradient_descent(
                10, -1, w_init, f, gradient,index, [], eta, alpha, 
            )
            
            if col==0:
                pass
                print('momentum = ' + str(alpha))
            print('Learning Rate = '+str(eta))
            ddf = mhessian(g)
            print("Hessian Matrix = ")
            print(ddf(w_history[-1]))
            visualize_learning(w_history)
            index += 1
            
        print()
            


exam2.get_dist()
solve_fw()
plt.show()
