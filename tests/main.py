#вызываем функцию
from src.masks import get_mask_card_number, get_mask_account

a = "7000792289606361"
b = "73654108430135874305"
if __name__ == "__main__":
    print(get_mask_card_number(f"{a}"))
    print(get_mask_account(f"{b}"))

