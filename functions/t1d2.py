import math


def t1d2(Lx, Qz, Lz):
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

    return fin_res
