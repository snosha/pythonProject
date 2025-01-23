import os
import json


def read_transactions(file_path):
    """
    Читает JSON-файл с финансовыми транзакциями.

    Returns:
        list: Список транзакций (словари) или пустой список.
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Файл не содержит список транзакций.")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при чтении файла: {e}")

    return []


# Указание пути к файлу operations.json
# Определяем базовую директорию (где находится текущий скрипт)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем путь к operations.json в папке data
file_path = os.path.join(base_dir, "data", "operations.json")

# Читаем данные из файла
transactions = read_transactions(file_path)

# Выводим транзакции
if transactions:
    print("Транзакции:")
    for transaction in transactions:
        print(transaction)
else:
    print("Нет данных для отображения.")
