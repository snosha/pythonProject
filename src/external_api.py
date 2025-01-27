import os
import requests
import json
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму в валюте (USD, EUR) в рубли (RUB).

    Параметры:
    amount (float): Сумма для конвертации.
    currency (str): Валюта, из которой нужно конвертировать. Допустимые значения: 'USD', 'EUR'.

    Возвращает:
    float: Сумма в рублях (RUB).

    Исключения:
    ValueError: Если указана неподдерживаемая валюта (не 'USD' или 'EUR').
    Exception: Если произошла ошибка при запросе к API или возвращен некорректный ответ.
    """
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


def convert_transaction_from_json(file_name: str) -> float:
    file_path = os.path.join("data", file_name)  # Путь к файлу operations.json
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transaction = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_name} не найден в папке data.")
    except json.JSONDecodeError:
        raise ValueError("Ошибка при чтении или парсинге JSON файла.")

    # Извлекаем информацию из транзакции
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    # Конвертируем в рубли
    return convert_to_rub(amount, currency)

