import math

# Определяем функцию f(x) и её производную f'(x)
def f(x):
    return x**3 + 3*x - 1
def f_prime(x):
    return 3*x**2 + 3
def f_prime2(x):
    return 6*x

# Метод Ньютона
def newton_method(x0, tol=0.01, max_iter=50):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:  # Избегаем деления на 0
            print("Производная равна нулю, метод не может продолжать.")
            return None
        
        x_new = x - fx / fpx
        print(f"Итерация {i+1}: x = {x_new}, f(x) = {fx}")
        
        # Проверка критерия сходимости
        if abs(x_new - x) < tol:
            print(f"Найден корень: {x_new}")
            return x_new
        
        x = x_new
    
    print("Превышено максимальное количество итераций.")
    return None

x0 = 1  
# res = f(x0)*f_prime2(x0)
# print(res)
root = newton_method(x0)
