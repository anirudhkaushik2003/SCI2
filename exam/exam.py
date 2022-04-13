import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np

# random points
def make_point():
    point1 = (0,0,0)

    value = 5/(2**0.5)
    value2 = 6/(2**0.5)
    x=0
    y=0
    z=0

    x=random.uniform(0,value)
    y=random.uniform((25 - (x**2))**0.5,(36 - (x**2))**0.5)
    z=0

    point2=(x,y,z)

    x /=2 
    y /=2
    z = random.uniform((25-((x**2 + y**2)/4))**0.5 ,(36-((x**2 + y**2)/4))**0.5 )

    point3=(x,y,z)

    point4=(x,y,-1*z)
    print("points = ")
    print(point1,point2,point3,point4)
    return(point1,point2,point3,point4)
    




