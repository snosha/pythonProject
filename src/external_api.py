import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертирует сумму в валюте (USD, EUR) в рубли (RUB)"""

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Currency {currency} not supported. Only USD and EUR are supported.")

    # Формируем параметры для запроса
    params = {
        "amount": amount,
        "from": currency,
        "to": "RUB"
    }
    headers = {
        "apikey": API_KEY
    }

    # Делаем запрос к внешнему API
    response = requests.get(API_URL, params=params, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates from API")

    data = response.json()

    if not data.get("success"):
        raise Exception("API returned an error")

    # Получаем результат конвертации
    return data["result"]
