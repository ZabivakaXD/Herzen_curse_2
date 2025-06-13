# Лабораторная работа №4

## Задание 1.1
Написать функцию two_sum, которая возвращает кортеж из двух индексов элементов списка lst, таких что сумма элементов по этим индексам равна переменной target, Элемент по индексу может быть
выбран лишь единожды, значения в списке могут повторяться. Если в списке встречается больше чем два индекса, подходящих под условие - вернуть наименьшие из всех. Элементы находятся в списке в произвольном порядке. Алгоритм на двух циклах, сложность O(n2).
Пример использования:
```
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum(lst, target)
print(result)
```
Результат:
```
(0, 6)
```

```
def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)
    return None  # Возвращаем None, если подходящие индексы не найдены

lst = [3, 2, 1, 9, 5, 7, 6, 8, 4]
#lst = list(map(int, input("Введите числа ")).split(" "))
target = 8
#target = int(input("Введите цель "))
result = two_sum(lst, target)
print(result)
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Two_sum.py)

## Задание 1.2

Усовершенствуйте предыдущую задачу ??, добавив функцию
two_sum_hashed(lst, target) так, чтобы сложность алгоритма была
ниже: O(n) или O(n · log(n)).

```
def two_sum_hushed(lst, target):
    # Создаем список пар (значение, индекс)
    indexed_lst = [(value, index) for index, value in enumerate(lst)]
    print(indexed_lst)
    
    # Сортируем по значениям
    indexed_lst.sort(key=lambda x: x[0])
    print(indexed_lst)
    
    left = 0
    right = len(indexed_lst) - 1
    
    while left < right:
        current_sum = indexed_lst[left][0] + indexed_lst[right][0]
        
        if current_sum == target:
            # Возвращаем индексы в исходном списке, наименьшие по значению
            return tuple(sorted([indexed_lst[left][1], indexed_lst[right][1]]))
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return None  # Возвращаем None, если подходящие индексы не найдены

lst = [3, 2, 1, 9, 5, 7, 6, 8, 4]
#lst = list(map(int, input("Введите числа ")).split(" "))
target = 8
#target = int(input("Введите цель "))
result_fast = two_sum_hushed(lst, target)
print(result_fast)
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Two_sum.py)

## Задание 1.3

: Усовершенствуйте предыдущую задачу 1.2, добавив функцию , которая возвращает все наборы индексов, удовлетворяющих условию
суммы target. Пример использования:
```
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed_all(lst, target)
print(result)
```
Результат:
```
[(0,6), (1,5), (2,4)]
```

```
def two_sum_hushed_lst(lst, target):
    # Создаем список пар (значение, индекс)
    indexed_lst = [(value, index) for index, value in enumerate(lst)]
    print(indexed_lst)
    
    # Сортируем по значениям
    indexed_lst.sort(key=lambda x: x[0])
    print(indexed_lst)
    
    left = 0
    right = len(indexed_lst) - 1
    result = []
    
    while left < right:
        current_sum = indexed_lst[left][0] + indexed_lst[right][0]
        
        if current_sum == target:
            # Возвращаем индексы в исходном списке, наименьшие по значению
            result.append(sorted([indexed_lst[left][1], indexed_lst[right][1]]))
            indexed_lst.remove(indexed_lst[left])
            indexed_lst.remove(indexed_lst[right])
            left = 0
            right = len(indexed_lst) - 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    if len(result) != 0:         
        return result
    else:
        return None  # Возвращаем None, если подходящие индексы не найдены

lst = [3, 2, 1, 9, 5, 7, 6, 8, 4]
#lst = list(map(int, input("Введите числа ")).split(" "))
target = 8
#target = int(input("Введите цель "))
result_fast_lst = two_sum_hushed_lst(lst, target)
print(result_fast_lst)
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Two_sum.py)

## Задание 1.4

Повторите или изучите понятие мемоизации в Python. Реализуйте с
помощью мемоизации и рекурсии вычисление чисел Фибоначчи сначала рукаки с помощью вручную добавленого к рекурсивной функции
словаря с ранее вычисленными числами Фибоначчи, а затем с помощью декоратора @cache из стандартного модуля Python functools.

```
def fibonacci_hand(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_hand(n - 1, memo) + fibonacci_hand(n - 2, memo)
    return memo[n]

from functools import cache

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#n = int(input("Введите номер числа Фибоначи"))
n = 10
memo = {0 : 0}
print(f"{n} по номеру число Фибоначи это, {fibonacci(n)}")
print(f"{n} по номеру число Фибоначи это, {fibonacci_hand(n, memo)}")
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Fib_numb.py)

## Задание 2.1

Отправка почты через smtplib.

```
import smtplib
from secrets import login, password

email_from = login
email_to = "kbolotov2004@gmail.com"
subject = 'Test'
message = "Hello"

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, f'Subject:{subject}\n{message}')
server.quit()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Send_mail.py)

## Задание 2.2

Парсинг сайта погоды (wheather HTML parsing) на google.com и/или
на простом сайте wttr.in с помощью BeautifulSoup (v4).

```
import urllib.request
from bs4 import BeautifulSoup

url = "https://wttr.in/"
with urllib.request.urlopen(url) as request:
    html = request.read()

bs = BeautifulSoup(html, "html.parser")
texts = bs.text

index_place = texts.find("Weather report:") + 15
index_end_place = index_place + 30
place = texts[index_place:index_end_place].strip()

index_weather = texts.find(" °C")
index_start_weather = index_weather - 8
weather = texts[index_start_weather:index_weather].strip().replace('(', ' ').replace(')', '').split(' ')

index_wind = texts.find("km/h")
index_start_wind = index_wind - 4
wind = texts[index_start_wind:index_wind].strip()

print(bs.text)
print("Погода в", place)
print("Температура", weather[0], "°C, ощущается как", weather[1],"°C", chr(127777))
print("Скорость ветра", wind, "км/ч", chr(127744))
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/weather.py)

## Задание 2.3

С помощью бибилиотеки matplotlib вывести два окна с графиками
функций по личному выбору. В одном окне два графика двух разных
функций. В другом окне - один график ещё одной функции.

```
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
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/graphing.py)