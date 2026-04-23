import json
import os

# Failu nosaukumi
FILE_NAME = "shopping_list.json"
PRICES_FILE = "prices.json"

# --- IEPIRKUMU SARAKSTA FUNKCIJAS ---

def load_list():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_list(items):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)

# --- CENU DATUBĀZES FUNKCIJAS ---

def load_prices():
    """Nolasa prices.json, atgriež vārdnīcu."""
    if not os.path.exists(PRICES_FILE):
        return {}
    with open(PRICES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            return {}

def save_prices(prices):
    """Saglabā cenu vārdnīcu JSON failā."""
    with open(PRICES_FILE, 'w', encoding='utf-8') as f:
        json.dump(prices, f, indent=4, ensure_ascii=False)

def get_price(name):
    """Atgriež cenu konkrētam produktam vai None."""
    prices = load_prices()
    return prices.get(name)

def set_price(name, price):
    """Saglabā vai atjaunina cenu datubāzē."""
    prices = load_prices()
    prices[name] = float(price) # Pārvēršam par skaitli drošībai
    save_prices(prices)