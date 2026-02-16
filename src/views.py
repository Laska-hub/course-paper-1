from typing import List, Dict

import pandas as pd

from src.reports import spending_by_category, spending_by_weekday


def main_page() -> Dict[str, str]:
    """Главная страница."""
    return {"message": "Главная страница"}


def events_page(
    df: pd.DataFrame,
    category: str,
) -> List[Dict[str, float]]:
    """Возвращает траты по выбранной категории."""
    result_df = spending_by_category(df, category)

    return [
        {
            "category": row["Категория"],
            "amount": float(row["Сумма операции"]),
        }
        for _, row in result_df.iterrows()
    ]


def weekday_page(
    df: pd.DataFrame,
) -> List[Dict[str, float]]:
    """Возвращает средние траты по дням недели."""
    result_df = spending_by_weekday(df)

    return [
        {
            "weekday": row["weekday"],
            "amount": float(row["Сумма операции"]),
        }
        for _, row in result_df.iterrows()
    ]
