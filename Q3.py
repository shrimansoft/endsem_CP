import numpy as np
from matplotlib import pyplot as plt


def PDEexplicit(L, n, Delt, tmax, func, a, b):
    u = [0 for x in range(n + 1)]
    u1 = [0 for x in range(n + 1)]

    # Updating Boundary conditions
    u[0], u[n] = a, b
    u1[0], u1[n] = a, b

    Delx = L / n
    alpha = Delt / (Delx**2)

    xvalue = [0]
    for i in range(1, n):
        x = i * Delx
        u[i] = func(x)
        xvalue.append(x)
    xvalue.append(xvalue[-1] + Delx)

    t = Delt
    while t < tmax:
        for i in range(1, n):
            u1[i] = alpha * u[i - 1] * (1 - 2 * alpha) * u[i] + alpha * u[i + 1]
            u[i] = u1[i].copy()
        t = t + Delt
    return u, xvalue

    # Function can be changed as per requirement. Now only boundary value defined.


def func(x):
    L=5
    if x == 0:
        return 0
    elif x == L:
        return 1


Delx = 0.1
Delt = 0.004
L = 5
t = [0.5, 1, 1.5, 5, 10]
x = np.arange(0, L + Delx, Delx)
for i in range(len(t)):
    u1 = PDEexplicit(L, Delx, Delt, func, t[i])
    u1 = np.transpose(u1)
    u1 = u1[0]
    plt.plot(x, u1, label=t[i])
plt.legend()
plt.show()
