from typing import Dict, List

from src.views import display_person_transfers, display_phone_transactions

sample_transactions: List[Dict] = [
    {"description": "Оплата 1234567890", "amount": -100},
    {"description": "Перевод Иван Иванов", "amount": -200},
]


def test_display_phone_transactions() -> None:
    result = display_phone_transactions(sample_transactions, "1234567890")
    assert len(result) == 1
    assert result[0]["amount"] == -100


def test_display_person_transfers() -> None:
    result = display_person_transfers(sample_transactions, "Иван Иванов")
    assert len(result) == 1
    assert result[0]["amount"] == -200
