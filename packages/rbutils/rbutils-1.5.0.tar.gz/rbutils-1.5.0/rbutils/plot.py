import matplotlib.pyplot as plt
import numpy as np
import math
import rbutils.rbnp as rbnp

# 绘制平面图
def plot_3d(x_start, x_end, y_start, y_end, num, funZ):
    # 创建新的图和坐标轴
    fig = plt.figure()
    # 111表示1行1列第1个
    ax = fig.add_subplot(111, projection="3d")
    # 生成网格数据
    X = np.linspace(x_start, x_end, num)  # m个数据的一维数组
    Y = np.linspace(y_start, y_end, num)  # n个数据的一维数组
    X, Y = np.meshgrid(X, Y)
    Z = funZ(X, Y)
    # 标识坐标轴
    plt.xlabel("X")
    plt.ylabel("Y")
    # 绘制表面图
    ax.plot_surface(X, Y, Z, cmap="viridis")
    # 显示图表
    plt.show()


# 绘制平面图和平行z轴的直线
def plot_3d_z(x_start, x_end, y_start, y_end, num, funZ, z_start, z_end, z_arr):
    # 创建新的图和坐标轴
    fig = plt.figure()
    # 111表示1行1列第1个
    ax = fig.add_subplot(111, projection="3d")
    # 生成网格数据
    X = np.linspace(x_start, x_end, num)  # m个数据的一维数组
    Y = np.linspace(y_start, y_end, num)  # n个数据的一维数组
    X, Y = np.meshgrid(X, Y)
    Z = funZ(X, Y)
    # 标识坐标轴
    plt.xlabel("X")
    plt.ylabel("Y")
    # 绘制表面图
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9)

    # 创建3d绘图区域
    z2 = np.linspace(z_start, z_end, num)
    for item in z_arr:
        x = item[0]
        y = item[1]
        ax.plot3D(x, y, z2, "red")
    # 显示图表
    plt.show()


# 绘制平面图和平行z轴的直线
def plot_3d_line(x_start, x_end, y_start, y_end, num, funZ, x1,y1,x2,y2,number):
    # 创建新的图和坐标轴
    fig = plt.figure()
    # 111表示1行1列第1个
    ax = fig.add_subplot(111, projection="3d")
    # 生成网格数据
    X = np.linspace(x_start, x_end, num)  # m个数据的一维数组
    Y = np.linspace(y_start, y_end, num)  # n个数据的一维数组
    X, Y = np.meshgrid(X, Y)
    Z = funZ(X, Y)
    # 标识坐标轴
    plt.xlabel("X")
    plt.ylabel("Y")
    # 绘制表面图
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9)

    # 创建3d绘图区域
    arr = rbnp.linspace_2d(x1,y1,x2,y2, number)
    X1 = arr[:,0]
    Y1 = arr[:,1]
    Z1 = funZ(X1, Y1)
    print('Z:',Z1)
    ax.scatter3D(X1, Y1, Z1,c='red')
    # 显示图表
    plt.show()


def _z(x, y):
    return x * math.e ** (2 * y)


if __name__ == "__main__":
    # 本地测试使用
    # print(rbnp.linspace_2d(1,2,3,4,51))
    # plot_3d(0, 3, -2, 1, 100, _z)
    # plot_3d_z(0, 3, -2, 1, 100, _z, 1, 30, np.array([[1, 0], [2, -1]]))
    # x不要太大
    plot_3d_line(1, 2, -1, 0, 100, _z, 1,0,2,-1,101)
