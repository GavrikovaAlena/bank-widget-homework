from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризация для карт
@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    ("7000792289606361", "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
])
def test_get_mask_card_number_valid(card_number: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [
    "123",  # Слишком короткий
    "123456789012345678",  # Слишком длинный
    "abcd123456789012",  # Не цифры
    ])
def test_get_mask_card_number_invalid(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


# Параметризация для счетов
@pytest.mark.parametrize("account, expected", [
    (7365410843013587, "**3587"),
    ("7365410843013587", "**3587"),
    (1234567890, "**7890"),
])
def test_get_mask_account_valid(account: Union[int, str], expected: str) -> None:
    assert get_mask_account(account) == expected


@pytest.mark.parametrize("account", [
    "123",  # <4 цифр
    "",  # Пустой
    "abcd",  # Не цифры
    "1" * 21,  # >20 цифр
])
def test_get_mask_account_invalid(account: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account)
