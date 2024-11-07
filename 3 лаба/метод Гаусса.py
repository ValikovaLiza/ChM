import numpy as np

def gauss_elimination(a, b):
    n = len(b)  # Определяем размерность системы уравнений
    
    # Прямой ход метода Гаусса
    for i in range(n):
        # Перебираем строки ниже текущей (i) для обнуления элементов под ведущим элементом
        for j in range(i + 1, n):
            # Вычисляем коэффициент для вычитания
            factor = a[j][i] / a[i][i]
            b[j] -= factor * b[i]  # Обновляем свободный член

            # Обновляем строки матрицы коэффициентов
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]

    # Обратный ход: находим решения
    x = np.zeros(n)  # Создаем массив для решения
    for i in range(n - 1, -1, -1):  # Проходим с конца к началу
        # Вычисляем значение переменной x[i]
        x[i] = (b[i] - np.dot(a[i], x)) / a[i][i]
    
    return x  # Возвращаем найденное решение

A = np.array([[1, 2, -1, -1],
              [2, 3, -1, 1],
              [2, 5, 2, 1],
              [3, 5, 1, 2]], dtype=float)

B = np.array([0, 3, 3, 5], dtype=float)

# Вызываем функцию и выводим решение
solution = gauss_elimination(A, B)
print("Решение методом Гаусса:", solution)


# Метод обратной матрицы
def inverse_matrix_method(a, b):
    # Находим обратную матрицу для матрицы коэффициентов a
    a_inv = np.linalg.inv(a)
    # Умножаем обратную матрицу на вектор свободных членов b,
    # чтобы найти решение системы уравнений
    x = np.dot(a_inv, b)
    return x  

solution = inverse_matrix_method(A, B)
print("Решение методом обратной матрицы:", solution)
