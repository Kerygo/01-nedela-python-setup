import sys
import storage
import utils

def main():
    items = storage.load_list()
    
    if len(sys.argv) < 2:
        print("Komandas: add, list, total, clear")
        return

    cmd = sys.argv[1]

    if cmd == "add":
        # Lietošana: python shop.py add Maize 3 1.20
        try:
            name = sys.argv[2]
            qty = int(sys.argv[3])
            price = float(sys.argv[4])
            items.append({"name": name, "qty": qty, "price": price})
            storage.save_list(items)
            print(f"✓ Pievienots: {name} x {qty}")
        except:
            print("Kļūda! Lieto: add [vārds] [skaits] [cena]")

    elif cmd == "list":
        for i, item in enumerate(items, 1):
            line_sum = utils.calc_line_total(item)
            print(f"{i}. {item['name']} - {item['qty']} x {item['price']} = {line_sum:.2f} EUR")

    elif cmd == "total":
        print(f"Kopā: {utils.calc_grand_total(items):.2f} EUR")

if __name__ == "__main__":
    main()