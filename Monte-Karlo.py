import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Для вирішення задачі спочатку визначаємо функцію та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок
n_points = 10000

# Генеруємо кількість випадкових x з діапазону [a, b]
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, f(b), n_points)

# Робимо обчислення площі під кривою методом Монте-Карло
under_curve = (y_random < f(x_random))
area_under_curve = np.sum(under_curve) / n_points * (b - a) * f(b)

# Реалізуємо вирішення задачі аналітичним методом
analytical_solution, _ = quad(f, a, b)

print(f"Обчислене значення інтеграла методом Монте-Карло: {area_under_curve}")
print(f"Аналітичне значення інтеграла: {analytical_solution}")

# Графік функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)  # Малюємо функцію

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання випадкових точок на графік
ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()