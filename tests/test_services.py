from typing import Dict, List

from src.services import (
    calculate_cashback,
    investment_bank,
    search_person_transfers,
    search_phone_numbers,
)

sample_transactions: List[Dict] = [
    {"amount": -100, "category": "Супермаркеты", "description": "Магазин А"},
    {"amount": 200, "category": "Пополнения", "description": "Зарплата"},
    {"amount": -50, "category": "Фастфуд", "description": "KFC"},
]


def test_calculate_cashback() -> None:
    cashback = calculate_cashback(sample_transactions)
    assert cashback["Супермаркеты"] == -1.0
    assert cashback["Пополнения"] == 2.0
    assert cashback["Фастфуд"] == -0.5


def test_investment_bank() -> None:
    total = investment_bank(sample_transactions, months=2, monthly_income=1000)
    expected_total = 2 * 1000 + sum(tx["amount"] for tx in sample_transactions)
    assert total == expected_total


def test_search_phone_numbers() -> None:
    transactions = [
        {"description": "Оплата 1234567890", "amount": -100},
        {"description": "Подарок 0987654321", "amount": -50},
    ]
    result = search_phone_numbers(transactions, "1234567890")
    assert len(result) == 1
    assert result[0]["amount"] == -100


def test_search_person_transfers() -> None:
    transactions = [
        {"description": "Перевод Иван Иванов", "amount": -200},
        {"description": "Перевод Петр Петров", "amount": -150},
    ]
    result = search_person_transfers(transactions, "Иван Иванов")
    assert len(result) == 1
    assert result[0]["amount"] == -200
