from datetime import datetime
from typing import Any

def filter_by_state(transactions: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """
    Функция, которая фильтрует список транзакций по статусу (state).
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]



def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Функция, которая сортирует список транзакций по дате (date) в убывающем порядке по умолчанию.
    """
    def date_key(transaction: dict[str, Any]) -> datetime:
        return datetime.fromisoformat(transaction['date'])

    return sorted(transactions, key=date_key, reverse=reverse)
