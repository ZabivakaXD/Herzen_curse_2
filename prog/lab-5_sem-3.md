# Лабораторная работа №5

## Задание 1.1

 Создайте свой класс-итератор class RandomNumberIterator, который, в ходе итерирования по такому итератору, генерирует случайные числа в количестве и в диапазоне, которые передаются в конструктор в виде списка параметров.

```
 import random

class RandomNumberIterator:
    def __init__(self, parametrs):
        self.count = parametrs[0]  # Количество случайных чисел
        self.start = parametrs[1]  # Начало диапазона
        self.end = parametrs[2]    # Конец диапазона
        self.generated = 0  # Счетчик сгенерированных чисел

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:
            self.generated += 1
            return random.randint(self.start, self.end)
        else:
            raise StopIteration

def main():
    parametrs = [5, 1, 10]
    random_iterator = RandomNumberIterator(parametrs)
    for number in random_iterator:
        print(number)
        
main()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/randomNumber_iterator.py)

## Задание 1.2

Решите задачу 1.1 уже с использованием генераторной функции, использующей ключевое слово yield. В качестве аргументов она должна
принимать количество элементов и диапазон

```
import random

def random_number_generator(parameters):
    for _ in range(parameters[0]):
        yield random.randint(parameters[1], parameters[2])

def main():
    parametrs = [5, 1, 10]
    for number in random_number_generator(parametrs):
        print(number)
    
main()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/randomNumber_generator.py)

## Задание 1.3

Сделайте две функции-генератора. Первый генератор создаёт ряд Фибоначчи, а второй генератор добавляет значение 10 к каждому числу.
Вызовете эти генераторы так, чтобы сгенерировать некоторое количество чисел Фибоначчи с добавлением числа 10 к каждому числу

```
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def add_ten_generator(fib_gen):
    for num in fib_gen:
        yield num + 10

def main():
    n = 10  # Количество чисел Фибоначчи
    fib_gen = fibonacci_generator(n)
    add_ten_gen = add_ten_generator(fib_gen)

    for number in add_ten_gen:
        print(number)

main()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/fib_numbers_with_plus_10.py)

## Задание 1.4

Напишите программу, на вход к которой подается список стран и городов для каждой страны. Затем по названиям городов из ещё одного
списка выводится в какой стране расположен каждый город.

```
def find_country_by_city(countries_cities, cities_to_find):
    dict_city_country = {}
    for country in countries_cities: 
        many_city = countries_cities.get(country)
        for city in many_city:
            dict_city_country[city] = country
    
    for need_to_find in cities_to_find:
        result = dict_city_country.get(need_to_find)
        if result != None:
            print(need_to_find, "-", result)
        else:
            print("Такой страны нет в списке")         

def main():
    countries_cities = {
        "Россия": ["Москва", "Санкт-Петербург", "Сургут"],
        "США": ["Вашингтон", "Нью-Йорк", "Лос-Анджелес"],
        "Франция": ["Париж", "Лион", "Марсель"]
    }
        
    cities_to_find = ["Москва", "Нью-Йорк", "Париж", "Токио"]
    find_country_by_city(countries_cities, cities_to_find)
    
main()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/many_diferent_city.py)

## Задание 2.1

Напишите класс менеджера контекста Timer, который умеет считать
время в секундах, затраченное на некоторые вычисления внутри соответствующего блока with с помощью функции perf_counter модуля time. Используйте этот менеджер контекста для определения времени на вычисления достаточно большого количества чисел Фибоначчи (например миллиона) в цикле с помощью отдельной функциигенератора

