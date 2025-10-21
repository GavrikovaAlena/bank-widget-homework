from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер карты в формате "XXXX XX** **** XXXX".
    Принимает номер карты как строку или число.
    Если длина != 16, выбрасывает ValueError.
    """
    card_str = str(card_number).replace(" ", "")
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен быть 16-цифровым")

    part1 = card_str[:4]
    part2 = card_str[4:6] + "**"
    part3 = "****"
    part4 = card_str[-4:]

    masked = f"{part1} {part2} {part3} {part4}"
    return masked


def get_mask_account(account: Union[str, int]) -> str:
    """
    Маскирует номер счёта в формате "**XXXX".
    Принимает номер счёта как строку или число.
    Если длина < 4, выбрасывает ValueError.
    """
    account_str = str(account).replace(" ", "")  # Очистка
    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    if len(account_str) > 20:
        raise ValueError("Слишком длинный номер счета")

    masked = "**" + account_str[-4:]
    return masked
