from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Generator[Dict, None, None]:
    """Генератор, который поочередно выдает транзакции с заданной валютой."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Генератор, который возвращает описание транзакции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]


# Список транзакций
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 876545344,
        "state": "EXECUTED",
        "date": "2020-05-15T10:45:10.126392",
        "operationAmount": {
            "amount": "4532.99",
            "currency": {"name": "EUR", "code": "EUR"}
        },
        "description": "Перевод с карты на карту",
        "from": "Счет 98765432109876543210",
        "to": "Счет 11223344556677889900"
    }
]

# 1. Использование filter_by_currency для валюты "USD"
usd_transactions = filter_by_currency(transactions, "USD")
print("USD Transactions:")
try:
    print(next(usd_transactions))  # Первая транзакция USD
    print(next(usd_transactions))  # Вторая транзакция USD
except StopIteration:
    print("No more USD transactions.")

# 2. Использование transaction_descriptions
descriptions = transaction_descriptions(transactions)
print("\nTransaction Descriptions:")
# Цикл for обрабатывает завершение генератора автоматически
for description in descriptions:
    print(description)

# 3. Использование card_number_generator
print("\nGenerated Card Numbers:")
for card_number in card_number_generator(1, 5):
    print(card_number)
