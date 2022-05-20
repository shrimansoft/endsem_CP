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


X, Y = data("data.txt", ",")


print(X, Y)


def legendre_basis(n, x):
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


coefficients = []

for i in range(7):
    num = 0
    den = 0
    for x, y in zip(X, Y):
        num += y * legendre_basis(i, x)
        den += legendre_basis(i, x) * legendre_basis(i, x)
    coefficients.append(num / den)


print(coefficients)
