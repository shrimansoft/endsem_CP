#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import *
import numpy as np
import matplotlib.pyplot as plt

# ---------------* defining the variables *----------------------

tp = 20 + 1
points = tp - 2
dx = 0.1
dt = 0.0008
a = dt / dx**2

# -----------------* Initial State *----------------------

init = np.zeros(points)
for i in range(points):
    init[i] = 20 * abs(np.sin(np.pi * (i + 1) * 0.1))


# -----------------* function plotter *-----------------------


def heatPloter(points, state, text):
    x = np.arange(0, 2.1, 0.1)
    y = np.zeros(points + 2)
    y[1:-1] = state
    plt.plot(x, y, label="i=" + text)


# heatPlotter(points, init, "initial state")
# plt.legend()
# plt.show()

# --------------* propagator *----------------------

A = np.zeros((points, points))

for i in range(points):
    A[i, i] = 1 - 2 * a
    if i + 1 < points:
        A[i + 1, i] = a
        A[i, i + 1] = a

# ----------------* evolving *-----------------------
watch = [
    0,
    10,
    20,
    50,
    100,
    500,
]
for i in range(501):
    if i == 0:
        state = init
    state = np.matmul(A, state)

    if i in watch:
        heatPloter(points, state, str(i))

plt.legend()
plt.show()


# ---------* comments on the plot *-------------------

# Temperature at the endpoint is zero as the boundary condition.
# With time we are losing the heat because the boundary condition is working like a sink at zero temperature.
# At the midpoint the temperature is rising and attains a maximum and then reducing since total heat is flowing out.
