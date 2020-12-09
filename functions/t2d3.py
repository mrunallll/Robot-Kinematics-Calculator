import math


def t2d3(points):
    Qz = math.tan(float(int(points[0])) / (int(points[1])))
    Qy = math.tan(math.tan(Qz)) * (float(int(points[1])) / (int(points[2])))
    Lz = (int(points[2])) / math.cos(Qy)

    a = 'Translation along z-axis is : ' + str(Lz)
    b = 'Rotation about Y-axis is : ' + str(Qy)
    c = 'Rotation about Z-axis is : ' + str(Qz)
    output_string = [a, b, c]

    return output_string
