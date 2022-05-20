from lib import *
import numpy as np
import matplotlib.pyplot as plt


X, Y = data("data.txt", ",")


# print(X, Y)


def legendre_basis(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return (3 * (x**2) - 1) / 2
    if n == 3:
        return (5 * (x**2) - 3 * x) / 2
    if n == 4:
        return (35 * x**4 - 30 * x**2 - 3) / 8
    if n == 5:
        return (63 * x**5 - 70 * x**3 + 15 * x) / 8
    if n == 6:
        return (231 * x**6 - 315 * x**4 + 105 * x**2 - 5) / 16


def legendre_fit(X, Y, d):
    length = len(X)
    p = d + 1
    A = np.zeros((p, p))
    b = np.zeros(p)

    for i in range(p):
        for j in range(p):
            total = 0
            for k in range(length):
                total += legendre_basis(X[k], j) * legendre_basis(X[k], i)
            A[i, j] = total

    for i in range(p):
        total = 0
        for j in range(length):
            total += legendre_basis(X[j], i) * Y[j]
        b[i] = total

    x = lu_decomp(A, b)
    return x


cofficient = legendre_fit(X, Y, 6)
print("cofficient: ", cofficient)


Y_value = []
for x in X:
    y = 0
    for i in range(7):
        y += cofficient[i] * legendre_basis(x, i)
    Y_value.append(y)


plt.plot(X, Y, "g.")
plt.plot(X, Y_value, "orange")
plt.show()

# -------------* OUTPUT *--------------------------
# cofficient:  [0.254211885835266, -0.17218286267747054, 0.18701530188300514, -0.11830920749508334, 0.11411855049286564, -0.0024888108366943845, -0.012384559712646365]
