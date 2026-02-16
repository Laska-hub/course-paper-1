from pathlib import Path
import pandas as pd

DATA_PATH: Path = Path("data/operations.xlsx")


def load_operations() -> pd.DataFrame:
    """Загружает операции из Excel файла."""
    df: pd.DataFrame = pd.read_excel(DATA_PATH)

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
