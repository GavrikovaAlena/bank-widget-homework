from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Принимает строку типа "Visa Platinum 7000792289606361"
    или "Счет 7365410843013587"
    и возвращает замаскированную строку.
    """
    parts = card_or_account.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат строки")

    number = parts[-1]
    if "счет" in card_or_account.lower():
        return " ".join(parts[:-1]) + " " + get_mask_account(number)
    else:
        return " ".join(parts[:-1]) + " " + get_mask_card_number(number)


def get_date(date_str: str) -> str:
    """
    Принимает строку даты в ISO-формате
    (например, "2024-03-11T02:26:18.671407")
    и возвращает в формате "ДД.ММ.ГГГГ".
    """
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d.%m.%Y")
