import sys
import os

# Добавляем папку src в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Импортируем функцию из utils.py
from src.utils import read_transactions


# Тест
def test_read_transactions():
    # Путь к файлу операций
    file_path = os.path.join(os.path.dirname(__file__), '../data/operations.json')

    # Тестируем, что функция возвращает список, если файл существует
    transactions = read_transactions(file_path)

    assert isinstance(transactions, list)
    # Проверка на "пустоту" файла
    if transactions:
        assert isinstance(transactions[0], dict)
