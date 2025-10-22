from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_to_rub


@pytest.mark.parametrize("currency, amount, expected_rate, expected", [
    ("RUB", "100", None, 100.0),
    ("USD", "100", 90.0, 9000.0),  # Пример курса
    ("EUR", "100", 100.0, 10000.0),
])
def test_convert_to_rub(currency, amount, expected_rate, expected):
    transaction = {"operationAmount": {"amount": amount, "currency": {"code": currency}}}
    if currency != "RUB":
        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"RUB": expected_rate}}
        with patch("requests.get", return_value=mock_response), \
             patch("os.getenv", return_value="fake_key"):
            assert convert_to_rub(transaction) == expected
    else:
        assert convert_to_rub(transaction) == expected


def test_convert_to_rub_no_api_key():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    with patch("os.getenv", return_value=None):
        with pytest.raises(ValueError):
            convert_to_rub(transaction)


def test_convert_to_rub_unknown_currency():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "BTC"}}}
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
