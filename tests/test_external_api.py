import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


# Тест на успешную конвертацию
@patch("requests.get")
def test_convert_to_rub_success(mock_get):
    """
    Тест на успешную конвертацию валюты с использованием API.
    Проверяется правильный ответ при успешной конвертации.
    """
    # Мокируем успешный ответ от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "result": 75.0  # Предположим, что 1 USD = 75 RUB
    }

    result = convert_to_rub(1, "USD")
    assert result == 75.0


# Тест на ошибку при неверной валюте
def test_convert_to_rub_invalid_currency():
    """
    Тест на ошибку при попытке конвертации с неверной валютой.
    Проверяется выброс исключения для неподдерживаемой валюты.
    """
    with pytest.raises(ValueError):
        convert_to_rub(1, "GBP")  # GBP не поддерживается


# Тест на ошибку при ошибке API
@patch("requests.get")
def test_convert_to_rub_failure(mock_get):
    """
    Тест на ошибку при запросе к API.
    Проверяется выброс исключения при получении ошибки от API.
    """
    # Мокируем ошибку при запросе
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {"success": False}

    with pytest.raises(Exception):
        convert_to_rub(1, "USD")


# Тест на ошибку при некорректном ответе
@patch("requests.get")
def test_convert_to_rub_invalid_response(mock_get):
    """
    Тест на ошибку при получении некорректного ответа от API.
    Проверяется выброс исключения при отсутствии успешного ответа.
    """
    # Мокируем некорректный ответ от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": False}

    with pytest.raises(Exception):
        convert_to_rub(1, "USD")
