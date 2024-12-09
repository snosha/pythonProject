# функция маскировки номера карты
def get_mask_card_number(card_number) -> str:

    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


# функция маскировки номера аккаунта
def get_mask_account(account_number: str) -> str:

    return "**" + account_number[-4:]
