def column(a, i):
    """
    Returns a specific column
    of a multidimensional list
    """
    return [row[i] for row in a]


def data(file, char_):
    """
    Open a file that contains
    data to fit | Format (x,y)
    char_ : separator character
           ' '     <== Space delimited
           '\t'    <== Tabs delimited
           ','     <== Comma delimitedk
    """
    data = open(file, "r")
    line = [line.rstrip().split(char_) for line in data]
    x = column(line, 0)
    y = column(line, 1)
    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    return x, y


# Forward backward substitution
def for_back(U, L, b):
    n = len(b)
    y = [0 for i in range(n)]

    for i in range(n):
        total = 0
        for j in range(i):
            total += L[i][j] * y[j]
        y[i] = (b[i] - total) / L[i][i]

    x = [0 for i in range(n)]

    for i in reversed(range(n)):
        total = 0
        for j in range(i + 1, n):
            total += U[i][j] * x[j]
        x[i] = (y[i] - total) / U[i][i]

    return x


def partial_pivot(A, b):
    count = 0
    n = len(A)
    for i in range(n - 1):
        if abs(A[i][i]) < 1e-10:
            for j in range(i + 1, n):
                if abs(A[j][i]) > abs(A[i][i]):
                    A[j], A[i] = (
                        A[i],
                        A[j],
                    )  # interchange ith and jth rows of matrix 'A'
                    count += 1
                    b[j], b[i] = (
                        b[i],
                        b[j],
                    )  # interchange ith and jth elements of vector 'b'
    return A, b, count


# LU Decomposition
def lu_decomp(A, b):
    def cr_out(A):
        U = [[0 for i in range(len(A))] for j in range(len(A))]
        L = [[0 for i in range(len(A))] for j in range(len(A))]

        for i in range(len(A)):
            L[i][i] = 1

        for j in range(len(A)):
            for i in range(len(A)):
                total = 0
                for k in range(i):
                    total += L[i][k] * U[k][j]

                if i == j:
                    U[i][j] = A[i][j] - total

                elif i > j:
                    L[i][j] = (A[i][j] - total) / U[j][j]

                else:
                    U[i][j] = A[i][j] - total

        return U, L

    partial_pivot(A, b)
    U, L = cr_out(A)
    x = for_back(U, L, b)
    return x
