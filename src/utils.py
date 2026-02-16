import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/transactions.xlsx")  # используем реальный файл в data/

def load_operations() -> pd.DataFrame:
    """Загружает операции из Excel файла с преобразованием типов."""
    df = pd.read_excel(DATA_PATH)

    # Преобразуем даты
    df["Дата операции"] = pd.to_datetime(df["Дата операции"])

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

    return df
