import pytest

from src.widget import get_date, mask_account_card


# Параметризация для mask_account_card
@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 7365410843013587", "Счет **3587"),
    ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
])
def test_mask_account_card_valid(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "Visa",  # Нет номера
    "Счет",  # Нет номера
    "Invalid 123",  # Короткий номер
])
def test_mask_account_card_invalid(input_str: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(input_str)


# Параметризация для get_date
@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11", "11.03.2024"),
    ("2023-01-01T00:00:00", "01.01.2023"),
])
def test_get_date_valid(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


@pytest.mark.parametrize("date_str", [
    "invalid",  # Не дата
    "2024-13-01",  # Неверный месяц
])
def test_get_date_invalid(date_str: str) -> None:
    with pytest.raises(ValueError):
        get_date(date_str)
