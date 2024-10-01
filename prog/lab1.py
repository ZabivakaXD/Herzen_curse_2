def calculate(a, b, opperand):
    if opperand == '+':
        return a + b
    elif opperand == '-':
        return a - b
    elif opperand == '*':
        return a * b
    elif opperand == '/':
        return a / b
    else:
        return 'unknown operation'

def test_calculate():
    assert calculate(1, 2, '+') == 3, 'dont work'
def test_calculate1():
    assert calculate('1','2','+') == 3, 'dont work'
def test_calculate2():
    assert calculate(1, 2, '+') == 3, 'dont work'

test_calculate2()
