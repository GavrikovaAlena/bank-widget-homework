import pytest
from typing import List, Dict, Any

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Фикстура для тестовых транзакций
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


# Тесты для filter_by_currency
@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),
    ("RUB", [873106923, 594226727]),
    ("EUR", []),  # Нет совпадений
])
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency: str, expected_ids: List[int]) -> None:
    filtered = list(filter_by_currency(sample_transactions, currency))
    assert [t["id"] for t in filtered] == expected_ids


def test_filter_by_currency_empty_list() -> None:
    assert list(filter_by_currency([], "USD")) == []


# Тесты для transaction_descriptions
@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([{"description": "Test1"}, {"description": "Test2"}], ["Test1", "Test2"]),
    ([], []),  # Пустой список
    ([{"description": ""}], [""]),  # Пустое описание
])
def test_transaction_descriptions(transactions: List[Dict[str, Any]], expected_descriptions: List[str]) -> None:
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


# Тесты для card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999999999999996, 9999999999999999, ["9999 9999 9999 9996", "9999 9999 9999 9997", "9999 9999 9999 9998"]),
])
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    generated = list(card_number_generator(start, stop))
    assert generated == expected


@pytest.mark.parametrize("start, stop", [
    (0, 5),  # start < 1
    (1, 10000000000000000),  # stop > max
    (5, 5),  # start >= stop
])
def test_card_number_generator_invalid(start: int, stop: int) -> None:
    with pytest.raises(ValueError):
        list(card_number_generator(start, stop))
