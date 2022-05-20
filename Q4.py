import math


def potientialFunction(x):
    return 1.0 / math.sqrt(1 + x**2)


def legendreZeroWeights(Degree):
    if Degree == 4:
        return [0.861136311, 0.339981043, -0.339981043, -0.861136311], [
            0.347854845,
            0.652145154,
            0.652145154,
            0.347854845,
        ]
    elif Degree == 5:
        return [0.906179845, 0.538469310, 0, -0.538469310, -0.906179845], [
            0.236926885,
            0.478628670,
            0.568888889,
            0.478628670,
            0.236926885,
        ]
    elif Degree == 6:
        return [
            0.932469514,
            0.661209386,
            0.238619186,
            -0.238619186,
            -0.661209386,
            -0.932469514,
        ], [
            0.171324492,
            0.360761573,
            0.467913934,
            0.467913934,
            0.360761573,
            0.171324492,
        ]


def gaussQuadratureFunction(f, n):
    s = 0
    zeros, weights = legendreZeroWeights(n)
    for j in range(n):
        s += weights[j - 1] * potientialFunction(zeros[j - 1])
    return s


num = [4, 5, 6]

for k in num:
    print(
        "Degree: ",
        k,
        ",Potential:",
        gaussQuadratureFunction(potientialFunction, k),
    )
# ---------------* OUTPUT *----------------------
# Degree:  4 ,Potential: 1.7620541789046658
# Degree:  5 ,Potential: 1.7628552954010728
# Degree:  6 ,Potential: 1.762730048499759
