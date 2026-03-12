KM_UZ_MILEM = 0.621371

# Sākam ciklu, lai programma nebeigtos pēc viena skaitļa
while True:
    print("\n--- Kilometru pārvērtējs ---")
    ievade = input("Ievadi kilometrus (vai 'stop', lai beigtu): ")

    # Pārbaudām, vai lietotājs grib iziet
    if ievade.lower() == "stop":
        print("Visu labu, Uz redzi!")
        break 

    try:
        km = float(ievade)
        miles = km * KM_UZ_MILEM
        print(f"Rezultāts: {km} km ir {miles:.2f} jūdzes.")
        print(f"Tu esi malacis!!!")
    except ValueError:
        print("Lūdzu, ieraksti skaitli!")