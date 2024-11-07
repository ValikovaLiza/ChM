import numpy as np

# Определяем матрицу A
A = np.array([[10.95, 1.21, -7.41, 0.94],
              [3.51, 9.78, 1.16, 2.58],
              [1.95, 7.36, 11.21, -7.43],
              [10.54, 11.21, 7.17, 2.38]], dtype=float)

# Находим собственные значения и собственные векторы
eigenvalues, eigenvectors = np.linalg.eig(A)

# Выводим результаты
print("Собственные числа:")
print(eigenvalues)

print("\nСобственные векторы:")
print(eigenvectors)