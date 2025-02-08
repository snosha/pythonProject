import json
import unittest
from datetime import datetime
from unittest.mock import patch

# Предположим, что весь код в главном файле был импортирован как mymodule
from main import filter_operations_by_description, get_valid_status, load_transactions_from_json


class TestBankingTransactions(unittest.TestCase):

    # Тест для загрузки данных из JSON
    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data=json.dumps([
        {"id": 1, "state": "EXECUTED", "date": "2021-08-10", "amount": "100.00", "currency": "USD", "description": "Payment"},
        {"id": 2, "state": "PENDING", "date": "2021-08-11", "amount": "200.00", "currency": "RUB", "description": "Transfer"}
    ]))
    def test_load_transactions_from_json(self, mock_file):
        transactions = load_transactions_from_json("test.json")
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["state"], "EXECUTED")
        self.assertEqual(transactions[1]["state"], "PENDING")
        mock_file.assert_called_once_with("test.json", "r", encoding="utf-8")

    # Тест для проверки правильности статуса
    @patch("builtins.input", side_effect=["executed"])
    def test_get_valid_status(self, mock_input):
        status = get_valid_status()
        self.assertEqual(status, "EXECUTED")

    # Тест для фильтрации транзакций по статусу
    def test_filter_transactions_by_status(self):
        transactions = [
            {"id": 1, "state": "EXECUTED", "date": "2021-08-10", "amount": "100.00", "currency": "USD", "description": "Payment"},
            {"id": 2, "state": "PENDING", "date": "2021-08-11", "amount": "200.00", "currency": "RUB", "description": "Transfer"}
        ]
        status = "EXECUTED"
        filtered = [t for t in transactions if t.get("state", "").upper() == status]
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["state"], "EXECUTED")

    # Тест для сортировки транзакций по дате
    def test_sort_transactions_by_date(self):
        transactions = [
            {"id": 1, "state": "EXECUTED", "date": "2021-08-10", "amount": "100.00", "currency": "USD", "description": "Payment"},
            {"id": 2, "state": "PENDING", "date": "2021-08-11", "amount": "200.00", "currency": "RUB", "description": "Transfer"}
        ]
        transactions.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
        self.assertEqual(transactions[0]["id"], 1)  # Первый элемент должен быть с более ранней датой

    # Тест для фильтрации транзакций по валюте
    def test_filter_transactions_by_currency(self):
        transactions = [
            {"id": 1, "state": "EXECUTED", "date": "2021-08-10", "amount": "100.00", "currency": "USD", "description": "Payment"},
            {"id": 2, "state": "PENDING", "date": "2021-08-11", "amount": "200.00", "currency": "RUB", "description": "Transfer"}
        ]
        filtered = [t for t in transactions if t.get("currency", "").upper() == "RUB"]
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["currency"], "RUB")

    # Тест для фильтрации транзакций по описанию
    def test_filter_transactions_by_description(self):
        transactions = [
            {"id": 1, "state": "EXECUTED", "date": "2021-08-10", "amount": "100.00", "currency": "USD", "description": "Payment"},
            {"id": 2, "state": "PENDING", "date": "2021-08-11", "amount": "200.00", "currency": "RUB", "description": "Transfer"}
        ]
        search_term = "Payment"
        filtered = filter_operations_by_description(transactions, search_term)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["description"], "Payment")


if __name__ == "__main__":
    unittest.main()
