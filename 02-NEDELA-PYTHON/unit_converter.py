# Konstantes
KM_TO_MILES = 0.621371
MILES_TO_KM = 1.60934
KG_TO_G = 1000

while True:
    print("\n--- UNIVERSĀLAIS KONVERTERIS ---")
    print("1. Kilometri -> Jūdzes")
    print("2. Jūdzes -> Kilometri")
    print("3. Kilogrami -> Grami")
    print("4. Grami -> Kilogrami")
    print("q. Iziet")

    izvele = input("Izvēlies darbību (1-4 vai 'q'): ").lower()

    if izvele == 'q':
        print("Visu labu! Programma beidz darbu.")
        break

    try:
        if izvele == '1':
            km = float(input("Ievadi kilometrus: "))
            print(f"Rezultāts: {km} km ir {km * KM_TO_MILES:.2f} jūdzes")
            
        elif izvele == '2':
            miles = float(input("Ievadi jūdzes: "))
            print(f"Rezultāts: {miles} jūdzes ir {miles * MILES_TO_KM:.2f} km")
            
        elif izvele == '3':
            kg = float(input("Ievadi kilogramus: "))
            print(f"Rezultāts: {kg} kg ir {kg * KG_TO_G} g")
            
        elif izvele == '4':
            g = float(input("Ievadi gramus: "))
            print(f"Rezultāts: {g} g ir {g / KG_TO_G} kg")
            
        else:
            print("Nepareiza izvēle, mēģini vēlreiz!")

    except ValueError:
        print("Kļūda! Lūdzu, ievadi skaitli, nevis burtus.")