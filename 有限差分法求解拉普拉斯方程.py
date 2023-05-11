# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:37:29 2023

@author: 86319
"""

import numpy as np

# 如果f!=0注意定义函数def f(x,y):
def diff(w, h, eps, xstart, xend, ystart, yend):
    xn = int((-xstart + xend) / h)
    x = np.linspace(xstart, xend, xn + 1)
    yn = int((-ystart + yend) / h)
    y = np.linspace(ystart, yend, yn + 1)

    # i列对应x的个数，j行对应y的个数
    u = np.zeros((len(y), len(x)))

    k = 0
    delta = eps + 1  # 保证初始delta比误差大

    # 初始条件需要依据题意改
    u[:, 0] = y * (y - 3)  # x=0
    u[:, -1] = 0  # x_max
    u[0, :] = np.sin(np.pi * x / 4)  # y=0
    u[-1, :] = 0  # y_max

    while delta > eps:
        u0 = u.copy()
        for i in range(1, len(x) - 1):
            for j in range(1, len(y) - 1):
                # 注意如果f!=0，得加上-h**2*f(x[i],y[j])
                u[j, i] = w * (u[j, i + 1] + u[j, i - 1] + u[j + 1, i] + u[j - 1, i]) / 4 + (1 - w) * u[j, i]
        delta = np.max(np.abs(u - u0))
        k += 1

    print('迭代次数:', k, ' 误差:', delta)
    return u
result = diff(1.25, 0.1, 1e-4, 0, 4, 0, 3)
print(result)