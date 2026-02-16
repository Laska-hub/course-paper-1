import pandas as pd


def spending_by_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """Отчет по сумме расходов по категории."""
    result = df[df["Категория"] == category][["Категория", "Сумма операции"]]
    return result


def spending_by_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Средние расходы по дням недели."""
    df = df.copy()
    df["weekday"] = df["Дата операции"].dt.day_name()
    result = (
        df.groupby("weekday")["Сумма операции"]
        .mean()
        .abs()
        .round(2)
        .reset_index()
    )
    return result
