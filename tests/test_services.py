from src.services import (
    cashback_analysis,
    get_currency_rates,
    get_stock_prices,
    investment_bank,
)


def test_get_currency_rates() -> None:
    rates = get_currency_rates()
    assert "USD" in rates


def test_get_stock_prices() -> None:
    prices = get_stock_prices("AAPL")
    assert "AAPL" in prices


def test_cashback_analysis() -> None:
    dummy_transactions = [
        {"amount": 100, "cashback": 1.5},
        {"amount": 200, "cashback": 3.0},
    ]
    result = cashback_analysis(dummy_transactions)
    assert isinstance(result, float)
    assert result > 0


def test_investment_bank() -> None:
    dummy_transactions = [
        {"amount": 100, "cashback": 1.5},
        {"amount": 200, "cashback": 3.0},
    ]
    result = investment_bank(dummy_transactions)
    assert isinstance(result, float)
    assert result == 300
