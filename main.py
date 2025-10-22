import os
from dotenv import load_dotenv
from src.utils import load_operations
from src.external_api import convert_to_rub

# Загружаем переменные из .env (ключ API)
load_dotenv()

def main():
    # Путь к файлу (абсолютный, относительно main.py)
    path = os.path.join(os.path.dirname(__file__), "data", "operations.json")

    # Загружаем операции через utils
    operations = load_operations(path)
    if not operations:
        print("Ошибка: Не удалось загрузить операции из файла.")
        return

    print(f"Загружено {len(operations)} операций.")

    # Для каждой операции конвертируем сумму в RUB
    for op in operations:
        try:
            # Получаем описание для вывода
            description = op.get("description", "Без описания")
            original_amount = op["operationAmount"]["amount"]
            original_currency = op["operationAmount"]["currency"]["code"]

            # Конвертируем через external_api
            rub_amount = convert_to_rub(op)

            print(f"Операция: {description}")
            print(f"  Исходная сумма: {original_amount} {original_currency}")
            print(f"  Сумма в RUB: {rub_amount:.2f} RUB")
            print("-" * 40)
        except Exception as e:
            print(f"Ошибка при обработке операции {op.get('id', 'неизвестный')}: {e}")
            print("-" * 40)

if __name__ == "__main__":
    main()
