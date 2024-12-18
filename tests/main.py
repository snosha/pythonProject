# гвызываем функцию
from src.widget import get_mask_account, get_mask_card_number

a = "Visa Platinum 7000792289606361"
b = "Счёт 73654108430135874305"
if __name__ == "__main__":
    print(get_mask_card_number(f"{a}"))
    print(get_mask_account(f"{b}"))
