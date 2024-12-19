import numpy as np
import pandas as pd

# Дано
f = lambda x, y: y - 3 * x  # Производная y'
x0, y0 = 1, 0               # Начальное условие
h = 0.3                     # Шаг
x_values = np.arange(x0, 2.2 + h, h)  # Точки сетки

# Метод Эйлера
def euler_method(f, x0, y0, h, x_values):
    y = [y0]
    for i in range(len(x_values) - 1):
        y_new = y[-1] + h * f(x_values[i], y[-1])
        y.append(y_new)
    return y

# Модифицированный метод Эйлера
def modified_euler_method(f, x0, y0, h, x_values):
    y = [y0]
    for i in range(len(x_values) - 1):
        y_predict = y[-1] + h * f(x_values[i], y[-1])  # Предсказанное значение
        y_correct = y[-1] + (h / 2) * (f(x_values[i], y[-1]) + f(x_values[i + 1], y_predict))
        y.append(y_correct)
    return y

# Метод Рунге-Кутта 4-го порядка
def runge_kutta_method(f, x0, y0, h, x_values):
    y = [y0]
    for i in range(len(x_values) - 1):
        k1 = h * f(x_values[i], y[-1])
        k2 = h * f(x_values[i] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x_values[i] + h, y[-1] + k3)
        y_new = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y.append(y_new)
    return y

# Вычисления
euler_results = euler_method(f, x0, y0, h, x_values)
modified_euler_results = modified_euler_method(f, x0, y0, h, x_values)
runge_kutta_results = runge_kutta_method(f, x0, y0, h, x_values)

# Сводная таблица
results_table = pd.DataFrame({
    "x": x_values,
    "Euler": euler_results,
    "Modified Euler": modified_euler_results,
    "Runge-Kutta": runge_kutta_results
})

print(results_table)
