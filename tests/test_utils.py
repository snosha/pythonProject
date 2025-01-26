import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100.0}]')
    def test_load_transactions_valid_file(self, mock_file):
        """
        Проверяет загрузку корректного файла с данными.
        """
        result = load_transactions()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["amount"], 100.0)

    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_load_transactions_invalid_format(self, mock_file):
        """
        Проверяет обработку файла с некорректным форматом (не список).
        """
        result = load_transactions()
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='invalid json')
    def test_load_transactions_invalid_json(self, mock_file):
        """
        Проверяет обработку некорректного JSON-файла.
        """
        result = load_transactions()
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_transactions_file_not_found(self, mock_file):
        """
        Проверяет поведение при отсутствии файла.
        """
        result = load_transactions()
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_transactions_empty_file(self, mock_file):
        """
        Проверяет обработку пустого файла.
        """
        result = load_transactions()
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
