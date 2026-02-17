from datetime import datetime
from typing import Dict, List

import pandas as pd

from src.reports import (
    spending_by_category,
    spending_by_weekday,
    spending_by_workday,
)

transactions_list: List[Dict] = [
    {
        "amount": -100.0,
        "card_last_digits": "7197",
        "category": "Супермаркеты",
        "date": datetime(2021, 12, 31, 16, 44),
    },
    {
        "amount": -50.0,
        "card_last_digits": "7197",
        "category": "Фастфуд",
        "date": datetime(2021, 12, 30, 12, 0),
    },
    {
        "amount": 200.0,
        "card_last_digits": "nan",
        "category": "Пополнения",
        "date": datetime(2021, 12, 29, 14, 0),
    },
]


def test_spending_by_category() -> None:
    df = pd.DataFrame(transactions_list)
    report = spending_by_category(df, "Супермаркеты")
    assert isinstance(report, list)
    assert report[0]["amount"] == -100.0


def test_spending_by_weekday() -> None:
    df = pd.DataFrame(transactions_list)
    report = spending_by_weekday(df)
    assert "Friday" in report or "Пятница" in report  # в зависимости от локали
    assert report["Friday"] == -100.0 or report["Пятница"] == -100.0


def test_spending_by_workday() -> None:
    df = pd.DataFrame(transactions_list)
    report = spending_by_workday(df)
    assert isinstance(report, dict)
    # Проверяем, что сумма расходов по рабочим дням корректно суммирована
    total = sum(report.values())
    expected = sum(
        tx["amount"] for tx in transactions_list if tx["date"].weekday() < 5
    )
    assert total == expected
