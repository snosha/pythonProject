import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызовов функции и их результатов.

    Этот декоратор записывает информацию о вызове функции, её аргументах и
    результатах в файл или выводит её в консоль. Если происходит ошибка во время выполнения функции,
    информация о ней также будет записана в лог.

    Параметры:
    - filename: путь к файлу для записи лога (по умолчанию логируется в консоль).

    Возвращает:
    - Функцию-декоратор для логирования.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Декоратор для конкретной функции, который логирует её вызов и результат.

        Параметры:
        - func: функция, которую нужно задекорировать.

        Возвращает:
        - Задекорированную функцию с логированием.
        """
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка для функции, которая логирует её вызов, выполнение и результат.

            Параметры:
            - *args: позиционные аргументы, переданные в функцию.
            - **kwargs: именованные аргументы, переданные в функцию.

            Возвращает:
            - Результат выполнения функции.
            """
            log_output = f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}"

            # Логирую в файл или консоль
            if filename:
                with open(filename, 'a') as log_file:
                    log_file.write(log_output + '\n')
            else:
                print(log_output)

            try:
                # Выполнение функции и логирование результата
                result = func(*args, **kwargs)
                log_output = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(log_output + '\n')
                else:
                    print(log_output)
                return result

            except Exception as e:
                # Логирование ошибки
                log_output = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(log_output + '\n')
                else:
                    print(log_output)  # Вывод ошибки в стандартный вывод

        return wrapper

    return decorator
