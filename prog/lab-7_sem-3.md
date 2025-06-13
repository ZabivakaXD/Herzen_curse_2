# Лабораторная работа №7

## Цель работы

Освоить принципы использования механизма обработки исключительных ситуаций при считывании/записи в файл на примере функции для сохранения лога операций и чтения настроек для работы калькулятора из файла. 

## Комментарии по выполнению

Работу можно структурировать на следующие части:

Применить принципы модульного тестирования и с использованием библиотеки unittest (см. пример в repl.it, сайт с официальной документацией и русско-язычный ресурс по unittest) протестировать возможные варианты работы программы по работе с файлом. Обратить внимание на возникновение исключительных ситуаций в этих операциях. Выделить ситуации при которых необходимо вручную поднять определенное исключение. 

В стартовом борде рассмотрен способ тестирования поднятия исключения в случае, когда мы не используем специальных библиотек для считывания/записи в файл. Вам же нужно протестировать срабатывание исключений при использовании библиотек configparser (для чтения) и csv (для записи) файлов.

### Опишем конкретные аспекты задания ниже.

1. Модульное тестирование с unittest

Можно вместо образца борда по ссылке в начале задания покрыть тестами функционал вашего калькулятора из предыдущих лабораторных работ.

Шаблон для тестирования с помощью unittest может выглядеть так:

```
import unittest

class TestSomeFunc(unittest.TestCase): # создаем свой класс для тестов

     def firsttestcase(self): # внутри функции один или несколько тестовых
         self.assertEqual(2*2, 4) # случаев, которые проверяют какие-то 
         # близкие предположения
         

     # ...
     def secondtestcase(self): # вторая группа тестов
         pass

```

unittest.main(verbosity=1)     # запуск тестов
Пример тестирования двух функций convert_precision и two_sum, которую мы создавали ранее. Нюанс тестирования в repl.it и PyCharm. В repl.it  тесты запускаются вручную с помощью вкладки Shell (справа) (пример борда), в PyCharm требуется закомментировать запуск тестов с помощью: 
```
unittest.main(verbosity=1)
```

2. Тестирование с помощью pytest

Можно вместо образца борда по ссылке в начале задания покрыть тестами функционал вашего калькулятора из предыдущих лабораторных работ.

По аналогии с предыдущим пунктом 2.

Перепешите те же самые тесты с помощью фреймворка pytest. Сравните его использование с фреймворком unittest.

```
import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO

# Добавляем путь к исходному файлу
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from Calculate import calculate, convert_precision, BatchCalculatorContextManager

class TestCalculate(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate([2, 3], '+', '0.1', 1), 5)
        self.assertEqual(calculate([5, 2], '-', '0.01', 2), 3)
        self.assertEqual(calculate([3, 4], '*', '0.001', 3), 12)
        self.assertEqual(calculate([10, 2], '/', '0.0001', 4), 5)
        self.assertEqual(calculate([10, 0], '/', '', 6), 'Нельзя делить на ноль')
    
    def test_statistical_operations(self):
        self.assertEqual(calculate([1, 2, 3, 4], 'среднее значение', '0.1', 1), 2.5)
        self.assertEqual(calculate([1, 2, 3, 4, 5], 'медиана', '0.01', 2), 3)
    
    def test_invalid_operations(self):
        self.assertEqual(calculate([1, 2, 3], 'invalid', '', 6), "Неизвестная операция")
        self.assertEqual(calculate([1, 2, 3], '/', 'abc', 6), "Неправильный вид значения округления")
    
    def test_precision(self):
        self.assertEqual(calculate([1, 3], '/', '0.001', 3), 0.333)
        self.assertEqual(calculate([10, 3], '/', '0.0001', 4), 3.3333)

class TestConvertPrecision(unittest.TestCase):
    def test_valid_precision(self):
        self.assertEqual(convert_precision(0.1), 1)
        self.assertEqual(convert_precision(0.001), 3)
        self.assertEqual(convert_precision(0.00001), 5)
    
    def test_invalid_precision(self):
        self.assertIsNone(convert_precision(0.123))
        self.assertIsNone(convert_precision(1.0))
        self.assertIsNone(convert_precision(10))

class TestContextManager(unittest.TestCase):
    def test_file_operations(self):
        test_file = "test_file.txt"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("test content")
        
        with BatchCalculatorContextManager(test_file) as file:
            content = file.read()
            self.assertEqual(content, "test content")
        
        os.remove(test_file)
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with BatchCalculatorContextManager("non_existent_file.txt") as file:
                pass

class TestExpressionProcessing(unittest.TestCase):
    @patch('builtins.print')
    def test_expression_processing(self, mock_print):
        test_file = "expressions.txt"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write("10 2 /\n")
            f.write("5 3 +\n")
        
        # Подменяем стандартный вывод
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            # Импортируем и вызываем file_read здесь
            from Calculate import file_read
            file_read()
            output = sys.stdout.getvalue()
            self.assertIn("10 2 / = 5", output)
            self.assertIn("5 3 + = 8", output)
        finally:
            sys.stdout = original_stdout
            os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
```

