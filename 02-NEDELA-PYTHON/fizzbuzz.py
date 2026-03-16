# 1. Krāsu definīcijas (tavas mīļākās)
ZALS = '\033[92m'
ZILS = '\033[94m'
DZELTENS = '\033[93m'
RESET = '\033[0m'

# 2. Galvenais cikls, lai programma nebeigtos uzreiz
while True:
    print("\n--- FIZZBUZZ PROGRAMMA ---")
    ievade = input("Līdz kuram skaitlim skaitīsim? (raksti 'q' lai izietu): ")

    # 3. Pārbaudām, vai lietotājs grib beigt
    if ievade.lower() == 'q':
        print("Programma beidz darbu. Atā!")
        break

    # 4. Mēģinām pārvērst ievadi par skaitli
    try:
        n = int(ievade)
        
        # 5. Pati FizzBuzz loģika (tikai 3 un 5)
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{DZELTENS}FizzBuzz{RESET}")
            elif i % 3 == 0:
                print(f"{ZALS}Fizz{RESET}")
            elif i % 5 == 0:
                print(f"{ZILS}Buzz{RESET}")
            else:
                print(i)
                
    except ValueError:
        print("Kļūda! Lūdzu ievadi veselu skaitli vai 'q'.")