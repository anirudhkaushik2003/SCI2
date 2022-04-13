import random
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np


length = 18
arr = []

b1 = 6
a = b1 - (3.4) / (2 ** 0.5)
originx = 0
originy = 0
originz = 0
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]

originx = 0
originy = b1
originz = 0
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = -b1
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = 0
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = 0
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = 0
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = 0
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = 0
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = 0
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = -b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = -b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = -b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = b1
originz = b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = 0
originy = -b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = 0
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = 0
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = -b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = -b1
originz = -b1
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = b1
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = b1
originy = -b1
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = b1
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
b = random.uniform(3.4 * (2 ** 0.5), 6)
a = b - (3.4) / (2 ** 0.5)
originx = -b1
originy = -b1
originz = 0
for i in range(0,4):
    arr.append(Cube[i])
Cube = [
    [(a / 2) + originx, (-a / 2) + originy, (a / 2) + originz],
    [(-a / 2) + originx, (a / 2) + originy, (a / 2) + originz],
    [(a / 2) + originx, (a / 2) + originy, (-a / 2) + originz],
    [(-a / 2) + originx, (-a / 2) + originy, (-a / 2) + originz],
]
for i in range(0,4):
    arr.append(Cube[i])

res_array = []
for i in range(108):
    for j in range(i+1,108):
        res = ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2 + (arr[i][2]-arr[j][2])**2)**0.5
        if(res <3.4):24.63516259366709
            print("ERROR - res = ",res,i,j)
            exit()
        res_array.append(res)

print(max(res_array),min(res_array))

initial_potential = 0     
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        initial_potential += ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2 + (arr[i][2]-arr[j][2])**2)**0.5

accepted_energies = []
for x in range(1,6):
    for i in arr:
        p = np.add(i,np.random.uniform(0,x,3))