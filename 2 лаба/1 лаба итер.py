# Определяем вспомогательную функцию φ(x)
def phi(x):
    return (1 - x**3) / 3

# Метод простых итераций
def simple_iteration(x0, tol=0.01, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = phi(x)
        print(f"Итерация {i+1}: x = {x_new}")
        
        # Проверка критерия сходимости
        if abs(x_new - x) < tol:
            print(f"Найдено решение: {x_new}")
            return x_new
        
        x = x_new
    
    print("Превышено максимальное количество итераций.")
    return None

# Начальное приближение
x0 = 0.5  # Начальное приближение можно выбрать в зависимости от задачи
root = simple_iteration(x0)
