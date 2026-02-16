from typing import List, Dict

from src.services import cashback_analysis, investment_bank


def test_cashback_analysis_real() -> None:
    """Тестирование функции cashback_analysis."""
    sample_data: List[Dict[str, float]] = [
        {"Категория": 1.0, "Кэшбэк": 1.0},
        {"Категория": 1.0, "Кэшбэк": 2.0},
        {"Категория": 2.0, "Кэшбэк": 3.0},
    ]

    result = cashback_analysis(sample_data)

    assert isinstance(result, dict)
    assert result["1.0"] == 3.0
    assert result["2.0"] == 3.0


def test_investment_analysis_real() -> None:
    """Тестирование функции investment_bank."""
    sample_data: List[Dict[str, float]] = [
        {"Округление на инвесткопилку": 0.5},
        {"Округление на инвесткопилку": 1.2},
        {"Округление на инвесткопилку": 0.3},
    ]

    total = investment_bank(sample_data)

    assert isinstance(total, float)
    assert total == 2.0
