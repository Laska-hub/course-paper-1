import pandas as pd

from src.reports import spending_by_category
from src.services import calculate_cashback, investment_bank
from src.views import display_person_transfers, display_phone_transactions

# Пример данных
data = [
    {
        "date": "2021-12-31 16:44:00",
        "amount": -160.89,
        "category": "Супермаркеты",
        "description": "Колхоз",
        "card_last_digits": "7197",
    },
    {
        "date": "2021-12-31 16:42:00",
        "amount": -64.0,
        "category": "Супермаркеты",
        "description": "Колхоз",
        "card_last_digits": "7197",
    },
    {
        "date": "2021-12-31 16:39:00",
        "amount": -118.12,
        "category": "Супермаркеты",
        "description": "Магнит",
        "card_last_digits": "7197",
    },
    {
        "date": "2021-12-31 15:44:00",
        "amount": -78.05,
        "category": "Супермаркеты",
        "description": "Колхоз",
        "card_last_digits": "7197",
    },
    {
        "date": "2021-12-31 01:23:00",
        "amount": -564.0,
        "category": "Различные товары",
        "description": "Ozon.ru",
        "card_last_digits": "5091",
    },
]

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

print("✅ Данные загружены и приведены к стандартной структуре:")
print(df.head())

# Кэшбэк
transactions_list = df.to_dict("records")
cashback_report = calculate_cashback(transactions_list)
print("\n=== Cashback Analysis ===")
print(cashback_report)

# Инвестиции
investment = investment_bank(transactions_list, 12, 1000)
print("\n=== Investment Bank ===")
print(investment)

# Поиск транзакций по категории
cat_report = spending_by_category(df, "Супермаркеты")
print("\n=== Spending by Category ===")
print(cat_report)

# Поиск по телефонам
phone_report = display_phone_transactions(transactions_list, "+7 921 11-22-33")
print("\n=== Search Phone Numbers ===")
print(phone_report)

# Поиск переводов конкретным людям
person_report = display_person_transfers(transactions_list, "Колхоз")
print("\n=== Search Person Transfers ===")
print(person_report)
