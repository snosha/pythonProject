import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_file_is_not_list(self, mock_file):
        """
        Тест, когда файл содержит не список (например, объект JSON).
        Ожидается, что функция вернет пустой список.
        """
        mock_file.return_value.read.return_value = '{"id": 1, "amount": 100}'  # Не список, а объект
        result = load_transactions('data/operations.json')
        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("builtins.open", new_callable=mock_open)
    def test_file_not_found(self, mock_file):
        """
        Тест, когда файл не найден.
        Ожидается, что функция вернет пустой список.
        """
        mock_file.side_effect = FileNotFoundError
        result = load_transactions('data/operations.json')
        self.assertEqual(result, [])  # Ожидаем пустой список

    @patch("builtins.open", new_callable=mock_open)
    def test_file_read_error(self, mock_file):
        """
        Тест, когда в файле некорректный JSON.
        Ожидается, что функция вернет пустой список.
        """
        mock_file.return_value.read.return_value = 'invalid json'
        result = load_transactions('data/operations.json')
        self.assertEqual(result, [])  # Ожидаем пустой список


if __name__ == "__main__":
    unittest.main()
