import sys
import storage
import utils

def main():
    items = storage.load_list()
    
    if len(sys.argv) < 2:
        print("Lieto: python shop.py [komanda]")
        return

    cmd = sys.argv[1]

    if cmd == "list":
        for i, item in enumerate(items, 1):
            line_sum = utils.calc_line_total(item)
            print(f"{i}. {item['name']} - {item['qty']} x {item['price']} = {line_sum:.2f} EUR")

    elif cmd == "total":
        print(f"Kopā: {utils.calc_grand_total(items):.2f} EUR")

    elif cmd == "add":
        try:
            if len(sys.argv) < 4:
                print("Kļūda! Lieto: add [vārds] [skaits]")
                return
                
            name = sys.argv[2]
            qty = int(sys.argv[3])
            
            # Meklējam cenu prices.json caur storage.py
            price = storage.get_price(name)
            
            if price is not None:
                print(f"Atrasta cena: {price:.2f} EUR")
                izvele = input("[A]kceptēt / [M]ainīt? ").lower()
                if izvele == "m":
                    price = float(input("Ievadi jaunu cenu: "))
                    storage.set_price(name, price)
            else:
                print("Cena nav zināma.")
                price = float(input("Ievadi cenu: "))
                storage.set_price(name, price)
                
            items.append({"name": name, "qty": qty, "price": price})
            storage.save_list(items)
            print(f"✓ Pievienots: {name} x {qty}")
            
        except ValueError:
            print("Kļūda! Skaits un cena jāievada kā skaitļi.")
        except Exception as e:
            print(f"Notika kļūda: {e}")

    else:
        print("Nezināma komanda!")

if __name__ == "__main__":
    main()