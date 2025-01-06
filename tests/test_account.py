import pytest

from src.masks import get_mask_account

# Фикстура для корректного номера счета


@pytest.fixture
def valid_account_number() -> str:
    return "12345678901234567890"

# Фикстура для номера счета меньшей длины


@pytest.fixture
def short_account_number() -> str:
    return "123"

# Фикстура для пустой строки


@pytest.fixture
def empty_account_number() -> str:
    return ""

# Фикстура для строки с пробелами


@pytest.fixture
def space_account_number() -> str:
    return " "

# Тестирование корректного номера счета


def test_get_mask_account_valid(valid_account_number: str) -> None:
    assert get_mask_account(valid_account_number) == "**7890"

# Тестирование номера счета меньшей длины


def test_get_mask_account_short(short_account_number: str) -> None:
    assert get_mask_account(short_account_number) == "**123"
    assert get_mask_account("1") == "**1"

# Тестирование пустой строки


def test_get_mask_account_empty(empty_account_number: str) -> None:
    with pytest.raises(ValueError):  # Ожидаем исключение ValueError
        get_mask_account(empty_account_number)

# Тестирование строки с пробелом


def test_get_mask_account_space(space_account_number: str) -> None:
    result = get_mask_account(space_account_number)
    assert result == "** "  # Проверяем, что пробел маскируется
