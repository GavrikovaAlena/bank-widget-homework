import os
import tempfile
import pytest
from typing import Any

from src.decorators import log


# Фикстура для успешной функции
@pytest.fixture
def success_func() -> Any:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    return add


# Фикстура для функции с ошибкой
@pytest.fixture
def error_func() -> Any:
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    return divide


# Тесты для логирования в консоль (успех)
def test_log_console_success(success_func: Any, capsys: pytest.CaptureFixture[str]) -> None:
    result = success_func(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out


# Тесты для логирования в консоль (ошибка)
def test_log_console_error(error_func: Any, capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(ZeroDivisionError):
        error_func(1, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


# Тесты для логирования в файл (успех)
def test_log_file_success(success_func: Any) -> None:
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_filename = temp_file.name

    # Переопределяем функцию с filename
    @log(filename=temp_filename)
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)
    assert result == 3

    with open(temp_filename, 'r') as f:
        content = f.read()
    assert "add ok" in content
    os.unlink(temp_filename)  # Удаляем временный файл


# Тесты для логирования в файл (ошибка)
def test_log_file_error(error_func: Any) -> None:
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_filename = temp_file.name

    # Переопределяем функцию с filename
    @log(filename=temp_filename)
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open(temp_filename, 'r') as f:
        content = f.read()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in content
    os.unlink(temp_filename)  # Удаляем временный файл


# Параметризация для различных сценариев
@pytest.mark.parametrize("args, kwargs, expected_message", [
    ((1, 2), {}, "add ok"),
    ((0, 0), {}, "add ok"),
])
def test_log_parametrized_success(args: tuple, kwargs: dict, expected_message: str,
                                  capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add(*args, **kwargs)
    captured = capsys.readouterr()
    assert expected_message in captured.out
