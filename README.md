# Bank Operations Widget

Этот проект представляет собой набор модулей для обработки банковских транзакций,
маскирования данных и генерации различных элементов. 

Он написан на Python и использует современные практики разработки 
(тесты с pytest, линтеры, типизация).


## Описание

Проект включает модули для:

- Маскирования номеров карт и счетов (masks).

- Форматирования виджетов для отображения транзакций (widget).

- Обработки и фильтрации транзакций (processing).

- Генерации данных и итераторов для транзакций (generators).

- Декорирование функций для логирования (decorators).

Все модули поддерживают типизацию (mypy) и покрыты тестами с использованием pytest.


## Установка

1. Клонируй репозиторий:
https://github.com/GavrikovaAlena/bank-widget-homework.git

2. Установи зависимости:
```
poetry install
```

## Использование

Импортируй модули из `src/`.

### Модуль masks
#### Модуль для маскирования номеров карт и счетов.
```
from src.masks import get_mask_card_number, get_mask_account

#Маскировка номера карты
masked_card = get_mask_card_number("7000792289606361")  # Вывод: 7000 79** **** 6361

#Маскировка номера счета
masked_account = get_mask_account("73654108430135874305")  # Вывод: **4305
```

### Модуль widget
#### Модуль для форматирования виджетов транзакций.
```
from src.widget import get_date, mask_account_card

#Форматирование даты
formatted_date = get_date("2024-03-11T02:26:18.671407")  # Вывод: 11.03.2024

#Маскировка счета или карты в виджете
masked = mask_account_card("Maestro 1596837868705199")  # Вывод: Maestro 1596 83** **** 5199
masked_account = mask_account_card("Счет 64686473678894779589")  # Вывод: Счет **9589
```

### Модуль processing
#### Модуль для обработки списка транзакций (фильтрация по дате, статусу и т.д.).
```
from src.processing import filter_by_state, sort_by_date

#Фильтрация по статусу
executed = filter_by_state(transactions, "EXECUTED")

#Сортировка по дате
sorted_transactions = sort_by_date(transactions, descending=True)
```

### Модуль generators
#### Модуль функуий-генераторов содержит функции-генераторы для эффективной обработки больших объемов данных транзакций
```
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

#Фильтрация по валюте
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))  # Первая транзакция в USD

#Генератор описаний
descriptions = transaction_descriptions(transactions)
print(next(descriptions))  # Описание первой транзакции

#Генератор номеров карт
for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 и т.д.
```

### Модуль decorators
#### Модуль для декорирования функций с логированием (успеха, ошибок и входных параметров в консоль или файл).
```
from src.decorators import log

# Пример использования декоратора для логирования в консоль
@log()
def add(x: int, y: int) -> int:
    return x + y

result = add(1, 2)  # Логирует: "add ok"
print(result)  # 3

# Пример с логированием в файл (при ошибке)
@log(filename="log.txt")
def divide(x: int, y: int) -> float:
    return x / y

try:
    divide(1, 0)  # Логирует в файл: "divide error: ZeroDivisionError. Inputs: (1, 0), {}"
except ZeroDivisionError:
    pass
```


## Структура проекта
```
project/
├── htmlcov/              # Отчет покрытия (добавляется для сдачи)
├── src/
│   ├── __init__.py
│   ├── masks.py            # Модуль маскирования
│   ├── widget.py           # Модуль виджетов
│   ├── processing.py       # Модуль обработки транзакций
│   ├── generators.py       # Модуль генераторов
│   └── decorators.py       # Модуль декорирования функций для логирования
├── tests/
│   ├── __init__.py
│   ├── test_masks.py       # Тесты для функций маскирования карт и счетов
│   ├── test_widget.py      # Тесты для функций форматирования и дат
│   ├── test_processing.py  # Тесты для фильтрации и сортировки транзакций
│   ├── test_generators.py  # Тесты для генераторов фильтрации по валюте, генерации описаний транзакций и номеров карт
│   └── test_decorators.py  # Тесты для декоратора логирования (фикстуры, параметризация, консоль/файл)
├── .flake8
├── .gitignore
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```


## Тестирование

Проект использует pytest для автоматизированного тестирования. 

Тесты покрывают все основные функции и обеспечивают покрытие кода более 80%.

Тесты используют фикстуры для генерации данных и параметризацию для проверки различных сценариев.


### Запуск тестов

- Установите зависимости: poetry install
- Запустите тесты: pytest
- С отчётом покрытия: pytest --cov=src --cov-report=html (отчёт в htmlcov/index.html)


### Линтеры и типизация
mypy: Проверка типов: mypy src/

flake8: Проверка стиля: flake8 src/ tests/ (не более 5 ошибок)

isort: Форматирование импортов: isort src/ tests/ (не более 1 изменения)

