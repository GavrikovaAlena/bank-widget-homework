from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета на основе типа.

    Args:
        info (str): строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        str: строка с замаскированным номером, например "Visa Platinum 7000 79** **** 6361"
    """
    parts = info.split(" ", 1)
    if len(parts) != 2:
        raise ValueError("Некорректный формат строки")
    card_type, number = parts[0], parts[1]

    if card_type.lower() == "счет" or card_type.lower() == " счет":
        masked_number = get_mask_account(number)
        return f"{card_type} {masked_number}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата ISO 8601 в формат "ДД.ММ.ГГГГ".

    Args:
        date_str (str): строка вида "2024-03-11T02:26:18.671407"

    Returns:
        str: дата в формате "11.03.2024"
    """
    dt = datetime.fromisoformat(date_str)
    return f"{dt.day:02d}.{dt.month:02d}.{dt.year}"