from __future__ import annotations

from datetime import datetime

import pandas as pd
import pytest

from src.reports import (
    spending_by_category,
    spending_by_weekday,
    spending_by_workday,
)


@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "amount": -100.0,
                "category": "Супермаркеты",
                "date": datetime(2021, 9, 1),
            },
            {
                "amount": -50.0,
                "category": "Супермаркеты",
                "date": datetime(2021, 9, 2),
            },
            {
                "amount": 500.0,
                "category": "Зарплата",
                "date": datetime(2021, 9, 3),
            },
        ]
    )


def test_spending_by_category(sample_df: pd.DataFrame) -> None:
    result = spending_by_category(sample_df, "Супермаркеты")

    assert isinstance(result, list)
    assert all("amount" in r and "cashback" in r for r in result)
    assert result[0]["cashback"] == 1.0  # 1% от -100


def test_spending_by_weekday(sample_df: pd.DataFrame) -> None:
    result = spending_by_weekday(sample_df)

    assert isinstance(result, dict)
    assert sum(result.values()) == -150.0


def test_spending_by_workday(sample_df: pd.DataFrame) -> None:
    result = spending_by_workday(sample_df)

    assert isinstance(result, dict)
    assert "workday" in result
    assert "weekend" in result
