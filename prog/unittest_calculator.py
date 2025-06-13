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