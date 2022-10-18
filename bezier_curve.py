#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Xu Haitao
# @Time : 2022/10/17 15:56
import matplotlib.pyplot as plt
import numpy as np

PT = []
isDrawable = True


def on_press(event, fig, steps):
    global PT
    s = np.linspace(1, steps, steps) / steps
    if event.button == 1:  # 鼠标左键点击
        PT.append([event.xdata, event.ydata])
        plt.scatter([event.xdata], [event.ydata])
        fig.canvas.draw()
    elif event.button == 3:  # 鼠标右键点击
        points = np.array(PT).reshape((-1, 2))
        points_num = points.shape[0]
        plt.scatter(points[:, 0], points[:, 1])  # 画出初始点并虚线连接表示顺序
        for i in range(points_num - 1):
            plt.plot(points[i: i + 2, 0], points[i: i + 2, 1], '--')
            plt.pause(0.1)
        # 为方便计算更改维度
        points = np.tile(points, (steps, 1, 1)).transpose((1, 0, 2))

        # 迭代，直到最后的曲线
        while points.shape[0] > 1:
            d_points = np.array([(points[i + 1, :, :] - points[i, :, :]) for i in range(points.shape[0] - 1)])
            s_temp = np.tile(s.reshape(-1, d_points.shape[1], 1), (points.shape[0] - 1, 1, 2))
            points = d_points * s_temp + points[:-1, :, :]
        # 画线
        for i in range(1, 11):
            plt.plot(points[0, (i - 1) * 10:i * 10, 0], points[0, (i - 1) * 10:i * 10, 1], 'r--')
            plt.pause(0.2)
        plt.plot(points[0, :, 0], points[0, :, 1], 'r')
        plt.pause(1)


def main():
    steps = 100

    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_title('Bezier Curve', fontsize=18)
    ax.set_xlabel('x', fontsize=18, fontfamily='sans-serif', fontstyle='italic')
    ax.set_ylabel('y', fontsize='x-large', fontstyle='oblique')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    fig.canvas.mpl_connect('button_press_event', lambda event: on_press(event, fig, steps))
    plt.show()


if __name__ == '__main__':
    main()
