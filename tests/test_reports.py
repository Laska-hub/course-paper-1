from src.reports import spending_by_category, spending_by_weekday
from src.utils import load_operations


def test_spending_by_category_real() -> None:
    df = load_operations()
    category = df["Категория"].dropna().iloc[0]

    result = spending_by_category(df, category)
    assert not result.empty


def test_spending_by_weekday_real() -> None:
    df = load_operations()

    result = spending_by_weekday(df)
    # разбиваем длинную строку на несколько строк
    assert "weekday" in result.columns and "Сумма операции" in result.columns
    assert not result.empty
