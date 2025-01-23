import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму в рубли.

    Args:
        amount (float): Сумма для конвертации.
        currency (str): Исходная валюта (например, USD или EUR).

    Returns:
        float: Сумма в рублях.
    """
    if currency == "RUB":
        return float(amount)

    headers = {"apikey": API_KEY}
    params = {"from": currency, "to": "RUB", "amount": amount}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", 0))
    except (requests.RequestException, ValueError) as e:
        print(f"Ошибка при конвертации валюты: {e}")
        return 0.0
