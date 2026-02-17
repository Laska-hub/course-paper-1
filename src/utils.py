# src/utils.py
from pathlib import Path

import pandas as pd

DATA_PATH: Path = Path("data/operations.xlsx")


def load_operations() -> pd.DataFrame:
    """Загружает операции из Excel файла и приводит к стандартной структуре."""
    df: pd.DataFrame = pd.read_excel(DATA_PATH)

    # Преобразуем даты (явно dayfirst)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)

    # Числовые поля
    df["Сумма операции"] = (
        df["Сумма операции"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df["Бонусы (включая кэшбэк)"] = (
        df["Бонусы (включая кэшбэк)"]
        .fillna(0)
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df["Округление на инвесткопилку"] = (
        df["Округление на инвесткопилку"]
        .fillna(0)
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    # Приводим к стандартным колонкам
    df_standard = pd.DataFrame()
    df_standard["date"] = df["Дата операции"]
    df_standard["amount"] = df["Сумма операции"]
    df_standard["category"] = df.get("Категория", "Неизвестно")
    df_standard["description"] = df.get("Описание", "")
    df_standard["card_last_digits"] = (
        df.get("Номер карты", "").astype(str).str[-4:]
    )

    return df_standard
