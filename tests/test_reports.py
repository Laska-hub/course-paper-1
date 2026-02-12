# tests/test_reports.py

from datetime import datetime

import pandas as pd

from src.reports import expenses_by_category, expenses_by_weekday


def test_expenses_by_category_structure() -> None:
    df = pd.DataFrame(
        {
            "Дата операции": ["2026-01-01", "2026-01-02"],
            "Сумма операции": [100, 200],
            "Категория": ["Food", "Food"],
        }
    )
    date = datetime.strptime("2026-01-03", "%Y-%m-%d")
    result = expenses_by_category(df, "Food", date)

    assert isinstance(result, dict)
    assert "total" in result


def test_expenses_by_weekday_structure() -> None:
    df = pd.DataFrame(
        {
            "Дата операции": ["2026-01-01", "2026-01-02"],
            "Сумма операции": [100, 200],
            "Категория": ["Food", "Food"],
        }
    )

    result = expenses_by_weekday(df)

    assert isinstance(result, dict)
    assert "Monday" in result
