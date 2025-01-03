import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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
