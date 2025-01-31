import os
import sys
from unittest.mock import mock_open, patch

from src.finance import read_transactions_from_csv

# Добавляем путь к папке src в sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))


def test_read_transactions_from_csv():
    # Подготавливаем mock-данные для CSV
    csv_data = """date,amount,category
2023-10-01,100,Food
2023-10-02,200,Transport"""

    # Ожидаемый результат
    expected = [
        {"date": "2023-10-01", "amount": "100", "category": "Food"},
        {"date": "2023-10-02", "amount": "200", "category": "Transport"},
    ]

    # Используем patch для имитации открытия файла
    with patch("builtins.open", mock_open(read_data=csv_data)):
        # Вызываем функцию и проверяем результат
        result = read_transactions_from_csv("dummy_file.csv")
        assert result == expected, "Функция вернула неверные данные"


def test_read_transactions_from_csv_file_not_found():
    # Имитируем ситуацию, когда файл не найден
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions_from_csv("non_existent_file.csv")
        assert result == [], "Функция должна вернуть пустой список при отсутствии файла"
