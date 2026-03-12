import random

skaitlis = random.randint(1, 100)
meginajumi = 0

print("Es iedomājos skaitli no 1 līdz 100. Uzmini!")

while True:
    ievade = input("Tava izvēle: ")
    meginajumi += 1
    
    try:
        minējums = int(ievade)
        if minējums < skaitlis:
            print("Par mazu!")
        elif minējums > skaitlis:
            print("Par lielu!")
        else:
            print(f"UZVARA! Uzminēji ar {meginajumi}. reizi.")
            break
    except ValueError:
        print("Lūdzu, ievadi veselu skaitli!")