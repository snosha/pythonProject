import pytest
from src.widget import get_date  # Импортируем вашу функцию


# Фикстура для корректной даты
@pytest.fixture
def valid_date():
    return "2024-03-11T02:26:18.671407"

# Фикстура для крайного случая с датой
@pytest.fixture
def edge_case_date():
    return "2024-01-01T00:00:00.000000"


def test_get_date_valid(valid_date):
    expected_output = "11.03.2024"  # Ожидаем, что дата будет в формате DD.MM.YYYY
    assert get_date(valid_date) == expected_output


def test_get_date_edge_case(edge_case_date):
    expected_output = "01.01.2024"  # Ожидаем, что дата будет в формате DD.MM.YYYY
    assert get_date(edge_case_date) == expected_output


# Параметризованные данные для тестов
@pytest.mark.parametrize("date_input, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Обычный случай
    ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Крайний случай
])
def test_get_date(date_input, expected_output):
    assert get_date(date_input) == expected_output
