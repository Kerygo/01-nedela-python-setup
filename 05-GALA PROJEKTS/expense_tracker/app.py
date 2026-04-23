from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category
from export import export_to_csv

def show_menu():
    print("\n" + "="*30)
    print("   IZDEVUMU IZSEKOTĀJS")
    print("="*30)
    print("1. Pievienot izdevumu")
    print("2. Parādīt visus izdevumus")
    print("3. Kopsavilkums pa kategorijām")
    print("4. Eksportēt uz CSV (Excel)")
    print("5. Iziet")
    return input("\nIzvēlies darbību (1-5): ")

def add_expense(expenses):
    print("\n--- Jauns izdevums ---")
    date = input("Datums (YYYY-MM-DD) [šodien - Enter]: ")
    if not date:
        from datetime import date as dt
        date = dt.today().strftime("%Y-%m-%d")
    
    try:
        amount = float(input("Summa (EUR): "))
    except ValueError:
        print("❌ Kļūda: Ievadi skaitli!")
        return
    
    category = input("Kategorija (Ēdiens, Transports, Izklaide, uc.): ")
    description = input("Apraksts: ")
    
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    save_expenses(expenses)
    print("✅ Pievienots!")

def main():
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print(f"\n{'Datums':<12} | {'Summa':>8} | {'Kategorija':<12} | {'Apraksts'}")
            print("-" * 50)
            for e in expenses:
                print(f"{e['date']:<12} | {e['amount']:>8.2f} | {e['category']:<12} | {e['description']}")
            print(f"\nKOPĀ: {sum_total(expenses):.2f} EUR")
        elif choice == "3":
            print("\n--- Pa kategorijām ---")
            for cat, total in sum_by_category(expenses).items():
                print(f"{cat:<15}: {total:>8.2f} EUR")
        elif choice == "4":
            if export_to_csv(expenses):
                print("✅ Dati eksportēti uz 'izdevumi.csv'!")
            else:
                print("❌ Nav datu, ko eksportēt.")
        elif choice == "5":
            print("Uz redzēšanos!")
            break

if __name__ == "__main__":
    main()