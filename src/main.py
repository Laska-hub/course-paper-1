from typing import Any, Dict

from src.services import (
    cashback_analysis,
    get_currency_rates,
    get_stock_prices,
    investment_bank,
)
from src.views import generate_json_response


def main() -> None:
    # Пример данных
    data: Dict[str, Any] = {"a": 1}

    # Генерация JSON-ответа
    generate_json_response(data)

    # Получение курсов валют
    rates: Dict[str, float] = get_currency_rates("USD")
    print("Currency rates:", rates)

    # Получение цен акций
    stock_data: Dict[str, Any] = get_stock_prices("AAPL")
    print("Stock data:", stock_data)

    # Пример транзакций для кэшбэка
    transactions = [
        {"amount": 100, "cashback": 1.5},
        {"amount": 200, "cashback": 3.0},
    ]
    total_cashback: float = cashback_analysis(transactions)
    print("Total cashback:", total_cashback)

    # Пример инвестиций в банк
    total_invested: float = investment_bank(transactions)
    print("Total invested:", total_invested)


if __name__ == "__main__":
    main()
