from pathlib import Path
import pandas as pd


DATA_PATH = Path("data/operations.xlsx")


def load_operations() -> pd.DataFrame:
    """Загружает операции из Excel файла."""
    df = pd.read_excel(DATA_PATH)

    # Приводим числовые колонки к нормальному виду
    df["Сумма операции"] = (
        df["Сумма операции"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df["Сумма платежа"] = (
        df["Сумма платежа"]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    return df
