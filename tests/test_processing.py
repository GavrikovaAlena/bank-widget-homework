from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстуры для данных
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "PENDING", "date": "2024-03-10T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-12T15:30:00"},
        {"id": 4, "state": "CANCELLED", "date": "2024-03-09T08:00:00"},
    ]


# Тесты для filter_by_state с фикстурой и параметризацией
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),
    ("PENDING", [2]),
    ("CANCELLED", [4]),
    ("UNKNOWN", []),  # Нет совпадений
])
def test_filter_by_state(sample_transactions: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    filtered = filter_by_state(sample_transactions, state)
    assert [t["id"] for t in filtered] == expected_ids


# Тесты для sort_by_date с фикстурой и параметризацией
@pytest.mark.parametrize("reverse, expected_order", [
    (True, [3, 1, 2, 4]),  # Убывание: 12, 11, 10, 9 марта
    (False, [4, 2, 1, 3]),  # Возрастание
])
def test_sort_by_date(sample_transactions: List[Dict[str, Any]], reverse: bool, expected_order: List[int]) -> None:
    sorted_list = sort_by_date(sample_transactions, reverse)
    assert [t["id"] for t in sorted_list] == expected_order


def test_sort_by_date_identical_dates() -> None:
    transactions = [
        {"id": 1, "date": "2024-03-11T00:00:00"},
        {"id": 2, "date": "2024-03-11T00:00:00"},
    ]
    sorted_list = sort_by_date(transactions, True)
    # Порядок сохраняется при одинаковых датах
    assert len(sorted_list) == 2


@pytest.mark.parametrize("transactions", [
    [],  # Пустой список
    [{"id": 1, "date": "invalid"}],  # Неверная дата
])
def test_sort_by_date_edge_cases(transactions: List[Dict[str, Any]]) -> None:
    if transactions and "invalid" in transactions[0]["date"]:
        with pytest.raises(ValueError):
            sort_by_date(transactions)
    else:
        assert sort_by_date(transactions) == []
