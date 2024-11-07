def f(x):
    return x**3 + 3*x - 1

# Метод хорд
def chord_method(a, b, tol=0.01, max_iter=100):
    if f(a) * f(b) > 0:
        print("На отрезке [a, b] нет корня или их больше одного.")
        return None
    
    for i in range(max_iter):
        x_new = b - f(b) * (b - a) / (f(b) - f(a))
        print(f"Итерация {i+1}: x = {x_new}")
        
        if abs(f(x_new)) < tol:
            print(f"Найден корень: {x_new}")
            return x_new
        
        if f(a) * f(x_new) < 0:
            b = x_new
        else:
            a = x_new
    
    print("Превышено максимальное количество итераций.")
    return None

a = 0
b = 1
root = chord_method(a, b)


# Разностный метод Ньютона с постоянным шагом
def newton_difference_method(x0, h, tol=0.01, max_iter=100):
    x = x0
    for i in range(max_iter):
        # Вычисляем разностную производную
        f_prime_approx = (f(x + h) - f(x)) / h
        
        if f_prime_approx == 0:
            print("Производная равна нулю, метод не может продолжать.")
            return None
        
        # Вычисляем следующее приближение
        x_new = x - f(x) / f_prime_approx
        print(f"Итерация {i+1}: x = {x_new}")
        
        # Проверяем условие сходимости
        if abs(x_new - x) < tol:
            print(f"Найден корень: {x_new}")
            return x_new
        
        x = x_new
    
    print("Превышено максимальное количество итераций.")
    return None

# Начальное приближение и шаг h
x0 = 0.5
h = 0.01
root = newton_difference_method(x0, h)
