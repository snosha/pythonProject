import json
import logging
from pathlib import Path

# Настройка логера
log_dir = 'logs'
if not Path(log_dir).exists():
    Path(log_dir).mkdir()

# Функция для настройки логера


def setup_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    log_file = Path(log_dir) / f'{module_name}.log'
    file_handler = logging.FileHandler(log_file, mode='w')  # Открываем файл в режиме перезаписи
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


# Создание логера для модуля

logger = setup_logger('utils')


def load_transactions(file_path='data/operations.json'):
    """
    Функция загружает данные о транзакциях из JSON-файла.

    Параметры:
    file_path (str): Путь к файлу с данными. По умолчанию 'data/operations.json'.

    Возвращает:
    list: Список транзакций из файла, если файл существует и содержит корректные данные.
          Пустой список в случае ошибки (например, если файл не существует или данные некорректны).
    """
    # Преобразуем относительный путь в абсолютный
    absolute_path = Path(file_path).resolve()

    # Проверка, существует ли файл
    if not absolute_path.is_file():
        logger.error(f"Файл не найден: {absolute_path}")  # Логирование ошибки
        return []  # Если файл не найден, возвращаем пустой список

    try:
        with open(absolute_path, 'r') as file:
            transactions = json.load(file)

        # Проверка, является ли содержимое файлом списка
        if not isinstance(transactions, list):
            logger.warning(f"Неверный формат данных в файле: {absolute_path}. Ожидался список.")  # Логирование предупреждения
            return []  # Если данные не список, возвращаем пустой список

        logger.info(f"Успешная загрузка транзакций из файла: {absolute_path}")  # Логирование успеха
        return transactions

    except json.JSONDecodeError:
        logger.error(f"Ошибка при декодировании JSON в файле: {absolute_path}")  # Логирование ошибки
        return []  # Если ошибка при чтении, возвращаем пустой список
    except Exception as e:  # Ловим все другие возможные ошибки
        logger.error(f"Неизвестная ошибка при загрузке данных из файла: {absolute_path}. Ошибка: {e}")  # Логирование ошибки
        return []  # Возвращаем пустой список при ошибках
