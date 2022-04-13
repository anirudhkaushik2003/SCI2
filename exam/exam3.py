import exam2
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as dt
from sklearn.model_selection import train_test_split

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
    w_history = w
    f_history = obj_func(w, extra_param)
    delta_w = np.zeros(w.shape)
    i = 0
    diff = 1.0e10

    while i < max_iterations and diff > threshold:
        delta_w = -learning_rate * grad_func(w, extra_param) + momentum * delta_w
        w = w + delta_w
        
        # store the history of w and f
        w_history = np.vstack((w_history, w))
        f_history = np.vstack((f_history, obj_func(w, extra_param)))

        # update iteration number and diff between successive values
        # of objective function
        i += 1
        diff = np.absolute(f_history[-1] - f_history[-2])
        plt.subplot(3, 4, index)
            
        plt.plot(i,obj_func(w), 'bo')
        
    return w_history, f_history





# Pts are 2D points and f_val is the corresponding function value


# Objective function
def f(w, extra=[]):
    return (
        4
        * epsilon
        * (
            ((sigma / w[0]) ** 12 - (sigma / w[0]) ** 6)
            + ((sigma / w[1]) ** 12 - (sigma / w[1]) ** 6)
            + ((sigma / w[2]) ** 12 - (sigma / w[2]) ** 6)
            + ((sigma / w[3]) ** 12 - (sigma / w[3]) ** 6)
            + ((sigma / w[4]) ** 12 - (sigma / w[4]) ** 6)
            + ((sigma / w[5]) ** 12 - (sigma / w[5]) ** 6)
        )
    )


# Function to compute the gradient
def grad(w, extra=[]):
    return (
        4
        * epsilon
        * (
            ((-12 * (sigma ** 12) / (w[0] ** 13)) + (6 * (sigma ** 6) / (w[0] ** 7)))
            * ((-12 * (sigma ** 12) / (w[1] ** 13)) + (6 * (sigma ** 6) / (w[1] ** 7)))
            * ((-12 * (sigma ** 12) / (w[2] ** 13)) + (6 * (sigma ** 6) / (w[2] ** 7)))
            * ((-12 * (sigma ** 12) / (w[3] ** 13)) + (6 * (sigma ** 6) / (w[3] ** 7)))
            * ((-12 * (sigma ** 12) / (w[4] ** 13)) + (6 * (sigma ** 6) / (w[4] ** 7)))
            * ((-12 * (sigma ** 12) / (w[5] ** 13)) + (6 * (sigma ** 6) / (w[5] ** 7)))
        )
    )


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

def solve_fw():
    # Setting up
    (res1, res2, res3, res4, res5, res6) = exam2.get_dist()
    rand = np.random.RandomState(19)
    w_init = np.array((res1, res2, res3, res4, res5, res6))
    fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(18, 12))

    
    learning_rates = [0.05, 0.2, 0.5, 0.8]
    momentum = [0, 0.5, 0.9]
    
    index = 1
    # Iteration through all possible parameter combinations
    print()
    for alpha in momentum:
        for eta, col in zip(learning_rates, [0, 1, 2, 3]):
            
            w_history, f_history = gradient_descent(
                100, -1, w_init, f, grad,index, [], eta, alpha, 
            )
            
            if col==0:
                print('momentum = ' + str(alpha))
            print('Learning Rate = '+str(eta))
            visualize_learning(w_history)
            index += 1
            
        print()
            



solve_fw()
plt.show()
