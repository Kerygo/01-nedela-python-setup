ZALS = '\033[92m'
SARKANS = '\033[91m'
RESET = '\033[0m'

while True:
    print("\n--- ATLAIDES PĀRBAUDE ---")
    ievade = input("Ievadi vecumu (vai 'q' lai izietu): ").lower()
    
    if ievade == 'q':
        break
        
    try:
        vecums = int(ievade)
        is_student = input("Vai esi students? (j/n): ").lower() == 'j'
        
        # Galvenais nosacījums:
        if (16 <= vecums <= 26) or is_student:
            print(f"{ZALS}Apsveicam! Tev pienākas studenta atlaide.{RESET}")
        else:
            print(f"{SARKANS}Diemžēl atlaide nepienākas.{RESET}")
            
    except ValueError:
        print("Lūdzu ievadi skaitli!")