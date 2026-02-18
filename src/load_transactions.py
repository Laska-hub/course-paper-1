from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, cast


def load_transactions() -> List[Dict[str, Any]]:
    """Загрузка транзакций из JSON файла."""
    file_path = Path("data/transactions.json")

    if not file_path.exists():
        return []

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    return cast(List[Dict[str, Any]], data)
