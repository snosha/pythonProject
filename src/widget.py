# Функция маскировки номера карты
def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, показывая только первые 17 символов, две цифры после них, и последние 4 цифры.
    """
    return card_number[:17] + " " + card_number[17:19] + "** **** " + card_number[-4:]


# Функция маскировки номера аккаунта
def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта, добавляя перед ним слово 'Счёт'
    и показывая только последние 4 цифры.
    """
    return "Счёт " + "**" + account_number[-4:]


# Функция преобразования даты
def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата 2024-03-11T02:26:18.671407
    в формат ДД.ММ.ГГГГ (например, 11.03.2024).
    """
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


# Ввод даты
input_date = "2024-03-11T02:26:18.671407"

# Вызываем функцию и выводим результат
formatted_date = get_date(input_date)
print(formatted_date)
