import matplotlib.pyplot as plt
import numpy as np


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
