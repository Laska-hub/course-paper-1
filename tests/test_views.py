# tests/test_views.py
from datetime import datetime
from typing import Dict, List

import pytest

from src.views import events_page, greeting_by_time, main_page


@pytest.fixture
def sample_transactions() -> List[Dict]:
    return [
        {
            "amount": -100.0,
            "card_last_digits": "1234",
            "category": "Супермаркеты",
            "date": "2021-09-01",
            "description": "Магнит",
        },
        {
            "amount": 500.0,
            "card_last_digits": "1234",
            "category": "Зарплата",
            "date": "2021-09-01",
            "description": "Компания",
        },
    ]


def test_greeting_by_time() -> None:
    assert greeting_by_time(datetime(2021, 1, 1, 6)) == "Доброе утро"
    assert greeting_by_time(datetime(2021, 1, 1, 13)) == "Добрый день"
    assert greeting_by_time(datetime(2021, 1, 1, 19)) == "Добрый вечер"
    assert greeting_by_time(datetime(2021, 1, 1, 2)) == "Доброй ночи"


def test_main_page_structure(sample_transactions: List[Dict]) -> None:
    result = main_page(sample_transactions, "2021-09-01")
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert isinstance(result["cards"], list)
    assert isinstance(result["top_transactions"], list)


def test_events_page_structure(sample_transactions: List[Dict]) -> None:
    result = events_page(sample_transactions, "2021-09-01", period="M")
    assert "expenses" in result
    assert "income" in result
    assert "currency_rates" in result
    assert "stock_prices" in result
