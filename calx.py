import numpy as np
import math

print('For Forward kinematics enter 1')
print('For Inverse kinematics enter 2')
T = int(input('Enter the choice code: '))

print('Enter 1 for Cartesian type Robot')
print('Enter 2 for Cylindrical type Robot')
print('Enter 3 for Spherical type Robot')
d = int(input('Enter the Robot Type: '))

if T == 1:
    if d == 1:
        Lx = int(input('Enter the translation along X-axis: '))
        Ly = int(input('Enter the translation along Y-axis: '))
        Lz = int(input('Enter the translation along Z-axis: '))
        L1 = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, Lz],
              [0, 0, 0, 1]]

        L2 = [[1, 0, 0, 0],
              [0, 1, 0, Ly],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

        # result is 4x4
        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

        # iterate through rows of L1
        for i in range(len(L1)):
            # iterate through columns of L2
            for j in range(len(L2[0])):
                # iterate through rows of L2
                for k in range(len(L2)):
                    res[i][j] += L1[i][k] * L2[k][j]

        L3 = [[1, 0, 0, Lx],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

        fin_res = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

        for i in range(len(res)):
            for j in range(len(L3[0])):
                for k in range(len(L3)):
                    fin_res[i][j] += res[i][k] * L3[k][j]

    # d==2 and else yet to be converted for matrix multiplication
    # fin_res variable should be the transformation matrix
    elif d == 2:
        Lx = int(input('Enter the translation along X-axis: '))
        Qz = int(input('Enter the angle of rotation about Z-axis: '))
        Lz = int(input('Enter the translation along Z-axis: '))

        L1 = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, Lz],
              [0, 0, 0, 1]]

        L2 = [[math.cos(Qz), -(math.sin(Qz)), 0, 0],
              [math.sin(Qz), math.cos(Qz), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

        for i in range(len(L1)):
            # iterate through columns of L2
            for j in range(len(L2[0])):
                # iterate through rows of L2
                for k in range(len(L2)):
                    res[i][j] += L1[i][k] * L2[k][j]

        L3 = [[1, 0, 0, Lx],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

        fin_res = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
        for i in range(len(res)):
            for j in range(len(L3[0])):
                for k in range(len(L3)):
                    fin_res[i][j] += res[i][k] * L3[k][j]


    else:
        Lz = int(input('Enter the translation along Z-axis: '))
        Qy = int(input('Enter the angle of rotation about Y-axis: '))
        Qz = int(input('Enter the angle of rotation about Z-axis: '))

        L1 = [[math.cos(Qz), -(math.sin(Qz)), 0, 0],
              [math.sin(Qz), math.cos(Qz), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

        L2 = [[math.cos(Qy), 0, math.sin(Qy), 0],
              [0, 1, 0, 0],
              [-(math.sin(Qy)), 0, math.cos(Qy), 0],
              [0, 0, 0, 1]]

        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

        for i in range(len(L1)):
            # iterate through columns of L2
            for j in range(len(L2[0])):
                # iterate through rows of L2
                for k in range(len(L2)):
                    res[i][j] += L1[i][k] * L2[k][j]

        L3 = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, Lz],
              [0, 0, 0, 1]]

        fin_res = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

        for i in range(len(res)):
            for j in range(len(L3[0])):
                for k in range(len(L3)):
                    fin_res[i][j] += res[i][k] * L3[k][j]

    print('Transformation Matrix: ')
    print(np.matrix(fin_res))
# End of forward

# inverse kinematics
elif T == 2:
    print("Enter the point: ")
    input_string = input("Enter the point separated by space ")
    list = input_string.split()
    if d == 1:
        print('Translation along X-axis is: ')
        print(list[0])
        print('Translation along Y-axis is: ')
        print(list[1])
        print('Translation along Z-axis is: ')
        print(list[2])
    elif d == 2:
        Lz = int(list[2])
        Qz = math.tan(float(int(list[0])) / (int(list[1])))
        Lx = int(list[0]) / math.cos(float(Qz))
        print('Translation along z-axis is : ')
        print(Lz)
        print('Rotation about Z-axis is : ')
        print(Qz)
        print('Translation along X-axis is : ')
        print(Lx)
    elif d == 3:
        Qz = math.tan(float(int(list[0])) / (int(list[1])));
        Qy = math.tan(math.tan(Qz)) * (float(int(list[1])) / (int(list[2])))
        Lz = (int(list[2])) / math.cos(Qy)
        print('Translation along z-axis is : ')
        print(Lz)
        print('Rotation about Y-axis is : ')
        print(Qy)
        print('Rotation about Z-axis is : ')
        print(Qz)
    else:
        print("Please enter a valid number.")
# end of inverse

else:
    print("Please enter a valid number.")
