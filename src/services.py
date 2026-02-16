from typing import Any, Dict, List


def cashback_analysis(transactions: List[Dict[str, Any]]) -> float:
    """Суммирует суммы кэшбэка"""
    total: float = 0.0
    for t in transactions:
        total += float(t.get("cashback", 0))
    return total


def investment_bank(transactions: List[Dict[str, Any]]) -> float:
    """Суммирует все инвестиции"""
    total_invested: float = sum(
        float(t.get("amount", 0)) for t in transactions
    )
    return total_invested


def get_currency_rates(base: str = "USD") -> Dict[str, float]:
    """Пример заглушки валютных курсов"""
    return {"USD": 1.0, "EUR": 0.95, "JPY": 145.0}


def get_stock_prices(symbol: str) -> Dict[str, float]:
    """Пример заглушки цен акций"""
    return {"AAPL": 175.0, "GOOGL": 2800.0}
