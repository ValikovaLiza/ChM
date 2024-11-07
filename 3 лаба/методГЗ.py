import numpy as np

def gauss_seidel(A, B, x0, tol=0.01, max_iterations=100):
    n = len(B)  # Количество уравнений
    x = np.array(x0, dtype=float)  # Начальное приближение
    
    for it in range(max_iterations):  # Основной цикл итераций
        x_old = np.copy(x)  # Сохраняем старое значение для проверки сходимости
        
        for i in range(n):  # Проходим по всем уравнениям
            # Считаем сумму по предыдущим компонентам
            sum1 = np.dot(A[i, :i], x[:i])
            # Считаем сумму по следующим компонентам
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            # Вычисляем новое значение переменной
            x[i] = (B[i] - sum1 - sum2) / A[i, i]
        
        # Проверка на сходимость: если изменение меньше заданной точности
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"Метод Гаусса-Зейделя сошелся за {it+1} итераций.")
            return x  # Возвращаем решение
    
    print("Метод Гаусса-Зейделя не сошелся.")
    return x  # Возвращаем последнее значение, даже если не сошелся

A = np.array([[3, 1, -1, 1],
              [1, -4, 1, -1],
              [-1, 1, 4, 1],
              [1, 2, 1, -5]], dtype=float)

B = np.array([9, -3, 12, 5], dtype=float)
initial_guess = [2.1, 1, 2, 0.5]  

solution = gauss_seidel(A, B, initial_guess)
print("Решение методом Гаусса-Зейделя:", solution)

#Метод Якоби

def jacobi(A, B, x0, tol=0.01, max_iterations=100):
    n = len(B)  # Количество уравнений
    x = np.array(x0, dtype=float)  # Начальное приближение
    
    for it in range(max_iterations):  # Основной цикл итераций
        x_old = np.copy(x)  # Сохраняем старое значение для проверки сходимости
        
        for i in range(n):  # Проходим по всем уравнениям
            # Считаем сумму по предыдущим компонентам
            sum1 = np.dot(A[i, :i], x_old[:i])
            # Считаем сумму по следующим компонентам
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            # Вычисляем новое значение переменной
            x[i] = (B[i] - sum1 - sum2) / A[i, i]
        
        # Проверка на сходимость: если изменение меньше заданной точности
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"Метод Якоби сошелся за {it+1} итераций.")
            return x  # Возвращаем решение
    
    print("Метод Якоби не сошелся.")
    return x

solution_jacobi = jacobi(A, B, initial_guess)
print("Решение методом Якоби:", solution_jacobi)
