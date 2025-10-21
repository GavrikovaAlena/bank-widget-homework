import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функции.

    Логирует имя функции и результат ("ok" при успехе) или ошибку и входные параметры при исключении.
    Если filename задан, логи записываются в файл; если нет - в консоль.

    Args:
        filename: Имя файла для логирования (опционально).

    Returns:
        Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None  # добавила для избежания ошибки, если возникнет исключение
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + '\n')
                else:
                    print(message)
                raise  # перебрасываем исключение

            # Логируем успешный вызов
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(message + '\n')
            else:
                print(message)

            return result

        return wrapper

    return decorator
