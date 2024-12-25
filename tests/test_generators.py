import pytest

# Генераторы
def filter_by_currency(transactions, currency_code):
    """Генератор, который поочередно выдает транзакции с заданной валютой."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, который возвращает описание транзакции по очереди."""
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, end: int):
    """Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]

# Пример данных для транзакций
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021-01-01T10:00:00",
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Payment for services",
        "from": "Account 1",
        "to": "Account 2"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2021-01-02T10:00:00",
        "operationAmount": {
            "amount": "200.00",
            "currency": {"name": "EUR", "code": "EUR"}
        },
        "description": "Payment for goods",
        "from": "Account 3",
        "to": "Account 4"
    }
]

# Фикстура для транзакций
@pytest.fixture
def transactions_data():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2021-01-01T10:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Payment for services",
            "from": "Account 1",
            "to": "Account 2"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2021-01-02T10:00:00",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "EUR", "code": "EUR"}
            },
            "description": "Payment for goods",
            "from": "Account 3",
            "to": "Account 4"
        }
    ]

# Тесты для filter_by_currency
def test_filter_by_currency(transactions_data):
    usd_transactions = list(filter_by_currency(transactions_data, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"

def test_filter_by_currency_empty_list():
    empty_transactions = []
    usd_transactions = list(filter_by_currency(empty_transactions, "USD"))
    assert len(usd_transactions) == 0

def test_filter_by_currency_no_matches(transactions_data):
    """Проверка, что генератор не возвращает транзакции, если валюта не совпадает."""
    # Фильтруем по валюте, которой нет в данных
    eur_transactions = list(filter_by_currency(transactions_data, "GBP"))  # Пример валюты, которой нет в данных
    assert len(eur_transactions) == 0  # Ожидаем пустой список, так как "GBP" нет в данных


# Тесты для transaction_descriptions
def test_transaction_descriptions(transactions_data):
    descriptions = list(transaction_descriptions(transactions_data))
    assert len(descriptions) == 2
    assert descriptions[0] == "Payment for services"
    assert descriptions[1] == "Payment for goods"

def test_transaction_descriptions_empty_list():
    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert len(descriptions) == 0

# Тесты для card_number_generator
def test_card_number_generator_format():
    card_numbers = list(card_number_generator(1, 5))
    assert len(card_numbers) == 5
    assert card_numbers[0] == "0000 0000 0000 0001"
    assert card_numbers[4] == "0000 0000 0000 0005"

def test_card_number_generator_range():
    card_numbers = list(card_number_generator(9999999999999990, 9999999999999995))
    assert len(card_numbers) == 6
    assert card_numbers[0] == "9999 9999 9999 9990"
    assert card_numbers[5] == "9999 9999 9999 9995"

def test_card_number_generator_single_number():
    card_numbers = list(card_number_generator(1234567890123456, 1234567890123456))
    assert len(card_numbers) == 1
    assert card_numbers[0] == "1234 5678 9012 3456"

# Параметризация для разных валют
@pytest.mark.parametrize("currency_code, expected_length", [("USD", 1), ("EUR", 1), ("GBP", 0)])
def test_filter_by_currency_parametrized(transactions_data, currency_code, expected_length):
    filtered_transactions = list(filter_by_currency(transactions_data, currency_code))
    assert len(filtered_transactions) == expected_length

if __name__ == "__main__":
    pytest.main()
