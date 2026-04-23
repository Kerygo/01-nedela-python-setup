import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    """Nolasa izdevumus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_expenses(expenses):
    """Saglabā izdevumu sarakstu JSON failā."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)