# app.py
import json
import logging
from datetime import datetime
from typing import Any

from flask import Flask, jsonify, request

from src.load_transactions import load_transactions

app = Flask("Finance API")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@app.route("/")
def index() -> Any:
    """Проверка работоспособности API."""
    return jsonify({"status": "Finance API is running"})


@app.route("/main")
def main_endpoint() -> Any:
    """Главная страница с краткой информацией."""
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "Missing date parameter"}), 400

    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return (
            jsonify(
                {"error": "Invalid date format, expected YYYY-MM-DD HH:MM:SS"}
            ),
            400,
        )

    transactions = load_transactions()

    response = {
        "greeting": "Добрый вечер",
        "cards": [],
        "currency_rates": [
            {"currency": "USD", "rate": 73.0},
            {"currency": "EUR", "rate": 85.0},
        ],
        "stock_prices": [
            {"stock": "AAPL", "price": 150.0},
            {"stock": "AMZN", "price": 3200.0},
            {"stock": "GOOGL", "price": 2750.0},
            {"stock": "MSFT", "price": 300.0},
            {"stock": "TSLA", "price": 1000.0},
        ],
        "top_transactions": transactions[:5],
    }

    logger.info(
        "Response:\n%s",
        json.dumps(response, ensure_ascii=False, indent=2),
    )
    return jsonify(response)


@app.route("/events")
def events_endpoint() -> Any:
    """Страница событий с доходами и расходами."""
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "Missing date parameter"}), 400

    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return (
            jsonify(
                {"error": "Invalid date format, expected YYYY-MM-DD HH:MM:SS"}
            ),
            400,
        )

    transactions = load_transactions()

    expenses = [t for t in transactions if t["amount"] < 0]
    income = [t for t in transactions if t["amount"] > 0]

    response = {
        "currency_rates": [
            {"currency": "USD", "rate": 73.0},
            {"currency": "EUR", "rate": 85.0},
        ],
        "expenses": {
            "main": expenses,
            "total_amount": sum(t["amount"] for t in expenses),
        },
        "income": {
            "main": income,
            "total_amount": sum(t["amount"] for t in income),
        },
        "stock_prices": [
            {"stock": "AAPL", "price": 150.0},
            {"stock": "AMZN", "price": 3200.0},
            {"stock": "GOOGL", "price": 2750.0},
            {"stock": "MSFT", "price": 300.0},
            {"stock": "TSLA", "price": 1000.0},
        ],
    }

    logger.info(
        "Response:\n%s",
        json.dumps(response, ensure_ascii=False, indent=2),
    )
    return jsonify(response)


if __name__ == "__main__":
    logger.info("Starting Finance API...")
    app.run(host="127.0.0.1", port=5001, debug=False)
