import numpy as np
def f1(x):
    return 0.5 - np.cos(x - 1)

def f2(y):
    return 3 + np.cos(y)

def seidel_method(x0, y0, tol=1e-3, max_iter=100):
    x, y = x0, y0
    for i in range(max_iter):
        y_new = f1(x)
        x_new = f2(y_new)
        if abs(x - x_new) < tol and abs(y - y_new) < tol:
            return x_new, y_new, i + 1
        x, y = x_new, y_new
        
    raise ValueError("Метод Зейделя не сошелся за отведенное число итераций")

x0, y0 = 3.0, 1.0
x, y, iterations = seidel_method(x0, y0)
print(f"Метод Зейделя: x ≈ {x:.3f}, y ≈ {y:.3f}, итераций: {iterations}")
