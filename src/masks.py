from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Возвращает замаскированый номер карты в формате: XXXX XX** **** XXXX"""

    card_str = str(card_number)

    if len(card_str) < 16:
        raise ValueError("Номер карты должен содержать не менее 16 цифр")

    part1 = card_str[:4]
    part2 = card_str[4:6]
    part3 = ""
    part4 = "****"
    part5 = card_str[-4:]

    masked = f"{part1} {part2}{part3} {part4} {part5}"
    return masked


def get_mask_account(account_number: Union[int, str]) -> str:
    """Возвращает замаскированный номер банковского счета в формате: **XXXX"""
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    masked = f"{account_str[-4:]}"
    return masked
