import sys
import storage
import utils

def main():
    # 1. Ielādējam esošo iepirkumu sarakstu
    items = storage.load_list()
    
    # Pārbaudām, vai ir ievadīta vismaz viena komanda
    if len(sys.argv) < 2:
        print("Lieto: python shop.py [komanda]")
        return

    cmd = sys.argv[1]

    # --- KOMANDA: LIST ---
    if cmd == "list":
        for i, item in enumerate(items, 1):
            line_sum = utils.calc_line_total(item)
            print(f"{i}. {item['name']} - {item['qty']} x {item['price']} = {line_sum:.2f} EUR")

    # --- KOMANDA: TOTAL ---
    elif cmd == "total":
        print(f"Kopā: {utils.calc_grand_total(items):.2f} EUR")

    # --- KOMANDA: ADD ---
    elif cmd == "add":
        try:
            if len(sys.argv) < 4:
                print("Kļūda! Lieto: add [vārds] [skaits]")
                return
                
            name = sys.argv[2]
            qty = int(sys.argv[3])
            
            # Meklējam cenu cenu datubāzē
            price = storage.get_price(name)
            
            if price is not None:
                print(f"Atrasta cena: {price:.2f} EUR")
                izvele = input("[A]kceptēt / [M]ainīt? ").lower()
                if izvele == "m":
                    price = float(input("Ievadi jaunu cenu (ar punktu!): "))
                    storage.set_price(name, price)
            else:
                print("Cena nav zināma.")
                price = float(input("Ievadi cenu (ar punktu!): "))
                storage.set_price(name, price)
                
            items.append({"name": name, "qty": qty, "price": price})
            storage.save_list(items)
            print(f"✓ Pievienots: {name} x {qty}")
            
        except ValueError:
            print("Kļūda! Skaits un cena jāievada kā skaitļi (izmanto punktu, nevis komatu).")
        except Exception as e:
            print(f"Notika kļūda: {e}")

    # --- KOMANDA: REMOVE ---
    elif cmd == "remove":
        try:
            if len(sys.argv) < 3:
                print("Kļūda! Lieto: remove [vārds]")
                return
            
            name_to_remove = sys.argv[2]
            original_count = len(items)
            items = [item for item in items if item['name'] != name_to_remove]
            
            if len(items) < original_count:
                storage.save_list(items)
                print(f"✓ Izdzēsts: {name_to_remove}")
            else:
                print(f"Prece '{name_to_remove}' netika atrasta sarakstā.")
        except Exception as e:
            print(f"Kļūda dzēšot: {e}")

    else:
        print("Nezināma komanda!")

# Palaižam galveno funkciju
if __name__ == "__main__":
    main()