import pytest
from src.processing.sort import sort_by_date

def test_sort_by_date():
    """Тест сортировки по убыванию (по умолчанию)."""
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert sort_by_date(data) == expected

def test_sort_by_date_ascending():
    """Тест сортировки по возрастанию."""
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    expected = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    assert sort_by_date(data, descending=False) == expected

def test_sort_empty_list():
    """Тест сортировки пустого списка."""
    data = []
    expected = []
    assert sort_by_date(data) == expected

def test_sort_invalid_date_format():
    """Тест сортировки с некорректным форматом даты."""
    data = [
        {'id': 1, 'state': 'EXECUTED', 'date': 'invalid_date'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    # Ожидаем, что элемент с некорректной датой будет обрабатываться как строка
    expected = [
        {'id': 2, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 1, 'state': 'EXECUTED', 'date': 'invalid_date'}
    ]
    assert sort_by_date(data, descending=False) == expected
