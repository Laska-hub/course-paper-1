from datetime import datetime
from typing import Dict

from src.data_loader import load_operations


def _filter_by_period(df, date_from: str, date_to: str):
    """Фильтрация по периоду."""
    start = datetime.strptime(date_from, "%Y-%m-%d")
    end = datetime.strptime(date_to, "%Y-%m-%d")

    return df[(df["Дата операции"] >= start) & (df["Дата операции"] <= end)]


def cashback_analysis(date_from: str, date_to: str) -> Dict[str, float]:
    """
    Возвращает сумму кэшбэка по категориям за период.
    """
    df = load_operations()

    df = df[df["Статус"] == "OK"]
    df = df[df["Сумма операции"] < 0]  # только расходы
    df = _filter_by_period(df, date_from, date_to)

    result = (
        df.groupby("Категория")["Бонусы (включая кэшбэк)"]
        .sum()
        .to_dict()
    )

    return result


def investment_analysis(date_from: str, date_to: str) -> float:
    """
    Считает сумму округлений за период.
    """
    df = load_operations()

    df = df[df["Статус"] == "OK"]
    df = _filter_by_period(df, date_from, date_to)

    total = df["Округление на инвесткопилку"].sum()

    return float(total)
