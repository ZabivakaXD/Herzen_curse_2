def calculate(a, b, operand):
    """
    Функция для выполнения арифметических операций.

    Функция получает два числа и арифметическую операцию.
    Определяет какая это из операций: '+', '-', '*', '/'

    Резульатом является число
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
