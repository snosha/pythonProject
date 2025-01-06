from typing import Any, Dict, List


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Аргументы:
        data (List[Dict[str, Any]]): Список словарей с ключом 'date'.
        descending (bool): Порядок сортировки (по убыванию по умолчанию).

    Возвращает:
        List[Dict[str, Any]]: Отсортированный список.
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)


# Пример использования
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Сортировка по убыванию (по умолчанию)
print(sort_by_date(data))

# Сортировка по возрастанию
print(sort_by_date(data, descending=False))
