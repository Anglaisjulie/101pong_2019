#!/usr/bin/python3

from math import *
import math
import sys


def calc(x0, y0, z0, x1, y1, z1):
    x = x1 - x0
    y = y1 - y0
    z = z1 - z0
    print(f"The velocity vector of the ball is:\n({x:.2f}, {y:.2f}, {z:.2f})")
    xt = x1 + (n * x)
    yt = y1 + (n * y)
    zt = z1 + (n * z)
    print(f"At time t + {n}, ball coordinates will be:\n({xt:.2f}, {yt:.2f}, {zt:.2f})")
    alpha = z / sqrt((x*x) + (y*y) + (z*z))
    angle = round(acos(alpha) / math.pi *180 - 90, 2)
    if z == 0 or xt == 0 or (z1 / z) > 0:
        print("The ball won’t reach the paddle.")
    else:
        print(f"The incidence angle is:\n{angle} degrees")

if __name__ == "__main__":
    x0 = float(sys.argv[1])
    y0 = float(sys.argv[2])
    z0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    y1 = float(sys.argv[5])
    z1 = float(sys.argv[6])
    n = int(sys.argv[7])
    if n < 0:
        print("error value n")
    else:
        calc(x0, y0, z0, x1, y1, z1)
