from rbutils.hello import helloworld
from rbutils.calc import add
from rbutils.plot import plot_3d, plot_3d_z
from rbutils.rbnp import linspace_2d

import math
import numpy as np


def test_helloworld():
    helloworld()


def test_add():
    print('1 + 2 =', add(1, 2))


def _z(x, y):
    return x * math.e ** (2 * y)


def test_plot_3d():
    plot_3d(0, 3, -2, 1, 100, _z)


def test_plot_3d_z():
    plot_3d_z(0, 3, -2, 1, 100, _z, 1, 30, np.array([[1, 0], [2, -1]]))


def test_linspace_2d():
    ret = linspace_2d(1, 2, 3, 4, 50)
    print('test:', ret)


if __name__ == "__main__":
    # 本地测试使用
    test_linspace_2d()
