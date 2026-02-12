# Course Paper 1 – Financial Analysis Project

## 📌 Описание проекта

Этот проект реализует набор инструментов для анализа финансовых данных:  
- получение валютных курсов и цен акций  
- анализ cashback по категориям  
- расчет инвестиционного банка  
- формирование аналитических отчетов с помощью pandas  
- генерация JSON-ответов (FastAPI)  
- покрытие кода тестами и статическая типизация  

Проект выполнен в рамках курсовой работы по Python.

---

## 🗂 Структура проекта

course_paper_1/
│
├── src/
│ ├── services.py # Бизнес-логика (курсы валют, акции, cashback, инвестиции)
│ ├── reports.py # Аналитические отчеты (pandas)
│ ├── views.py # JSON-ответы (FastAPI)
│ └── main.py # Точка входа (опционально)
│
├── tests/
│ ├── test_services.py
│ ├── test_reports.py
│ └── test_views.py
│
├── pyproject.toml # Poetry конфигурация
├── README.md
└── .venv/ # Виртуальное окружение


## ⚙️ Используемые технологии

- Python 3.13
- Poetry (управление зависимостями)
- pytest (тестирование)
- mypy (статическая типизация)
- pandas (анализ данных)
- FastAPI (JSON API)

## 📊 Пример функционала
Анализ cashback
cashback_analysis([100, 200, 300])

Инвестиционный банк
investment_bank([100, 200, 300])

Отчеты pandas

расходы по категориям
расходы по дням недели

🌐 FastAPI JSON Response
from src.views import generate_json_response
generate_json_response({"test": 123})

📌 Результаты тестирования

Все тесты успешно пройдены:

7 passed in 0.48s
