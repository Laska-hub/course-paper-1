from typing import List, Dict


def cashback_analysis(operations: List[Dict[str, float]]) -> Dict[str, float]:
    """Считает cashback по категориям"""
    cashback_dict: Dict[str, float] = {}
    for op in operations:
        category = str(op["Категория"])
        amount = float(op.get("Кэшбэк", 0.0))
        cashback_dict[category] = cashback_dict.get(category, 0.0) + amount
    return cashback_dict


def investment_bank(operations: List[Dict[str, float]]) -> float:
    """Считает сумму округлений на инвесткопилку"""
    total: float = 0.0
    for op in operations:
        total += float(op.get("Округление на инвесткопилку", 0.0))
    return total
