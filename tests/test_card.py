import pytest
from src.masks import get_mask_card_number, get_mask_account


# Тестирование корректного номера карты
def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


# Тестирование номера карты нестандартной длины
def test_get_mask_card_number_short():
    assert get_mask_card_number("12345678") == "1234 56** **** 5678"


# Тестирование пустой строки
def test_get_mask_card_number_empty():
    with pytest.raises(ValueError):  # Изменено на ValueError
        get_mask_card_number("")