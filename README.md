# Bank Operations Widget

## Цель проекта
Это виджет для обработки банковских операций:
маскировка номеров карт/счетов, форматирование дат,
фильтрация и сортировка транзакций.
Разработан на Python с использованием Poetry, следует PEP8 и GitFlow.




## Установка
1. Клонируй репозиторий:
https://github.com/GavrikovaAlena/bank-widget-homework.git

2. Установи зависимости:
poetry install



## Использование
Импортируй модули из `src/`.

### Маскировка (masks.py и widget.py)
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))  # "Visa Platinum 7000 79** **** 6361"
print(get_date("2024-03-11T02:26:18.671407"))              # "11.03.2024"


### Обработка транзакций (processing.py)
from src.processing import filter_by_state, sort_by_date

transactions = [...]  # Пример из задания

"#"Фильтрация по 'EXECUTED' (не забудь убрать кавычки вокруг хэштэга)
filtered = filter_by_state(transactions)
print(filtered)  # [{'id': 41428829, ...}, {'id': 939719570, ...}]

"#"Сортировка по дате (убывание)(не забудь убрать кавычки вокруг хэштэга)
sorted_trans = sort_by_date(transactions)
print(sorted_trans)  # [{'id': 41428829, ...}, {'id': 615064591, ...}, ...]


## Структура проекта
src/: Основной код (masks.py, widget.py, processing.py).

tests/: Тесты (пока пусто).

main.py: Пример запуска (пока пусто).
