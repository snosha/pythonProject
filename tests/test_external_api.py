import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub

# Тест на успешную конвертацию
@patch("requests.get")
def test_convert_to_rub_success(mock_get):
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
    with pytest.raises(ValueError):
        convert_to_rub(1, "GBP")  # GBP не поддерживается

# Тест на ошибку при ошибке API
@patch("requests.get")
def test_convert_to_rub_failure(mock_get):
    # Мокируем ошибку при запросе
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {"success": False}

    with pytest.raises(Exception):
        convert_to_rub(1, "USD")

# Тест на ошибку при некорректном ответе
@patch("requests.get")
def test_convert_to_rub_invalid_response(mock_get):
    # Мокируем некорректный ответ от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"success": False}

    with pytest.raises(Exception):
        convert_to_rub(1, "USD")
