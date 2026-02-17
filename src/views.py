from typing import Dict, List

from src.services import search_person_transfers, search_phone_numbers


def display_phone_transactions(
    transactions: List[Dict], phone: str
) -> List[Dict]:
    """Возвращает транзакции с указанным номером телефона"""
    return search_phone_numbers(transactions, phone)


def display_person_transfers(
    transactions: List[Dict], person: str
) -> List[Dict]:
    """Возвращает переводы указанному человеку"""
    return search_person_transfers(transactions, person)
