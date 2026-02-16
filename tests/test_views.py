from src.utils import load_operations
from src.views import events_page, main_page, weekday_page


def test_main_page() -> None:
    """Тестирование главной страницы."""
    result = main_page()
    assert isinstance(result, dict)
    assert result["message"] == "Главная страница"


def test_events_page() -> None:
    """Тестирование events_page."""
    df = load_operations()

    result = events_page(df, "Супермаркеты")

    assert isinstance(result, list)
    assert all("category" in op for op in result)
    assert all("amount" in op for op in result)


def test_weekday_page() -> None:
    """Тестирование weekday_page."""
    df = load_operations()

    result = weekday_page(df)

    assert isinstance(result, list)
    assert all("weekday" in day for day in result)
    assert all("amount" in day for day in result)
