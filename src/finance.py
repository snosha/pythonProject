import csv
from pathlib import Path

import pandas as pd


def read_transactions_from_csv(csv_file_name):
    """
    Считывает финансовые операции из CSV-файла, находящегося в папке `data`.
    """
    try:
        # Поднимаемся на уровень выше (в папку project) и ищем папку data
        base_dir = Path(__file__).parent.parent  # Переход в корневую папку проекта
        file_path = base_dir / 'data' / csv_file_name
        print(f"Ищем файл по пути: {file_path}")
        transactions = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден. Убедитесь, что папка 'data' и файл существуют.")
        return []


def read_transactions_from_excel(excel_file_name):
    """
    Считывает финансовые операции из Excel-файла, находящегося в папке `data`.
    """
    try:
        # Поднимаемся на уровень выше (в папку project) и ищем папку data
        base_dir = Path(__file__).parent.parent  # Переход в корневую папку проекта
        file_path = base_dir / 'data' / excel_file_name
        print(f"Ищем файл по пути: {file_path}")
        df = pd.read_excel(file_path)
        transactions = df.to_dict('records')
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден. Убедитесь, что папка 'data' и файл существуют.")

    return []
