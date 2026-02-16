from datetime import datetime, timedelta

from src.reports import spending_by_category, spending_by_weekday
from src.services import cashback_analysis, investment_bank
from src.utils import load_operations
from src.views import events_page, main_page, weekday_page


def check_excel() -> None:
    """Проверка загрузки Excel."""
    print("=== Проверка загрузки Excel ===")
    df = load_operations()
    print("Первые 5 строк данных:")
    print(df.head())
    print("Колонки:", list(df.columns))
    print()


def check_reports() -> None:
    """Проверка reports.py."""
    print("=== Проверка reports.py ===")
    df = load_operations()

    category = (
        "Супермаркеты"
        if "Супермаркеты" in df["Категория"].values
        else df["Категория"].dropna().iloc[0]
    )

    cat_report = spending_by_category(df, category)
    print(f"Траты по категории '{category}':")
    print(cat_report)
    print()

    weekday_report = spending_by_weekday(df)
    print("Средние траты по дням недели:")
    print(weekday_report)
    print()


def check_services() -> None:
    """Проверка services.py."""
    print("=== Проверка services.py ===")
    df = load_operations()

    start_date = datetime.now() - timedelta(days=90)

    recent_transactions = [
        {
            "amount": float(row["Сумма операции"]),
            "cashback": float(
                row.get("Бонусы (включая кэшбэк)", 0.0)
            ),
            "rounding": float(
                row.get("Округление на инвесткопилку", 0.0)
            ),
            "category": str(
                row.get("Категория", "Другое")
            ),
        }
        for _, row in df.iterrows()
        if row["Дата операции"] >= start_date
    ]

    cashback_result = cashback_analysis(recent_transactions)
    print("Кэшбэк по категориям за последние 3 месяца:")
    print(cashback_result)
    print()

    total_invest = investment_bank(recent_transactions)
    print(
        "Сумма округлений на инвесткопилку за последние 3 месяца:",
        total_invest,
    )
    print()


def check_views() -> None:
    """Проверка views.py."""
    print("=== Проверка views.py ===")
    print("Главная страница JSON:")
    print(main_page())
    print()

    df = load_operations()

    category = (
        "Супермаркеты"
        if "Супермаркеты" in df["Категория"].values
        else df["Категория"].dropna().iloc[0]
    )

    cat_page = events_page(df, category)
    print("Отчет по категории через views:")
    print(cat_page)
    print()

    weekday_page_report = weekday_page(df)
    print("Средние траты по дням недели через views:")
    print(weekday_page_report)
    print()


if __name__ == "__main__":
    check_excel()
    check_reports()
    check_services()
    check_views()
