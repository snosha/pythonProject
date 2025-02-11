import json
import os
from pathlib import Path


def load_transactions(file_path='data/operations.json'):
    # Преобразуем относительный путь в абсолютный
    absolute_path = Path(file_path).resolve()

    # Проверка, существует ли файл
    if not absolute_path.is_file():
        return []  # Если файл не найден, возвращаем пустой список

    try:
        with open(absolute_path, 'r') as file:
            transactions = json.load(file)

        # Проверка, является ли содержимое файлом списка
        if not isinstance(transactions, list):
            return []  # Если данные не список, возвращаем пустой список

        return transactions
    except json.JSONDecodeError:  # Обработка ошибок, если файл пуст или невалидный JSON
        return []  # Если ошибка при чтении, возвращаем пустой список
    except Exception as e:  # Ловим все другие возможные ошибки
        print(f"Unexpected error: {e}")  # Можно добавить логирование ошибок
        return []  # Возвращаем пустой список при ошибках
