from hello import helloworld
from calc import add
from plot import plot_3d,plot_3d_z


import math
import numpy as np
def test_helloworld():
    helloworld()

def test_add():
    print('1 + 2 =',add(1,2))

def _z(x, y):
    return x*math.e**(2*y)

def test_plot_3d():
    plot_3d(0, 3, -2, 1, 100, _z)

def test_plot_3d_z():
    plot_3d_z(0, 3, -2, 1, 100, _z,1,30,np.array([[1,0],[2,-1]]))