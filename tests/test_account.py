import pytest
from src.masks import get_mask_account

# Тестирование корректного номера счета
def test_get_mask_account_valid():
    assert get_mask_account("12345678901234567890") == "**7890"

# Тестирование номера счета меньшей длины
def test_get_mask_account_short():
    assert get_mask_account("123") == "**123"
    assert get_mask_account("1") == "**1"

# Тестирование пустой строки
def test_get_mask_account_empty():
    with pytest.raises(ValueError):  # Изменено на ValueError
        get_mask_account("")


