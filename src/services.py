from typing import Dict, List


def calculate_cashback(transactions: List[Dict]) -> Dict[str, float]:
    """Считает кешбэк по категориям"""
    cashback_dict: Dict[str, float] = {}
    for tx in transactions:
        category = tx.get("category", "Другое")
        amount = float(tx.get("amount", 0))
        cashback = amount * 0.01  # 1% cashback
        cashback_dict[category] = cashback_dict.get(category, 0) + cashback
    return cashback_dict


def investment_bank(
    transactions: List[Dict], months: int, monthly_income: float
) -> float:
    """Считает накопления в банке за месяцы с учётом транзакций"""
    total: float = months * monthly_income
    for tx in transactions:
        amount = float(tx.get("amount", 0))
        total += amount  # расходы отрицательные, пополнения положительные
    return total


def search_phone_numbers(transactions: List[Dict], phone: str) -> List[Dict]:
    """Ищет транзакции по номеру телефона"""
    return [
        tx for tx in transactions if phone in str(tx.get("description", ""))
    ]


def search_person_transfers(
    transactions: List[Dict], person: str
) -> List[Dict]:
    """Ищет переводы конкретному человеку"""
    return [
        tx for tx in transactions if person in str(tx.get("description", ""))
    ]