```
import time

class Timer:
    """Менеджер контекста для измерения времени выполнения блока кода."""
    def __enter__(self):  # Начало отсчета времени
        self.start = time.perf_counter()  
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # Конец отсчета времени
        self.end = time.perf_counter()  
        self.elapsed = self.end - self.start
        print(f"Время выполнения: {self.elapsed:.2f} секунд")

def fibonacci_generator(n):
    """Функция-генератор чисел Фибоначчи до n элементов."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    N = 10**6  # Количество чисел Фибоначчи
    with Timer():
        for _ in fibonacci_generator(N):
            pass

main()
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Fibonaci_Timer.py)

## Задание 2.2

Напишите класс менеджера контекста BatchCalculatorContextManager,
для вашего проекта калькулятора из предыдущих лабораторных работ. Этот менеджер контекста должен уметь открывать и закрывать. текстовый файл, в каждой строчке которого записана пара чисел в
сочетании с арифметической операцией над ними в виде простого
арифметического выражения без пробелов. В сочетании с дополнительной функцией генератором и вашим менеджером контекста прочитайте все строчки текстового файла и вызовите нужное число раз
функцию calculate(...) вашего калькулятора, чтобы распечатать
все результаты на экране.

```
class BatchCalculatorContextManager:
    """
    Менеджер контекста для работы с файлом, содержащим арифметические выражения.
    Открывает и закрывает файл.
    """
    def __init__(self, file_path):
        self.file_path = file_path  # Путь к файлу
        self.file = None            # Объект файла

    def __enter__(self):
        # Открываем файл на чтение
        self.file = open(self.file_path, 'r', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Закрываем файл
        if self.file:
            self.file.close()
```

```
def file_read():
    """
    Главная функция для запуска калькулятора.
    
    Читает из файла все выражения.
    
    Выводит результат вычисления.
    """
    file_path = "prog\expressions.txt"  # Имя файла с арифметическими выражениями
    work_numbers = "0123456789"
    work_opertand = "+ - * /"
    
    # Обрабатываем файл с помощью менеджера контекста и генератора
    with BatchCalculatorContextManager(file_path) as file:
        for expression in expression_generator(file):
            number = ""
            numbers = []
            for char in expression:
                if char in work_numbers:
                    number += char
                elif char == " ":
                    next
                elif char in work_opertand:
                    operand = char
                    numbers.append(int(number))
                    number = ""
                else:
                    print("Неправильно записано выражение в файле")
            numbers.append(int(number))
            result = calculate(numbers, operand, "")
            print(f"{expression} = {result}")
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Calculate.py)

## Задание 2.3

Установите локально на свой компьютер объектную базу данных MongoDB.
Установите с помощью менеджера пакетов pip или conda, в зависимости от того чем вы пользуетесь, пакет pymongo для подключения к
базам данных MongoDB. Например команда для pip:
pip install pymongo. С помощью инструмента MongoDB Shell создайте нового пользователя с правами админа, к примеру. Введите в
командной строке mongosh без аргументов и уже в командной строке
внутри MongoDB Shell введите:
```
db.createUser({
user: "myUserAdmin",
pwd: "abc123",
roles: [
{ role: "userAdminAnyDatabase", db: "admin" },
"readWriteAnyDatabase"
]
})
```
Затем выйдите из MongoDB Shell (Введите exit или нажмите CtrlD). Перезайдите снова в MongoDB Shell с помощью команды mongosh
-u myUserAdmin в командной строке и введя пароль abc123. Тем самым вы залогинетесь в базу MongoDB под новой учётной записью.
Создайте пустую базу данных myshinynewdb с помощью команды use
myshinynewdb. Добавьте коллекцию user в эту базу данных с одной
единственной записью: db.user.insert({name: "Ada Lovelace", age:
205}). Коллекция будет создана автоматически. Напишите класс менеджера контекста для управляемого подключения к MondoDB и отключения от неё. Внутри блока with с помощью вызова метода
user_collection.find({'age': 205}) найдите вашу запись об
"Ada␣Lovelace" и распечатайте её в терминале.

```
from pymongo import MongoClient

class MongoDBConnectionContextManager(object):
    """MongoDB Connection Context Manager"""
    def __init__(self, host='localhost', port=27017, username='admin', password='admin'):
        self.host = host; self.port = port
        self.username = username; self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            self.host, self.port,
            username=self.username, password=self.password,
            authMechanism='SCRAM-SHA-1'
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# Использование контекстного менеджера
mongo = MongoDBConnectionContextManager(host='localhost', port=27017, username='myUserAdmin', password='abc123')
with mongo as mongo_connection_context:
    collection = mongo_connection_context.connection['myshinynewdb']['user']
    user = collection.find({'age': 205})
    print(next(user))
```
[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/Work_with_Mongo.py)