import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x
x = np.linspace(0, 10, 100)

# Первая функция: f(x) = sin(x)
f_x = np.sin(x)

# Вторая функция: g(x) = cos(x)
g_x = np.cos(x)

# Третья функция: h(x) = e^(-x) * sin(2x)
h_x = np.exp(-x) * np.sin(2 * x)

# Первое окно с двумя графиками
plt.figure(1)
plt.subplot(2, 1, 1)  # Два графика вертикально
plt.plot(x, f_x, label='f(x) = sin(x)', color='blue')
plt.title('Графики функций')
plt.ylabel('f(x)')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x, g_x, label='g(x) = cos(x)', color='red')
plt.ylabel('g(x)')
plt.legend()
plt.grid()

plt.xlabel('x')
plt.tight_layout()  # Для лучшего расположения графиков
plt.show()

# Второе окно с одним графиком
plt.figure(2)
plt.plot(x, h_x, label='h(x) = e^(-x) * sin(2x)', color='green')
plt.title('График функции h(x)')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend()
plt.grid()
plt.show()
