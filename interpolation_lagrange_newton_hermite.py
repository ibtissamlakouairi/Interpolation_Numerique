import numpy as np

def lagrange(x_points, y_points, x):
    result = 0
    for i in range(len(x_points)):
        term = y_points[i]
        for j in range(len(x_points)):
            if i != j:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        result = result + term
    return result

def newton_coefficients(x_points, y_points):
    n = len(x_points)
    table = np.zeros((n, n))
    table[:, 0] = y_points
    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (
                table[i + 1, j - 1] - table[i, j - 1]
            ) / (  x_points[i + j] - x_points[i] )
    coefficients = table[0, :]
    return coefficients

def newton(x_points, y_points, x):
    coefficients = newton_coefficients(x_points, y_points)
    result= coefficients[0]
    product= 1

    for i in range(1, len(x_points)):
        product = product * (x - x_points[i - 1])
        result = result + coefficients[i] * product
    return result

def hermite(x_points, y_points, dy_points, x):
    n = len(x_points)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 2 * n))

    for i in range(n):
        z[2 * i] = x_points[i]
        z[2 * i + 1] = x_points[i]

        Q[2 * i, 0] = y_points[i]
        Q[2 * i + 1, 0] = y_points[i]

        Q[2 * i + 1, 1] = dy_points[i]

        if i != 0:
            Q[2 * i, 1] = (
                Q[2 * i, 0] - Q[2 * i - 1, 0]
            ) / (
                z[2 * i] - z[2 * i - 1] )

    for j in range(2, 2 * n):
        for i in range(j, 2 * n):
            Q[i, j] = (
                Q[i, j - 1] - Q[i - 1, j - 1]
            ) / (
                z[i] - z[i - j] )

    result = Q[0, 0]
    product = 1

    for j in range(1, 2 * n):
        product = product * (x - z[j - 1])
        result = result + Q[j, j] * product
    return result