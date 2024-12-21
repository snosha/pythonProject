import pytest
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