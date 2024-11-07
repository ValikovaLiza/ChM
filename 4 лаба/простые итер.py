import numpy as np

epsilon = 0.001
x, y = 0.0, 0.0  
max_iterations = 1000

def f1(x, y):
    return 3 + np.cos(y)

def f2(x, y):
    return 0.5 - np.cos(x - 1)

iterations = 0
while iterations < max_iterations:
    x_new = f1(x, y)
    y_new = f2(x, y)

    if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
        break

    x, y = x_new, y_new
    iterations += 1

print(x, y, iterations)
