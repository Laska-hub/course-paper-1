# src/views.py
from datetime import datetime
from typing import Dict, List

import pandas as pd


def greeting_by_time(now: datetime) -> str:
    hour = now.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    if 12 <= hour < 17:
        return "Добрый день"
    if 17 <= hour < 23:
        return "Добрый вечер"
    return "Доброй ночи"


def main_page(transactions: List[Dict], date_str: str) -> Dict:
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    start_month = current_date.replace(day=1)
    df = pd.DataFrame(transactions)
    df["date"] = pd.to_datetime(df["date"])
    df = df[(df["date"] >= start_month) & (df["date"] <= current_date)]

    greet = greeting_by_time(current_date)

    cards_summary = []
    grouped = df.groupby("card_last_digits")["amount"].sum().reset_index()
    for _, row in grouped.iterrows():
        total = row["amount"]
        cashback = total * 0.01
        cards_summary.append(
            {
                "last_digits": row["card_last_digits"],
                "total_spent": total,
                "cashback": cashback,
            }
        )

    top_transactions = df.nlargest(5, "amount")[
        ["date", "amount", "category", "description", "card_last_digits"]
    ]
    top_transactions_list = top_transactions.to_dict("records")

    currency_rates = [
        {"currency": "USD", "rate": 73.0},
        {"currency": "EUR", "rate": 85.0},
    ]
    stock_prices = [
        {"stock": "AAPL", "price": 150.0},
        {"stock": "AMZN", "price": 3200.0},
        {"stock": "GOOGL", "price": 2750.0},
        {"stock": "MSFT", "price": 300.0},
        {"stock": "TSLA", "price": 1000.0},
    ]

    return {
        "greeting": greet,
        "cards": cards_summary,
        "top_transactions": top_transactions_list,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }


def events_page(
    transactions: List[Dict], date_str: str, period: str = "M"
) -> Dict:
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    df = pd.DataFrame(transactions)
    df["date"] = pd.to_datetime(df["date"])

    if period == "W":
        start_date = current_date - pd.Timedelta(days=current_date.weekday())
    elif period == "M":
        start_date = current_date.replace(day=1)
    elif period == "Y":
        start_date = current_date.replace(month=1, day=1)
    else:
        start_date = df["date"].min()

    df_period = df[(df["date"] >= start_date) & (df["date"] <= current_date)]

    df_expenses = df_period[df_period["amount"] < 0]
    df_income = df_period[df_period["amount"] > 0]

    def summarize(df_sub: pd.DataFrame) -> Dict:
        main = df_sub.groupby("category")["amount"].sum().reset_index()
        main = main.sort_values("amount", ascending=True)
        total = main["amount"].sum()
        main_list = main.head(7).to_dict("records")
        if len(main) > 7:
            rest_sum = main["amount"][7:].sum()
            main_list.append({"category": "Остальное", "amount": rest_sum})
        return {"total_amount": round(total), "main": main_list}

    expenses_summary = summarize(df_expenses)
    income_summary = summarize(df_income)

    currency_rates = [
        {"currency": "USD", "rate": 73.0},
        {"currency": "EUR", "rate": 85.0},
    ]
    stock_prices = [
        {"stock": "AAPL", "price": 150.0},
        {"stock": "AMZN", "price": 3200.0},
        {"stock": "GOOGL", "price": 2750.0},
        {"stock": "MSFT", "price": 300.0},
        {"stock": "TSLA", "price": 1000.0},
    ]

    return {
        "expenses": expenses_summary,
        "income": income_summary,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
