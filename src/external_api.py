import os
import requests

def convert_to_rub(operation):
    """
    Конвертирует сумму операции в RUB по курсу из API.

    Args:
        operation (dict): Словарь операции с полем 'operationAmount'.

    Returns:
        float: Сумма в RUB. Если валюта RUB или ошибка — исходная сумма.
    """
    try:
        amount = float(operation["operationAmount"]["amount"])
        currency = operation["operationAmount"]["currency"]["code"]
    except (KeyError, ValueError, TypeError) as e:
        raise ValueError(f"Неверный формат operationAmount в операции: {e}")

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        # Для неизвестных валют возвращаем исходную сумму
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в .env")

    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    params = {
        "base": currency,
        "symbols": "RUB"
    }
    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "rates" not in data or "RUB" not in data["rates"]:
            raise ValueError("Неверный ответ от API: нет курса RUB")
        rate = data["rates"]["RUB"]
        rub_amount = amount * rate
        return round(rub_amount, 2)
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        # Fallback: возвращаем исходную сумму при ошибке
        print(f"Ошибка конвертации для {currency}: {e}. Используем исходную сумму.")
        return amount
