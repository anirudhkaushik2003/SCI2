import exam
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt




## main code
def get_dist():
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')

    (point1,point2,point3,point4) = exam.make_point()


    # # Creating plot
    # ax.scatter3D(point1[0], point1[1], point1[2], color = "blue")
    # ax.scatter3D(point2[0], point2[1], point2[2], color = "red")
    # ax.scatter3D(point3[0], point3[1], point3[2], color = "green")
    # ax.scatter3D(point4[0], point4[1], point4[2], color = "yellow")

    # plt.title("4 atoms in 3D")
    
    # # show plot
    # plt.show()
    # #print(point1,point2,point3,point4)

    point1=np.array(point1)
    point2=np.array(point2)
    point3=np.array(point3)
    point4=np.array(point4)

    
    
    
    

    epsilon= 0.238
    sigma = 3.4

    # 1 2
    a = abs(np.subtract(point2,point1))
    res1 = a[0]**2 + a[1]**2 + a[2]**2
    res1 = res1**0.5

    final1 = 4*epsilon*((sigma/res1)**12 - (sigma/res1)**6)

    # 1 3
    a = abs(np.subtract(point1,point3))
    res2 = a[0]**2 + a[1]**2 + a[2]**2
    res2 = res2**0.5

    final2 = 4*epsilon*((sigma/res2)**12 - (sigma/res2)**6)



    # 1 4
    a = abs(np.subtract(point1,point4))
    res3 = a[0]**2 + a[1]**2 + a[2]**2
    res3 = res3**0.5

    final3 = 4*epsilon*((sigma/res3)**12 - (sigma/res3)**6)


    # 2 3
    a = abs(np.subtract(point2,point3))
    res4 = a[0]**2 + a[1]**2 + a[2]**2
    res4 = res4**0.5

    final4 = 4*epsilon*((sigma/res4)**12 - (sigma/res4)**6)


    # 2 4 
    a = abs(np.subtract(point2,point4))
    res5 = a[0]**2 + a[1]**2 + a[2]**2
    res5 = res5**0.5

    final5 = 4*epsilon*((sigma/res5)**12 - (sigma/res5)**6)


    # 3 4
    a = abs(np.subtract(point3,point4))
    res6 = a[0]**2 + a[1]**2 + a[2]**2
    res6 = res6**0.5

    final6 = 4*epsilon*((sigma/res6)**12 - (sigma/res6)**6)
    print("initial potential energy of the system = ",final1+final2+final3+final4+final5+final6)
    return (res1,res2,res3,res4,res5,res6)




