#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Xu Haitao
# @Time : 2022/10/17 20:39
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def on_press(event, fig, V, n):
    # global V
    if event.button == 1:  # 鼠标左键点击
        V[0].append(event.xdata)
        V[1].append(event.ydata)
        plt.scatter([event.xdata], [event.ydata])
        fig.canvas.draw()
    elif event.button == 3:  # 鼠标右键点击
        V_num = len(V[0])
        T = np.linspace(0, 1, n + V_num + 1)  # T存储节点
        t_x = np.linspace(0, 1, 160)  # t_x存储每一个t值
        X = V[0]
        Y = V[1]
        plt.scatter(X, Y)
        for i in range(len(X) - 1):
            plt.plot(X[i:i + 2], Y[i:i + 2], '--')
            plt.pause(0.1)
        x = []  # 用来存储曲线的x值
        y = []  # 用来存储曲线的y值
        for i in range(V_num - n):  # for循环用作获取第几条曲线段的数值
            result = pd.DataFrame(t_x, columns=['t'])
            for j in range(n + 1):
                result1 = []
                for t in t_x:
                    result1.append(N(i + j, n, T, t))
                result['N_{0}{1}'.format(i + j, n)] = result1  # 将N_ij存入dataframe
            Ni_matrix = np.matrix(result[result['t'].apply(lambda x: T[i + n] <= x <= T[i + n + 1])].iloc[:,
                                  1:])  # Ni_matrix 是一个 t_ba*j 维矩阵

            x = x + (Ni_matrix * np.matrix(X[i:i + n + 1]).T).T.tolist()[0]
            y = y + (Ni_matrix * np.matrix(Y[i:i + n + 1]).T).T.tolist()[0]

        for i in range(len(x)):
            plt.plot(x[i:(i + 2)], y[i:i + 2], 'r--')
            plt.pause(0.02)
        plt.plot(x, y, 'r')
        plt.pause(0.01)


def N(i, k, T, t):  # 曲线N_ik
    if k == 0:
        if t < T[i] or t > T[i + 1]:
            return 0
        else:
            return 1
    else:
        result = (t - T[i]) / (T[i + k] - T[i]) * N(i, k - 1, T, t) + (T[i + k + 1] - t) / (
                T[i + k + 1] - T[i + 1]) * N(i + 1, k - 1, T, t)
        return result


def main(_n):
    V = [[], []]  # 有重复型值点坐标
    n = _n
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_title('B_Curve', fontsize=18)
    ax.set_xlabel('x', fontsize=18, fontfamily='sans-serif', fontstyle='italic')
    ax.set_ylabel('y', fontsize='x-large', fontstyle='oblique')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    fig.canvas.mpl_connect('button_press_event', lambda event: on_press(event,fig, V, n))
    plt.show()


if __name__ == '__main__':
    main(1)
