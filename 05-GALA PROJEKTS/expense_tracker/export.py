import csv

def export_to_csv(expenses, filepath="izdevumi.csv"):
    """Eksportē izdevumus CSV failā, ko var atvērt Excel."""
    if not expenses:
        return False
        
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
        for exp in expenses:
            writer.writerow([exp["date"], f"{exp['amount']:.2f}", exp["category"], exp["description"]])
    return True