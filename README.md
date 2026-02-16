# Course Paper 1 – Financial Analysis Project

## 📌 Описание проекта

Проект реализует инструменты для анализа финансовых данных и генерации отчетов:  

- Загрузка и обработка транзакций из Excel (`data/operations.xlsx`)  
- Анализ расходов по категориям и дням недели  
- Подсчет cashback по категориям  
- Расчет инвестиций (округления на инвесткопилку)  
- Генерация аналитических отчетов с помощью `pandas`  
- Формирование JSON-ответов для веб-интерфейса  
- Покрытие кода тестами (`pytest`) и статическая типизация (`mypy`)  

Проект выполнен в рамках курсовой работы по Python.

---

## 🗂 Структура проекта

course_paper_1/
│
├── src/
│ ├── utils.py # Вспомогательные функции (загрузка данных, фильтры)
│ ├── services.py # Бизнес-логика (cashback, инвестиции)
│ ├── reports.py # Аналитические отчеты (расходы по категориям/дням недели)
│ ├── views.py # JSON-ответы для интерфейса
│ 
│
├── data/
│ └── operations.xlsx # Исходные финансовые данные
│
├── tests/
│ ├── test_services.py
│ ├── test_reports.py
│ └── test_views.py
│
├── user_settings.json # Настройки пользователя (путь для отчетов, тема, язык и др.)
├── pyproject.toml, poetry lock # Конфигурация Poetry
├── README.md
└── .venv/ # Виртуальное окружение
 ---.gitinore
 --- check_code.py


## ⚙️ Используемые технологии

- Python 3.13  
- Poetry (управление зависимостями)  
- pandas (анализ данных)  
- pytest (тестирование)  
- mypy (статическая типизация)  
- FastAPI (формирование JSON-ответов, веб-интерфейс)  

## 📊 Примеры функционала

### Анализ расходов по категории

```python
from src.reports import spending_by_category
from src.utils import load_operations

df = load_operations()
result = spending_by_category(df, "Супермаркеты")
print(result)

 -- Средние траты по дням недели
from src.reports import spending_by_weekday

result = spending_by_weekday(df)
print(result)

 -- Анализ cashback
from src.services import cashback_analysis

cashback = cashback_analysis("2021-10-01", "2021-12-31")
print(cashback)

 --  Инвестиционный банк
from src.services import investment_analysis

invested = investment_analysis("2021-10-01", "2021-12-31")
print(invested)

 -- JSON-ответ для веб-интерфейса
from src.views import main_page, events_page, weekday_page

print(main_page())
print(events_page())
print(weekday_page())

** функции events_page и weekday_page используют фильтр за последние 3 месяца от переданной даты. 
Если данных за этот период нет, результат будет пустым.

 -- Проверка работы и тесты

Запуск тестов:

poetry run pytest -v tests/

Пример успешного вывода: 7 passed, 0 failed, 4 warnings in 1.49s

Проверка кода и работы функций: poetry run python check_code.py