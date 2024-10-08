import logging

logging.basicConfig(filename='prog\Calculate.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    """Decorate
    """
    def wrapper(a, b, operand):
        """Closure

        Логируется информация о том какие операнды и какая арифметическая операция собираются поступить на вход функции.
        Затем внутри того же closure следует сам вызов функции calculate(...).
        А затем, после этого снова логирование, но уже с результатом выполнения вычисления, проделанного в этой функции.

        Возвращает результат выражения
        """
        logging.info(f'Вызов функции {func.__name__} с параметрами: a={a}, b={b}, operand="{operand}"')
        result = func(a, b, operand)
        logging.info(f'Результат выполнения функции {func.__name__}: {result}')
        return result
    return wrapper

@log_decorator
def calculate(a, b, operand):
    """
    Функция для выполнения арифметических операций.

    Функция получает два числа и арифметическую операцию.
    Определяет какая это из операций: '+', '-', '*', '/'

    Результат является число
    """
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif operand == '/':
        if b != 0:
            return a / b
        else: 
            return 'Нельзя делить на ноль'
    else:
        return 'Неизвестная операция'

def main():
    """
    Главная функция для запуска калькулятора.
    
    Запрашивает у пользователя ввод двух чисел и операции.
    
    Выводит результат вычисления.
    """
    a, operand, b = map(str, input("Введите выражение ").split())
    print("Результат выражения ", calculate(int(a), int(b), operand))
    
#main()

def test_calculate():
    assert calculate(1, 2, '+') == 3, 'dont work'
    assert calculate('1','2','+') == 3, 'dont work'
    assert calculate(5, 0, '/') == 'Нельзя делить на ноль', 'dont work'
    assert calculate(1, 2, '*') == 2, 'dont work'
    assert calculate(1, 2, '-') == -1, 'dont work'

test_calculate()