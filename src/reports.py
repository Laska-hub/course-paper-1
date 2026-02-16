from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict

import pandas as pd


def save_report(filename_func: Callable[..., str]):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            file_path = filename_func(None)  # игнорируем аргументы
            with open(file_path, "w", encoding="utf-8") as f:
                import json

                json.dump(result, f)
            return result

        return wrapper

    return decorator


def expenses_by_category(
    df: pd.DataFrame, category: str, date: datetime
) -> Dict[str, float]:
    df["Дата операции"] = pd.to_datetime(df["Дата операции"])
    filtered = df[
        (df["Категория"] == category) & (df["Дата операции"] <= date)
    ]
    total = filtered["Сумма операции"].sum()
    return {"total": total}


def expenses_by_weekday(df: pd.DataFrame) -> Dict[str, float]:
    df["Дата операции"] = pd.to_datetime(df["Дата операции"])
    df["weekday"] = df["Дата операции"].dt.day_name()
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    result: Dict[str, float] = {day: 0.0 for day in weekdays}
    grouped = df.groupby("weekday")["Сумма операции"].sum()
    for day, val in grouped.items():
        result[day] = val
    return result
