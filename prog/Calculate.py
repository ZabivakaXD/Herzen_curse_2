import logging

logging.basicConfig(filename='prog\Calculate.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def log_decorator(func):
    """Decorate
    """
    def wrapper(numbers, operand, tolerance):
        """Closure

        Логируется информация о том какие операнды и какая арифметическая операция собираются поступить на вход функции.
        Затем внутри того же closure следует сам вызов функции calculate(...).
        А затем, после этого снова логирование, но уже с результатом выполнения вычисления, проделанного в этой функции.

        Возвращает результат выражения
        """
        logging.info(f'Вызов функции {func.__name__} с параметрами: numbers={numbers}, operand="{operand}", tolerance={tolerance}')
        result = func(numbers, operand, tolerance)
        logging.info(f'Результат выполнения функции {func.__name__}: {result}')
        return result
    return wrapper

@log_decorator
def calculate(numbers, operand, tolerance):
    """
    Функция для выполнения арифметических операций.

    Функция получает числа и арифметическую операцию.
    Определяет какая это из операций

    Результатом является число
    """
    if tolerance == "":
        int_tolerance = 6
    else: 
        int_tolerance = convert_precision(float(tolerance))
        
    if int_tolerance == None:
        return "Неправильный вид значения округления"
    
    result = None
    if operand == '+':
        result = 0
        for number in numbers:
            result += number
    elif operand == '-':
        result = numbers[0]
        numbers.pop(0)
        for number in numbers:
            result -= number
    elif operand == '*':
        result = numbers[0]
        numbers.pop(0)
        for number in numbers:
            result *= number
    elif operand == '/':
        if 0 not in numbers:
            result = numbers[0]
            numbers.pop(0)
            for number in numbers:
                result /= number
        else: 
            return 'Нельзя делить на ноль'
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
    
    if result == None:
        return "Неизвестная операция"
    else: 
        return round(result, int_tolerance)

def convert_precision(tolerance):
    import math
    
    int_tolerance = int(math.log10(tolerance))
    
    if tolerance == 10**int_tolerance and int_tolerance < 0:
        return -int_tolerance
    else: 
        return None
    
def expression_generator(file):
    """
    Генератор для построчного чтения и возврата арифметических выражений из файла.
    """
    for line in file:
        yield line.strip()  # Убираем лишние пробелы и символы переноса строки

def cmd_read():
    """
    Главная функция для запуска калькулятора.
    
    Запрашивает у пользователя ввод чисел и операции.
    
    Выводит результат вычисления.
    """
    numbers = list(map(str, input("Введите числа ")).split(" "))
    operand = str(input("Введите арифметическая операцию "))
    tolerance = str(input("Введите точность "))
    print("Результат выражения ", calculate(numbers, operand, tolerance))
    
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

file_read()
#cmd_read()

def test_calculate():
    assert calculate(1, 2, '+') == 3, 'dont work'
    assert calculate('1','2','+') == 3, 'dont work'
    assert calculate(5, 0, '/') == 'Нельзя делить на ноль', 'dont work'
    assert calculate(1, 2, '*') == 2, 'dont work'
    assert calculate(1, 2, '-') == -1, 'dont work'

#test_calculate()