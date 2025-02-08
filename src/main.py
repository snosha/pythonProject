import csv
import json
from typing import Dict, List

import pandas as pd

from filter_re import filter_operations_by_description

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}
VALID_SORT_ORDERS = {"по возрастанию": True, "по убыванию": False}


def load_transactions_from_json(filepath: str) -> List[Dict]:
    """
    Загружает транзакции из JSON файла.

    Аргументы:
        filepath (str): Путь к JSON файлу с транзакциями.

    Возвращает:
        List[Dict]: Список транзакций в формате словаря.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def load_transactions_from_csv(filepath: str) -> List[Dict]:
    """
    Загружает транзакции из CSV файла.

    Аргументы:
        filepath (str): Путь к CSV файлу с транзакциями.

    Возвращает:
        List[Dict]: Список транзакций в формате словаря.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_transactions_from_xlsx(filepath: str) -> List[Dict]:
    """
    Загружает транзакции из XLSX файла.

    Аргументы:
        filepath (str): Путь к XLSX файлу с транзакциями.

    Возвращает:
        List[Dict]: Список транзакций в формате словаря.
    """
    df = pd.read_excel(filepath)
    return df.to_dict(orient="records")


def get_valid_status() -> str:
    """
    Запрашивает у пользователя ввод статуса для фильтрации транзакций.

    Возвращает:
        str: Статус, введенный пользователем. Должен быть одним из допустимых значений:
             "EXECUTED", "CANCELED" или "PENDING".
    """
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию: ").strip().upper()
        if status in VALID_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status

        print(f'Статус операции "{status}" недоступен.')


def ask_yes_no(question: str) -> bool:
    """
    Запрашивает у пользователя ответ на вопрос "Да/Нет".

    Аргументы:
        question (str): Вопрос, на который нужно ответить.

    Возвращает:
        bool: True, если ответ "Да", иначе False.
    """
    return input(question + " (Да/Нет): ").strip().lower() == "да"


def main():
    """
    Основная функция программы, реализующая логику работы с транзакциями.

    Запрашивает у пользователя источник данных (JSON, CSV или XLSX), выполняет фильтрацию
    и сортировку транзакций по заданным критериям, затем выводит итоговый список транзакций.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = load_transactions_from_json("C:/Users/Антон/PycharmProjects/pythonProject/data/operations.json")
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = load_transactions_from_csv("C:/Users/Антон/PycharmProjects/pythonProject/data/transactions.csv")
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = load_transactions_from_xlsx("C:/Users/Антон/PycharmProjects/pythonProject/data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

    status = get_valid_status()
    # Изменена строка фильтрации с "status" на "state"
    transactions = [t for t in transactions if t.get("state", "").upper() == status]

    if ask_yes_no("Отсортировать операции по дате?"):
        while True:
            order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            if order in VALID_SORT_ORDERS:
                try:
                    transactions.sort(key=lambda x: x.get("date", ""), reverse=not VALID_SORT_ORDERS[order])
                    break
                except Exception as e:
                    print(f"Ошибка при сортировке: {e}. Попробуйте снова.")
            else:
                print("Некорректный выбор. Попробуйте снова.")

    if ask_yes_no("Выводить только рублевые транзакции?"):
        transactions = [t for t in transactions if t.get("currency", "").upper() == "RUB"]

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании?"):
        search_term = input("Введите слово для фильтрации по описанию: ").strip()
        transactions = filter_operations_by_description(transactions, search_term)

    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for t in transactions:
            print(f"{t.get('date', 'Нет даты')} {t.get('description', 'Нет описания')}")
            print(f"{t.get('account_from', 'Не указан источник')} -> {t.get('account_to', 'Не указан получатель')}")
            print(f"Сумма: {t.get('amount', 'Не указана')} {t.get('currency', 'Не указана')}\n")


if __name__ == "__main__":
    main()