[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/unittest_calculator.py)

```
import pytest
import os
import sys
from io import StringIO
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from Calculate import calculate, convert_precision, BatchCalculatorContextManager, file_read

# Тесты для calculate
@pytest.mark.parametrize("numbers, operand, tolerance, precision, expected", [
    ([2, 3], '+', '0.1', 1, 5),
    ([5, 2], '-', '0.01', 2, 3),
    ([3, 4], '*', '0.001', 3, 12),
    ([10, 2], '/', '0.0001', 4, 5),
    ([10, 0], '/', '', 6, 'Нельзя делить на ноль'),
    ([1, 2, 3, 4], 'среднее значение', '0.1', 1, 2.5),
    ([1, 2, 3, 4, 5], 'медиана', '0.01', 2, 3),
    ([1, 2, 3], 'invalid', '', 6, "Неизвестная операция"),
    ([1, 3], '/', '0.001', 3, 0.333),
])
def test_calculate(numbers, operand, tolerance, precision, expected):
    assert calculate(numbers, operand, tolerance, precision) == expected

# Тесты для convert_precision
@pytest.mark.parametrize("tolerance, expected", [
    (0.1, 1),
    (0.001, 3),
    (0.00001, 5),
    (0.123, None),
    (1.0, None),
    (10, None),
])
def test_convert_precision(tolerance, expected):
    assert convert_precision(tolerance) == expected

# Тесты для контекстного менеджера
def test_context_manager(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content", encoding='utf-8')
    
    with BatchCalculatorContextManager(str(test_file)) as file:
        content = file.read()
        assert content == "test content"

def test_context_manager_file_not_found():
    with pytest.raises(FileNotFoundError):
        with BatchCalculatorContextManager("non_existent_file.txt") as file:
            pass

# Тест обработки выражений
def test_file_read_processing(capsys, tmp_path):
    test_file = tmp_path / "expressions.txt"
    test_file.write_text("10 2 /\n5 3 +", encoding='utf-8')
    
    # Мокаем путь к файлу
    with patch('calculator.BatchCalculatorContextManager') as mock_manager:
        mock_manager.return_value.__enter__.return_value = [
            "10 2 /",
            "5 3 +"
        ]
        
        file_read()
        captured = capsys.readouterr()
        assert "10 2 / = 5" in captured.out
        assert "5 3 + = 8" in captured.out

# Тест обработки ошибок
def test_invalid_expression(capsys, tmp_path):
    test_file = tmp_path / "expressions.txt"
    test_file.write_text("10 a /", encoding='utf-8')
    
    with patch('calculator.BatchCalculatorContextManager') as mock_manager:
        mock_manager.return_value.__enter__.return_value = ["10 a /"]
        
        file_read()
        captured = capsys.readouterr()
        assert "Неправильно записано выражение в файле" in captured.out
```

[ссылка на файл](https://github.com/ZabivakaXD/Herzen_curse_2/blob/main/prog/pytest_calculator.py)