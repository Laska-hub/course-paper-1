from __future__ import annotations

from typing import Dict, List, cast

import pandas as pd

from src.decorators import report_logger


@report_logger
def spending_by_category(
    df: pd.DataFrame,
    category: str,
) -> List[Dict[str, float]]:
    """
    Возвращает список операций по выбранной категории
    с расчетом кэшбэка (1%).
    """
    if df.empty:
        return []

    filtered_df = df[df["category"] == category]

    if filtered_df.empty:
        return []

    result: List[Dict[str, float]] = []

    for _, row in filtered_df.iterrows():
        amount = float(row["amount"])
        cashback = abs(amount) * 0.01 if amount < 0 else 0.0

        result.append(
            {
                "amount": amount,
                "cashback": round(cashback, 2),
            }
        )

    return result


@report_logger
def spending_by_weekday(
    df: pd.DataFrame,
) -> Dict[str, float]:
    """
    Возвращает сумму расходов по дням недели.
    """
    if df.empty:
        return {}

    df_copy = df.copy()
    df_copy["weekday"] = df_copy["date"].dt.day_name()

    expenses = df_copy[df_copy["amount"] < 0]

    grouped = expenses.groupby("weekday")["amount"].sum()

    return cast(Dict[str, float], grouped.to_dict())


@report_logger
def spending_by_workday(
    df: pd.DataFrame,
) -> Dict[str, float]:
    """
    Возвращает сумму расходов отдельно по
    рабочим и выходным дням.
    """
    if df.empty:
        return {}

    df_copy = df.copy()
    df_copy["is_workday"] = df_copy["date"].dt.weekday < 5

    expenses = df_copy[df_copy["amount"] < 0]

    grouped = expenses.groupby("is_workday")["amount"].sum()

    result: Dict[str, float] = {
        "workday": float(grouped.get(True, 0.0)),
        "weekend": float(grouped.get(False, 0.0)),
    }

    return result
