def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, скрывая часть символов.

    Аргументы:
        card_number (str): Полный номер карты в виде строки.

    Возвращает:
        str: Маскированный номер карты, где только первые 6 и последние 4 цифры видны,
             а остальные заменены символами "*".
    """
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского аккаунта, скрывая часть символов.

    Аргументы:
        account_number (str): Полный номер аккаунта в виде строки.

    Возвращает:
        str: Маскированный номер аккаунта, где только последние 4 цифры видны,
             а остальные заменены символами "*".
    """
    return "**" + account_number[-4:]
