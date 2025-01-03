from decorators.decorators import log
import pytest
import os


# Тестирую логирование при успешном выполнении функции
def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    @log()
    def sample_function(a: int, b: int) -> int:
        return a + b

    sample_function(1, 2)

    captured = capsys.readouterr()

    # Проверяю, что в консоль был выведен правильный лог
    assert "Вызов функции sample_function с аргументами (1, 2) и {}" in captured.out
    assert "sample_function ok" in captured.out


# Тестирую логирование в файл при успешном выполнении функции
def test_log_to_file(tmp_path: pytest.TempPathFactory) -> None:
    log_file = os.path.join(str(tmp_path), "test_log.txt")  # Используем os.path.join для корректного создания пути

    @log(filename=log_file)
    def sample_function(a: int, b: int) -> int:
        return a + b

    sample_function(1, 2)

    # Проверяю, что в файл был записан правильный лог
    with open(log_file, "r") as file:
        log_contents = file.read()

    assert "Вызов функции sample_function с аргументами (1, 2) и {}" in log_contents
    assert "sample_function ok" in log_contents


# Тестирую логирование ошибок в консоль
def test_log_with_error_in_console(capsys: pytest.CaptureFixture) -> None:
    @log()
    def sample_function(a: int, b: int) -> float:
        return a / b  # Деление на ноль вызовет ошибку

    try:
        sample_function(1, 0)
    except ZeroDivisionError:
        pass  # Ожидаю, что ошибка будет выброшена

    captured = capsys.readouterr()

    # Проверяю, что ошибка была корректно выведена в консоль
    assert "sample_function error: division by zero. Inputs: (1, 0), {}" in captured.out


# Тестирую логирование ошибок в файл
def test_log_with_error_in_file(tmp_path: pytest.TempPathFactory) -> None:
    log_file = os.path.join(str(tmp_path), "test_log.txt")  # Используем os.path.join для корректного создания пути

    @log(filename=log_file)
    def sample_function(a: int, b: int) -> float:
        return a / b  # Деление на ноль вызовет ошибку

    try:
        sample_function(1, 0)
    except ZeroDivisionError:
        pass  # Ожидаю, что ошибка будет выброшена

    # Проверяю, что ошибка записана в лог-файл
    with open(log_file, "r") as file:
        log_contents = file.read()

    assert "sample_function error: division by zero. Inputs: (1, 0), {}" in log_contents
