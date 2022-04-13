import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np


point_array = []
num_points = 0
L = 18
while True:
    print(num_points)
    if num_points >= 108:
        break
    point = np.random.uniform(0, L, 3)
    if num_points == 0:
        point_array.append(point)
        num_points += 1
    else:
        cond = 1
        for i in point_array:
            res = (
                (i[0] - point[0]) ** 2 + (i[1] - point[1]) ** 2 + (i[2] - point[2]) ** 2
            ) ** 0.5
            if res >= 3.4:
                if abs(i[0] - point[0]) > L / 2:
                    if (i[0] - point[0]) > 0:
                        point[0] += i[0] - point[0] - L / 2
                    else:
                        point[0] += i[0] - point[0] + L / 2
                if abs(i[1] - point[1]) > L / 2:
                    if (i[1] - point[1]) > 0:
                        point[1] += i[1] - point[1] - L / 2
                    else:
                        point[1] += i[1] - point[1] + L / 2
                if abs(i[2] - point[2]) > L / 2:
                    if (i[2] - point[2]) > 0:
                        point[2] += i[2] - point[2] - L / 2
                    else:
                        point[2] += i[2] - point[2] + L / 2
            res = ((i[0] - point[0]) ** 2 + (i[1] - point[1]) ** 2 + (i[2] - point[2]) ** 2) ** 0.5
            if res >= 3.4:
                pass
            else:
                cond = 0
                break
        if  cond == 1:
            point_array.append(point)
            num_points += 1
            
