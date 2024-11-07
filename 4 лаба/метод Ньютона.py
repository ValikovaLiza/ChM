import numpy as np

def f(x, y):
    return np.cos(x - 1) + y - 0.5

def g(x, y):
    return x - np.cos(y) - 3

def jacobian(x, y):
    df_dx = -np.sin(x - 1)
    df_dy = 1
    dg_dx = 1
    dg_dy = np.sin(y)
    return np.array([[df_dx, df_dy], [dg_dx, dg_dy]])

def newton_method(x0, y0, tol=1e-3, max_iter=100):
    x, y = x0, y0
    for i in range(max_iter):
        J = jacobian(x, y)
        F = np.array([f(x, y), g(x, y)])
        delta = np.linalg.solve(J, -F)
        x, y = x + delta[0], y + delta[1]
        if np.linalg.norm(delta) < tol:
            return x, y, i + 1
    raise ValueError("Метод Ньютона не сошелся за отведенное число итераций")

x0, y0 = 3.0, 1.0
x, y, iterations = newton_method(x0, y0)
print(f"Метод Ньютона: x ≈ {x:.3f}, y ≈ {y:.3f}, итераций: {iterations}")
