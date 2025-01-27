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
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


# Логирование для модуля masks

logger_masks = setup_logger('masks')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, скрывая часть символов.
    """
    if not card_number:  # Проверка на пустую строку
        logger_masks.error("Номер карты не может быть пустой")  # Логирование ошибки
        raise ValueError("Номер карты не может быть пустой")

    masked_card = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger_masks.info(f"Маскировка номера карты: {masked_card}")  # Логирование успешной маскировки
    return masked_card


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского аккаунта, скрывая часть символов.
    """
    if not account_number:  # Проверка на пустую строку
        logger_masks.error("Номер аккаунта не должен быть пустой")  # Логирование ошибки
        raise ValueError("Номер аккаунта не должен быть пустой")

    masked_account = "**" + account_number[-4:]
    logger_masks.info(f"Маскировка номера аккаунта: {masked_account}")  # Логирование успешной маскировки
    return masked_account
