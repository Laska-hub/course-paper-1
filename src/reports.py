from typing import Dict, List

import pandas as pd


def spending_by_category(
    transactions: pd.DataFrame, category: str
) -> List[Dict[str, float]]:
    """
    Возвращает список транзакций по указанной категории.
    """
    filtered = transactions[transactions["category"] == category]
    result: List[Dict[str, float]] = []
    for _, row in filtered.iterrows():
        result.append(
            {
                "amount": float(row["amount"]),
                "cashback": float(row.get("cashback", 0)),
            }
        )
    return result


def spending_by_weekday(transactions: pd.DataFrame) -> Dict[str, float]:
    """
    Считает сумму расходов по дням недели.
    """
    df = transactions.copy()
    df["weekday"] = df["date"].dt.day_name()
    weekday_sum = df.groupby("weekday")["amount"].sum().to_dict()
    return {k: float(v) for k, v in weekday_sum.items()}


def spending_by_workday(transactions: pd.DataFrame) -> Dict[str, float]:
    """
    Считает сумму расходов по рабочим дням (понедельник–пятница).
    """
    df = transactions.copy()
    df["weekday"] = df["date"].dt.day_name()
    workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    df = df[df["weekday"].isin(workdays)]
    weekday_sum = df.groupby("weekday")["amount"].sum().to_dict()
    return {k: float(v) for k, v in weekday_sum.items()}
