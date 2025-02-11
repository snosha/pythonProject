from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по состоянию.

    Аргументы:
        data (List[Dict[str, Any]]): Список словарей с ключом 'state'.
        state (str): Состояние для фильтрации (по умолчанию 'EXECUTED').

    Возвращает:
        List[Dict[str, Any]]: Отфильтрованный список словарей.
    """
    return [item for item in data if item['state'] == state]


# Создаем список словарей
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Пример с использованием по умолчанию 'EXECUTED'
print(filter_by_state(data))

# Пример с передачей 'CANCELED'
print(filter_by_state(data, 'CANCELED'))
