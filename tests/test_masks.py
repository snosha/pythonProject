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


from src.widget import get_date  # Импортируем вашу функцию

def test_get_date_valid():
    input_date = "2024-03-11T02:26:18.671407"
    expected_output = "11.03.2024"  # Ожидаем, что дата будет в формате DD.MM.YYYY
    assert get_date(input_date) == expected_output


def test_get_date_edge_case():
    # Проверяем крайний случай для даты
    input_date = "2024-01-01T00:00:00.000000"
    expected_output = "01.01.2024"  # Ожидаем, что дата будет в формате DD.MM.YYYY
    assert get_date(input_date) == expected_output