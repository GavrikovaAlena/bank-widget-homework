import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_valid():
    data = [{"id": 1}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        assert load_operations("dummy.json") == data


def test_load_operations_empty():
    with patch("builtins.open", mock_open(read_data="")):
        assert load_operations("dummy.json") == []


def test_load_operations_not_list():
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        assert load_operations("dummy.json") == []


def test_load_operations_file_not_found():
    assert load_operations("nonexistent.json") == []


def test_load_operations_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")):
        assert load_operations("dummy.json") == []
