from datetime import datetime

def sum_total(expenses):
    if not expenses:
        return 0
    return sum(exp["amount"] for exp in expenses)

def sum_by_category(expenses):
    totals = {}
    for exp in expenses:
        cat = exp["category"]
        totals[cat] = totals.get(cat, 0) + exp["amount"]
    return totals

def filter_by_month(expenses, year, month):
    filtered = []
    for exp in expenses:
        d = datetime.strptime(exp["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            filtered.append(exp)
    return filtered