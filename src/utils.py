import json
import os


def load_operations(path):
    """
    Загружает операции из JSON-файла.

    Args:
        path (str): Путь к файлу operations.json.

    Returns:
        list: Список словарей с операциями. Если ошибка — пустой список.
    """
    print(f"Текущая рабочая директория: {os.getcwd()}")
    print(f"Абсолютный путь к файлу: {os.path.abspath(path)}")

    if not os.path.exists(path):
        print(f"Ошибка: Файл {path} не найден.")
        return []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Предполагаем, что JSON — это массив операций
        operations = data if isinstance(data, list) else []
        print(f"Успешно загружено {len(operations)} операций из {path}.")
        return operations
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {path}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке {path}: {e}")
        return []
