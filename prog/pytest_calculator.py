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