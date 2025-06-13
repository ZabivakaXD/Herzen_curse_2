# Лабораторная работа №3

## Задание 1.1

Модернизируйте калькулятор из задач 1.2 и 1.4 Лабораторной работы
№ 2. Добавьте к калькулятору такую настройку как точность вычислений, которая передаётся в виде keyword параметра tolerance со
значением по умолчанию 1e−6. На основе переданного значения этого
параметра извлеките с помощью вычислений порядок этого значения
(например 6 для 1e−6) в виде отдельной функции convert_precision,
вызываемой из calculate. Задокументируйте convert_precision и
дополните документацию к calculate в коде. Извлечённый порядок
используйте для округления итогового результата в функции calculate.
Покройте (напишите) дополнительными тестами convert_precision
и calculate в связи с появлением tolerance с помощью пакета pytest
или стандартных unittest Python по выбору.
```
def convert_precision(tolerance):
    import math
    
    int_tolerance = int(math.log10(tolerance))
    
    if tolerance == 10**int_tolerance and int_tolerance < 0:
        return -int_tolerance
    else: 
        return None
```
```
if tolerance == "":
        int_tolerance = 6
    else: 
        int_tolerance = convert_precision(float(tolerance))
        
    if int_tolerance == None:
        return "Неправильный вид значения округления"
...
return round(result, int_tolerance)
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Calculate.py)

## 1.2

Модернизируйте калькулятор из задачи 1.1. Добавьте переменное количество неименоманных аргументов (операндов, ∗args) после параметра action и перед keyword параметром tolerance. К списку
поддерживаемых действий добавьте вычисление таких величин как
среднее значение (medium), дисперсия (variance), стандартное отклонение (std_deviation), медиана (median, q2, второй квартиль) и межквартильный размах (q3 - q1, разница третьего и первого квартилей).
Покройте новые реализованные функции и функцию calculate дополнительными юнит-тестами

```
 elif operand == 'среднее значение':
        result = sum(numbers)/len(numbers)
    elif operand == 'дисперсия':
        medium = sum(numbers)/len(numbers)
        result = sum((xi - medium) ** 2 for xi in numbers) / len(results)
    elif operand == 'стандартное отклонение':
        medium = sum(numbers)/len(numbers)
        result = (sum((xi - medium) ** 2 for xi in numbers) / (len(results) - 1))**0.5
    elif operand == 'медиана':
        mid = len(numbers) // 2
        sorted_numbers = sort(list(numbers))
        if mid % 2 == 0:
            result = (sorted_numbers[mid] + sorted_numbers[mid + 1]) / 2
        else:
            result = sorted_numbers[mid // 2 + 1]
    elif operand == 'первый квартиль':
        mid = len(numbers) // 2
        sorted_numbers = sort(list(numbers))
        if mid % 2 == 0:
            numbers = numbers[0:mid + 1]
            mid = len(numbers) // 2
            result = (numbers[mid] + numbers[mid + 1]) / 2
        else:
            numbers = numbers[0:mid + 1]
            mid = len(numbers) // 2
            result = numbers[mid + 1]
    elif operand == 'третий квартиль':
        mid = len(numbers) // 2
        sorted_numbers = sort(list(numbers))
        if mid % 2 == 0:
            numbers = numbers[mid: -1]
            mid = len(numbers) // 2
            result = (numbers[mid] + numbers[mid + 1]) / 2
        else:
            numbers = numbers[mid: -1]
            mid = len(numbers) // 2
            result = numbers[mid // 2 + 1]
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Calculate.py)