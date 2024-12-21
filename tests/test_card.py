import pytest
from src.masks import get_mask_card_number

# Параметризованные тесты
@pytest.mark.parametrize("card_number, expected_result", [
    ("1234567890123456", "1234 56** **** 3456"),  # Тестируем корректный номер карты
    ("12345678", "1234 56** **** 5678"),  # Тестируем карту нестандартной длины
])
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result

# Параметризованный тест для пустой строки и пробела
@pytest.mark.parametrize("card_number, expected_result", [
    ("", None),  # Пустая строка должна вызвать ошибку
    (" ", "  ** ****  ")  # Пробел должен оставаться как есть
])
def test_get_mask_card_number_empty(card_number, expected_result):
    if card_number == "":
        with pytest.raises(ValueError):  # Ожидаем исключение ValueError для пустой строки
            get_mask_card_number(card_number)
    else:
        # Если передан пробел, проверим, что возвращается строка с пробелом
        result = get_mask_card_number(card_number)
        assert result == expected_result  # Проверяем, что пробел остался как есть
