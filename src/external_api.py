import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из указанной валюты (USD, EUR) в рубли (RUB).

    Параметры:
    amount (float): Сумма для конвертации.
    currency (str): Код валюты (например, 'USD' или 'EUR').

    Возвращает:
    float: Конвертированная сумма в рублях (RUB).
    """
    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Валюта {currency} не поддерживается. Только USD и EUR допустимы.")

    # Формируем параметры для запроса
    params = {
        "amount": amount,
        "from": currency,
        "to": "RUB"
    }
    headers = {
        "apikey": API_KEY
    }

    # Выполняем запрос к API
    response = requests.get(API_URL, params=params, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка API: статус {response.status_code}")

    data = response.json()

    if not data.get("success"):
        raise Exception("API вернуло ошибку")

    # Возвращаем результат конвертации
    return data["result"]


def process_transaction(some_transaction: dict) -> float:
    """
    Обрабатывает транзакцию и возвращает её сумму в рублях (RUB).
    Если валюта не RUB, выполняется конвертация с помощью convert_to_rub.

    Параметры:
    some_transaction (dict): Словарь с данными транзакции.

    Возвращает:
    float: Сумма транзакции в рублях (RUB).
    """
    try:
        # Извлекаем сумму и код валюты
        amount = float(some_transaction["operationAmount"]["amount"])
        currency = some_transaction["operationAmount"]["currency"]["code"]
    except (KeyError, TypeError, ValueError):
        raise ValueError("Некорректная структура данных транзакции.")

    # Если валюта не RUB, выполняем конвертацию
    if currency != "RUB":
        return convert_to_rub(amount, currency)

    # Если валюта RUB, возвращаем сумму без изменений
    return amount
