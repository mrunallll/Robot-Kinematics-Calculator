import math


def t2d2(points):
    Lz = int(points[2])
    Qz = math.tan(float(int(points[0])) / (int(points[1])))
    Lx = int(points[0]) / math.cos(float(Qz))

    a = 'Translation along z-axis is : ' + str(Lz)
    b = 'Rotation about Z-axis is : ' + str(Qz)
    c = 'Translation along X-axis is : ' + str(Lx)
    output_string = [a, b, c]

    return output_string
