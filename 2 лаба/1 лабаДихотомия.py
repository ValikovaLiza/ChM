import math

eps = 0.01

def func(x):
    return x**3 + 3*x - 1
def bisection_method(a, b, eps):
    if func(a) * func(b) >= 0:
        print("На данном отрезке метод дихотомии не применим.")
        return None
    
    while abs(b - a) > eps:
        mid = (a + b) / 2
        if func(mid) == 0: 
            return mid
        elif func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

a = -2
b = 0.5

root = bisection_method(a, b, eps)

if root is not None:
    print(f"Корень уравнения: {root}")
    print(f"Проверка: f({root}) = {func(root)}")



import numpy as np
import matplotlib.pyplot as plt

def y1(x):
    return x**3

def y2(x):
    return 3*x - 1

# Диапазон x для построения графиков
x = np.linspace(-2, 2, 400)

# Построение графиков
plt.figure(figsize=(8, 6))
plt.plot(x, y1(x), label=r'$y = x^3$', color='b')
plt.plot(x, y2(x), label=r'$y = 3x - 1$', color='r')

# Настройки графика
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Графики функций $y = x^3$ и $y = 3x - 1$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
