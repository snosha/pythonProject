import json
import os


def load_transactions() -> list[dict]:
    """
    Загружает данные о финансовых транзакциях из файла data/operations.json.
    Возвращает список словарей или пустой список, если файл некорректен.
    """
    file_path = os.path.join("data", "operations.json")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, FileNotFoundError, TypeError):
        pass
    return []
