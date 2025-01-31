from finance import read_transactions_from_csv, read_transactions_from_excel

# Пример использования функции для CSV
csv_transactions = read_transactions_from_csv('transactions.csv')
print("Транзакции из CSV:")
for transaction in csv_transactions:
    print(transaction)

# Пример использования функции для Excel
excel_transactions = read_transactions_from_excel('transactions_excel.xlsx')
print("\nТранзакции из Excel:")
for transaction in excel_transactions:

    print(transaction)
