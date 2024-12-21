def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, скрывая часть символов.
    """
    if not card_number:  # Проверка на пустую строку
        raise ValueError("Номер карты не может быть пустой")
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского аккаунта, скрывая часть символов.
    """
    if not account_number:  # Проверка на пустую строку
        raise ValueError("Номер аккаунта не должен быть пустой")
    return "**" + account_number[-4:]
